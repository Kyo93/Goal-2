param(
  [Parameter(Mandatory = $false)]
  [string]$ZabbixUrl = "https://zabbix.cit.insea.io/api_jsonrpc.php",

  [Parameter(Mandatory = $false)]
  [string]$Token = $env:ZABBIX_TOKEN,

  [Parameter(Mandatory = $false)]
  [string]$GroupName = "All VNM",

  [Parameter(Mandatory = $false)]
  [string]$Month = (Get-Date -Format "yyyy-MM"),

  [Parameter(Mandatory = $false)]
  [string[]]$Severities = @("High", "Disaster"),

  [Parameter(Mandatory = $false)]
  [string]$OutputDir = "Goal-2\RawData\Export zabbix",

  [Parameter(Mandatory = $false)]
  [switch]$SkipCertificateCheck
)

$ErrorActionPreference = "Stop"

if (-not $Token) {
  throw "Missing Zabbix API token. Set `$env:ZABBIX_TOKEN or pass -Token."
}

$severityToId = @{
  "Not classified" = 0
  "Information"    = 1
  "Warning"        = 2
  "Average"        = 3
  "High"           = 4
  "Disaster"       = 5
}
$idToSeverity = @{
  "0" = "Not classified"
  "1" = "Information"
  "2" = "Warning"
  "3" = "Average"
  "4" = "High"
  "5" = "Disaster"
}

$normalizedSeverities = @(
  $Severities |
    ForEach-Object { $_ -split "," } |
    ForEach-Object { $_.Trim() } |
    Where-Object { $_ -ne "" }
)

$severityIds = @()
foreach ($severity in $normalizedSeverities) {
  if (-not $severityToId.ContainsKey($severity)) {
    throw "Unsupported severity '$severity'. Valid values: $($severityToId.Keys -join ', ')"
  }
  $severityIds += $severityToId[$severity]
}

try {
  $monthStart = [DateTimeOffset]::ParseExact(
    "$Month-01T00:00:00+07:00",
    "yyyy-MM-ddTHH:mm:sszzz",
    [Globalization.CultureInfo]::InvariantCulture
  )
} catch {
  throw "Invalid -Month '$Month'. Use yyyy-MM, for example 2026-05."
}
$monthEnd = $monthStart.AddMonths(1)

if ($PSVersionTable.PSVersion.Major -lt 6) {
  Add-Type @"
using System.Net;
using System.Security.Cryptography.X509Certificates;
public class TrustAllCertsPolicy : ICertificatePolicy {
  public bool CheckValidationResult(ServicePoint srvPoint, X509Certificate certificate, WebRequest request, int certificateProblem) { return true; }
}
"@ -ErrorAction SilentlyContinue
  if ($SkipCertificateCheck) {
    [System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy
  }
  [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
}

$headers = @{
  Authorization  = "Bearer $Token"
  "Content-Type" = "application/json-rpc"
}

function Invoke-ZabbixApi {
  param(
    [Parameter(Mandatory = $true)][string]$Method,
    [Parameter(Mandatory = $true)][hashtable]$Params,
    [Parameter(Mandatory = $true)][int]$Id
  )

  $body = @{
    jsonrpc = "2.0"
    method  = $Method
    params  = $Params
    id      = $Id
  } | ConvertTo-Json -Depth 50

  $requestParams = @{
    Uri        = $ZabbixUrl
    Method     = "Post"
    Headers    = $headers
    Body       = $body
    TimeoutSec = 180
  }
  if ($PSVersionTable.PSVersion.Major -ge 6 -and $SkipCertificateCheck) {
    $requestParams.SkipCertificateCheck = $true
  }

  $response = Invoke-RestMethod @requestParams
  if ($response.error) {
    throw ($response.error | ConvertTo-Json -Depth 20)
  }

  return $response.result
}

function Format-ZabbixTime {
  param([object]$Clock)
  if (-not $Clock -or $Clock -eq "0") { return "" }
  return [DateTimeOffset]::FromUnixTimeSeconds([int64]$Clock).
    ToOffset([TimeSpan]::FromHours(7)).
    ToString("yyyy-MM-dd hh:mm:ss tt", [Globalization.CultureInfo]::InvariantCulture)
}

function Format-Duration {
  param([int64]$Seconds)
  if ($Seconds -lt 0) { $Seconds = 0 }

  $days = [math]::Floor($Seconds / 86400)
  $remaining = $Seconds % 86400
  $hours = [math]::Floor($remaining / 3600)
  $remaining = $remaining % 3600
  $minutes = [math]::Floor($remaining / 60)
  $secs = $remaining % 60

  $parts = New-Object System.Collections.Generic.List[string]
  if ($days -gt 0) { $parts.Add("${days}d") }
  if ($hours -gt 0) { $parts.Add("${hours}h") }
  if ($minutes -gt 0) { $parts.Add("${minutes}m") }
  if ($secs -gt 0 -or $parts.Count -eq 0) { $parts.Add("${secs}s") }
  return ($parts -join " ")
}

function Format-IsoLocalTime {
  param([object]$Clock)
  if (-not $Clock -or $Clock -eq "0") { return "" }
  return [DateTimeOffset]::FromUnixTimeSeconds([int64]$Clock).
    ToOffset([TimeSpan]::FromHours(7)).
    ToString("yyyy-MM-ddTHH:mm:sszzz", [Globalization.CultureInfo]::InvariantCulture)
}

function Format-IsoUtcTime {
  param([object]$Clock)
  if (-not $Clock -or $Clock -eq "0") { return "" }
  return [DateTimeOffset]::FromUnixTimeSeconds([int64]$Clock).
    ToUniversalTime().
    ToString("yyyy-MM-ddTHH:mm:ssZ", [Globalization.CultureInfo]::InvariantCulture)
}

function Get-SiteCodeFromHost {
  param([string]$HostName)
  $match = [regex]::Match($HostName.ToUpperInvariant(), "^VNM([A-Z0-9]{3})")
  if ($match.Success) { return $match.Groups[1].Value }
  return "UNKNOWN"
}

function Normalize-ProblemSignature {
  param([string]$Problem)
  $text = $Problem.ToLowerInvariant()
  $text = [regex]::Replace($text, "\(current [^)]+\)", "")
  $text = [regex]::Replace($text, "current:\s*\d+(?:\.\d+)?\s*mbps", "current:<value> mbps", "IgnoreCase")
  $text = [regex]::Replace($text, "\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?\s*(?:mbps|gbps|%|hz|m|s|c)\b", "<value>", "IgnoreCase")
  $text = [regex]::Replace($text, "\s+", " ").Trim()
  return $text
}

function Convert-Tags {
  param([object[]]$Tags)
  $map = [ordered]@{}
  foreach ($tagEntry in @($Tags)) {
    $tagName = [string]$tagEntry.tag
    $tagValue = [string]$tagEntry.value
    if (-not $tagName) { continue }
    if (-not $map.Contains($tagName)) {
      $map[$tagName] = New-Object System.Collections.Generic.List[string]
    }
    if ($tagValue -and -not $map[$tagName].Contains($tagValue)) {
      $map[$tagName].Add($tagValue)
    }
  }
  return $map
}

function Join-TagValues {
  param(
    [hashtable]$TagMap,
    [string]$Key
  )
  if (-not $TagMap.Contains($Key)) { return "UNKNOWN" }
  $values = @($TagMap[$Key]) | Where-Object { $_ -and $_ -ne "UNKNOWN" } | Sort-Object -Unique
  if ($values.Count -eq 0) { return "UNKNOWN" }
  return ($values -join ",")
}

if (-not (Test-Path $OutputDir)) {
  New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

$groupResult = Invoke-ZabbixApi -Method "hostgroup.get" -Params @{
  output = @("groupid", "name")
  filter = @{ name = @($GroupName) }
} -Id 100

if (-not $groupResult -or $groupResult.Count -eq 0) {
  throw "Host group '$GroupName' was not found."
}

$groupId = $groupResult[0].groupid
$from = $monthStart.ToUnixTimeSeconds()
$till = $monthEnd.ToUnixTimeSeconds()

$events = Invoke-ZabbixApi -Method "event.get" -Params @{
  output       = @("eventid", "objectid", "clock", "name", "severity", "acknowledged", "value", "r_eventid", "opdata")
  source       = 0
  object       = 0
  groupids     = @($groupId)
  severities   = $severityIds
  value        = 1
  time_from    = $from
  time_till    = $till
  selectHosts  = @("hostid", "host", "name")
  selectTags   = "extend"
  selectAlerts = @("alertid", "p_eventid", "clock", "status", "error")
  sortfield    = @("clock", "eventid")
  sortorder    = "DESC"
  limit        = 100000
} -Id 200

$recoveryIds = @(
  $events |
    Where-Object { $_.r_eventid -and $_.r_eventid -ne "0" } |
    ForEach-Object { $_.r_eventid } |
    Sort-Object -Unique
)

$recoveryById = @{}
for ($i = 0; $i -lt $recoveryIds.Count; $i += 500) {
  $end = [Math]::Min($i + 499, $recoveryIds.Count - 1)
  $chunk = @($recoveryIds[$i..$end])
  if ($chunk.Count -eq 0) { continue }

  $recoveries = Invoke-ZabbixApi -Method "event.get" -Params @{
    output   = @("eventid", "clock")
    eventids = $chunk
  } -Id (300 + [int]($i / 500))

  foreach ($recovery in @($recoveries)) {
    $recoveryById[$recovery.eventid] = $recovery
  }
}

$safeGroupName = ($GroupName -replace "[^\w.-]+", "_").Trim("_")
$safeSeverityName = (($normalizedSeverities -join "_") -replace "[^\w.-]+", "_").Trim("_")
$exportedAtLocal = [DateTimeOffset]::Now.ToOffset([TimeSpan]::FromHours(7)).ToString("yyyy-MM-ddTHH:mm:sszzz", [Globalization.CultureInfo]::InvariantCulture)
$normalizedRows = @($events) | ForEach-Object {
  $recoveryClock = $null
  if ($_.r_eventid -and $_.r_eventid -ne "0" -and $recoveryById.ContainsKey($_.r_eventid)) {
    $recoveryClock = [int64]$recoveryById[$_.r_eventid].clock
  }

  $status = if ($recoveryClock) { "RESOLVED" } else { "PROBLEM" }
  $durationUntil = if ($recoveryClock) { $recoveryClock } else { [DateTimeOffset]::Now.ToUnixTimeSeconds() }
  $hostName = if ($_.hosts -and $_.hosts.Count -gt 0) { $_.hosts[0].name } else { "" }
  $hostId = if ($_.hosts -and $_.hosts.Count -gt 0) { $_.hosts[0].hostid } else { "" }
  $tagMap = Convert-Tags @($_.tags)
  $tagsJson = $tagMap | ConvertTo-Json -Depth 20 -Compress

  [pscustomobject]@{
    event_id           = $_.eventid
    r_event_id         = $_.r_eventid
    trigger_id         = $_.objectid
    source             = "zabbix_api"
    host_group         = $GroupName
    host_group_id      = $groupId
    export_month       = $Month
    exported_at_local  = $exportedAtLocal
    severity           = $idToSeverity[[string]$_.severity]
    severity_id        = $_.severity
    status             = $status
    acknowledged       = if ($_.acknowledged -eq "1") { "true" } else { "false" }
    host               = $hostName
    host_id            = $hostId
    site_code          = Get-SiteCodeFromHost $hostName
    problem_raw        = $_.name
    problem_signature  = Normalize-ProblemSignature $_.name
    opdata             = $_.opdata
    started_at_local   = Format-IsoLocalTime $_.clock
    started_at_utc     = Format-IsoUtcTime $_.clock
    recovered_at_local = if ($recoveryClock) { Format-IsoLocalTime $recoveryClock } else { "" }
    recovered_at_utc   = if ($recoveryClock) { Format-IsoUtcTime $recoveryClock } else { "" }
    duration_seconds   = $durationUntil - [int64]$_.clock
    duration_text      = Format-Duration ($durationUntil - [int64]$_.clock)
    action_count       = @($_.alerts).Count
    domain             = Join-TagValues $tagMap "class"
    component          = Join-TagValues $tagMap "component"
    scope              = Join-TagValues $tagMap "scope"
    tags_text          = (@($_.tags) | ForEach-Object { "$($_.tag): $($_.value)" }) -join ", "
    tags_json          = $tagsJson
    evidence_label     = "SOURCE FACT"
  }
}

$normalizedFile = Join-Path $OutputDir "zbx_problems_normalized_${safeGroupName}_${safeSeverityName}_${Month}.csv"
$normalizedRows | Export-Csv -Path $normalizedFile -NoTypeInformation -Encoding UTF8

[pscustomobject]@{
  group                  = $GroupName
  groupid                = $groupId
  month                  = $Month
  severities             = ($normalizedSeverities -join ", ")
  normalized_rows        = $normalizedRows.Count
  recovery_events_joined = $recoveryById.Count
  output                 = (Resolve-Path $normalizedFile).Path
} | ConvertTo-Json -Depth 5
