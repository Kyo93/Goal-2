# Clean Rawdata - Zabbix on Alpha

This folder contains the Alpha-specific script and build notes for the `Clean Rawdata - Zabbix` workflow.

Use this folder when manually building the workflow in Alpha Intelligence. Do not use files in `scripts/` for Alpha Code Executor nodes; `scripts/` is for local/VPN Zabbix API pull only.

## Decision

Split the workflow into separate nodes. For Zabbix, Google Drive can be the
direct Alpha input, including a folder containing many daily CSV files. The key
rule is that the Python processor should receive CSV file content, not a raw
Google Drive folder URL.

Recommended production flow:

```text
Start with Google Drive folder_id
  -> Google Drive / Drive API list files node
  -> Filter CSV files by date/name
  -> Download selected CSV files
  -> Code Executor node: normalize one or many CSV bodies
  -> Merge / Aggregate node, only if processing each file in a separate loop
  -> Upload AK Knowledge, if generating a Knowledge file
  -> Validation / Result node
```

Quick test flow for one bundled CSV:

```text
Start
  -> Google Drive direct download / HTTP Request node
  -> Code Executor node: alpha-zabbix-processor-node-lite.py
  -> Upload AK Knowledge
  -> Validation / Result node
```

Reason:

- Alpha Code Executor is intended for lightweight variable manipulation and deterministic processing.
- Alpha official Code Executor documentation recommends using the provided HTTP Request node instead of implementing HTTP calls inside Code Executor.
- Code Executor has a short execution limit, so listing a folder and downloading many files inside the same node is fragile.
- Separating file read/download from processing makes failures easier to debug:
  - folder/list/share-link issue = Google Drive or HTTP node failure
  - per-file download issue = download node failure
  - bad CSV/header/data issue = Code Executor failure

Official Alpha references:

- Code Executor: https://ai.insea.io/guide/code-executor
- Workflow API Integration: https://ai.insea.io/guide/workflow-api-integration

## Current Status: Alpha Flow Completed

The Zabbix flow is completed on Alpha Intelligent for the bundled May-to-June
impact-only export.

Completed flow:

```text
Start
  -> Google Drive / Download CSV from Folder
  -> Code Executor: alpha-zabbix-processor-node-lite.py
  -> Upload AK Knowledge
  -> End / Result
```

The final Knowledge file must be:

```text
04_alert_patterns.md
```

The Code Executor returns a file-like output named `knowledge_file`. Use that
file output for Knowledge upload instead of uploading the raw `markdown` string.
The returned object has `knowledge_filename = 04_alert_patterns.md`.

Verified final Alpha output:

```text
input_rows = 5199
record_count = 5199
alert_pattern_count = 365
alert_pattern_headings = 365
site_family_sections = 50
rejected_row_count = 0
duplicate_rows = 0
reconciliation_passed = true
upload_ready = true
validation_status = PASS
```

The generated markdown is structured for local-package-style Knowledge:

```text
# Raw Zabbix Alert Patterns
> Alert pattern is not a confirmed incident.

metadata yaml block
## Site Pattern Family Summary
## Alert Pattern ALP-...
```

The `Site Pattern Family Summary` section is the first reading layer for
SuperAgent/Knowledge answers. Individual alert pattern blocks are supporting
evidence and should not be treated as confirmed incidents.

## Google Drive Folder Input Rule

Google Drive can be the direct input source for Alpha.

For Zabbix, this is expected because Zabbix data may be exported daily and stored
as many source files in one Drive folder.

However, do not pass a Google Drive folder URL directly into the Python processor.
The folder URL should be handled by a Drive list-files node or a Drive API/HTTP
node first.

Folder URL example:

```text
https://drive.google.com/drive/folders/<FOLDER_ID>?usp=drive_link
```

This folder URL is useful as the workflow input, but it is not a CSV file. Alpha
must first list the files inside the folder and select the CSV files to process.

Expected machine flow:

```text
folder_id
  -> list files in folder
  -> selected file_id[]
  -> download each file_id
  -> process each CSV body
```

Use either:

```text
folder_id
```

or:

```text
folder_url -> extract folder_id -> list files
```

For each CSV file inside the folder, use its file link or file ID.

File preview URL example:

```text
https://drive.google.com/file/d/<FILE_ID>/view?usp=drive_link
```

Direct download URL for one file:

```text
https://drive.google.com/uc?export=download&id=<FILE_ID>
```

The folder and files must be shared so Alpha can read them. For a public-link
test:

```text
Anyone with the link can view
```

If using an authenticated Google Drive connector in Alpha, prefer connector
authentication over public sharing.

If a file is not readable by Alpha, Google Drive may return an HTML login page.
The processor detects this and returns:

```text
HTTP body looks like HTML/login page; expected CSV export
```

## Multi-file Strategy

Zabbix is not like the ISP incident report. It can produce many daily source
files, and those files should remain traceable.

Use one of these strategies.

### Strategy A: Folder input with loop, recommended for production

Input:

```json
{
  "zabbix_folder_id": "<GOOGLE_DRIVE_FOLDER_ID>",
  "from_date": "2026-05-01",
  "to_date": "2026-06-06"
}
```

Flow:

```text
Start
  -> List Google Drive folder files
  -> Filter files:
       mime/type or extension = .csv
       name/date inside requested range
  -> Download selected CSV files
  -> Normalize with Code Executor
       small batch: pass zabbix_export_bodies[] into one node
       large batch: loop one file per node, then merge
  -> Validate merged result
  -> Result
```

Use this when daily files are the long-term operating model.

### Strategy B: Bundle file, recommended for first Alpha validation

Input:

```json
{
  "zabbix_file_id": "<GOOGLE_DRIVE_FILE_ID_OF_COMBINED_CSV>"
}
```

Flow:

```text
Start
  -> Download one bundled CSV
  -> Generate alert-pattern Knowledge file with Code Executor
  -> Upload AK Knowledge
  -> Validate
  -> Result
```

Use this to finish task 3.3 quickly and prove the processor works.

### Strategy C: Manifest file

Input:

```json
{
  "zabbix_manifest_file_id": "<GOOGLE_DRIVE_FILE_ID_OF_MANIFEST_CSV>"
}
```

Manifest columns:

```csv
source_date,file_name,file_id,source_label,period_start,period_end,expected_rows,sha256,created_at
```

Flow:

```text
Start
  -> Download manifest CSV
  -> Parse manifest
  -> Loop manifest rows
       -> Download file_id
       -> Normalize one CSV
  -> Merge normalized outputs
  -> Validate against manifest expected_rows
  -> Result
```

Use this when Drive folder listing is hard to configure or when you want a stable
audit list of source files.

## Workflow Build

Build the workflow in two stages:

1. First validate with a single bundled CSV.
2. Then switch the input layer to a Google Drive folder and process many daily CSV files.

The completed Alpha Knowledge upload uses the lite processor:

```text
alpha-zabbix-processor-node-lite.py
```

The full processor and merge node remain available for future workflows that
need full normalized Zabbix row records. For the current Knowledge/SuperAgent
flow, prefer the lite processor because it emits compact alert patterns and the
ready-to-upload markdown file.

## Workflow Build: Folder Multi-file Mode

Use this for the real Zabbix operating model.

### Node 1: Start

Name:

```text
Start
```

Input fields:

```json
{
  "zabbix_folder_id": "string",
  "from_date": "string",
  "to_date": "string",
  "file_name_prefix": "string"
}
```

Example test input:

```json
{
  "zabbix_folder_id": "<GOOGLE_DRIVE_FOLDER_ID>",
  "from_date": "2026-05-01",
  "to_date": "2026-06-06",
  "file_name_prefix": "zbx_problems_impact"
}
```

If Alpha only gives you a folder URL from the UI, extract the folder ID from:

```text
https://drive.google.com/drive/folders/<FOLDER_ID>?usp=drive_link
```

### Node 2: List Drive Folder Files

Node type:

```text
Google Drive connector / Drive API / HTTP Request
```

Goal:

```text
Return files inside zabbix_folder_id.
```

Required output per file:

```json
{
  "file_id": "string",
  "file_name": "string",
  "mime_type": "string",
  "modified_time": "string"
}
```

If using Google Drive API directly, the conceptual request is:

```text
List files where parent = zabbix_folder_id and trashed = false
```

### Node 3: Filter Zabbix CSV Files

Node type:

```text
Code Executor / Filter / Condition
```

Rules:

```text
file_name ends with .csv
file_name starts with file_name_prefix, if prefix is supplied
file date is inside from_date/to_date, if date is encoded in file_name
```

Expected output:

```json
{
  "selected_files": [
    {
      "file_id": "...",
      "file_name": "zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05-01.csv"
    }
  ],
  "selected_file_count": 1
}
```

### Node 4: Loop Selected Files

Node type:

```text
Loop / For each
```

Loop input:

```text
selected_files
```

For each file, run Node 5. Then choose one execution mode:

```text
Small batch / first test:
  collect body[] and file_name[]
  -> run Node 6 once with zabbix_export_bodies + source_labels

Large batch / timeout-safe production:
  run Node 6 once per file
  -> run Node 7 merge
```

### Node 5: Download One Zabbix CSV

Node type:

```text
Google Drive download file / HTTP Request
```

Input:

```text
current_file.file_id
```

If using direct download URL:

```text
https://drive.google.com/uc?export=download&id={{current_file.file_id}}
```

Expected output mapping:

```text
body -> zabbix_export_body
current_file.file_name -> source_label
```

For multi-body mode, collect all loop outputs as arrays:

```text
body[] -> zabbix_export_bodies
current_file.file_name[] -> source_labels
```

### Node 6: Normalize Zabbix CSV Body/Bodies

Node type:

```text
Code Executor
```

Language:

```text
Python 3
```

Code:

```text
Copy all code from alpha-zabbix-processor-node.py in this folder.
```

Input variables:

```text
Single-file mode:
  zabbix_export_body

Multi-file mode:
  zabbix_export_bodies
  source_labels
```

Optional input variables:

```text
zabbix_export_file
zabbix_export_files
zabbix_sources
```

Input examples:

```json
{
  "zabbix_export_bodies": ["<csv body 1>", "<csv body 2>"],
  "source_labels": ["zabbix_2026-05-01.csv", "zabbix_2026-05-02.csv"]
}
```

`zabbix_sources` may also be a list of objects when Alpha keeps file metadata
and body together:

```json
[
  {
    "name": "zabbix_2026-05-01.csv",
    "body": "<csv body>"
  }
]
```

Output variables:

```text
json_text
alert_patterns_text
json_result
alert_patterns_result
markdown
summary
```

Each loop iteration should also preserve:

```text
source_file_id
source_file_name
```

If Node 6 receives `zabbix_export_bodies`, it already returns one merged output.
In that case, skip Node 7.

### Node 7: Merge Daily Zabbix Outputs

Node type:

```text
Code Executor / Aggregator
```

Purpose:

```text
Merge all per-file json_result.records into one normalized alert collection,
dedupe by alert_id or event_id, then regroup alert patterns globally.
```

Code:

```text
Copy all code from alpha-zabbix-merge-node.py in this folder.
```

Input variables:

```text
zabbix_json_results
zabbix_json_texts
source_files
```

Use either `zabbix_json_results` or `zabbix_json_texts` depending on what the
Alpha loop node can pass forward.

Use Node 7 only when Node 6 ran separately per file. Do not use Node 7 when
Node 6 already received `zabbix_export_bodies` and returned `source_type:
zabbix_multi_source`.

Output variables:

```text
json_text
alert_patterns_text
json_result
alert_patterns_result
markdown
summary
```

Important:

```text
Do not simply concatenate alert_patterns_result.records from daily files.
The same host/problem pattern may appear across multiple days, so final pattern
grouping must happen after all alert records are merged.
```

If Alpha does not support loop aggregation cleanly yet, use the single bundled CSV mode first.

### Node 8: Validate Merged Zabbix Output

Validation rules:

```text
ok == true
source_file_count > 0
record_count > 0
alert_pattern_count > 0
rejected_row_count == 0
duplicate_rows >= 0
reconciliation_passed == true
upload_ready == true
```

### Node 9: Result

Return:

```json
{
  "ok": true,
  "source_file_count": "{{source_file_count}}",
  "summary": "{{summary}}",
  "zabbix_alerts_json": "{{json_text}}",
  "alert_patterns_json": "{{alert_patterns_text}}",
  "zabbix_markdown": "{{markdown}}"
}
```

## Workflow Build: Single Bundle Test Mode

Use this to finish 3.3 quickly before enabling folder multi-file mode.

### Node 1B: Start

Input fields:

```json
{
  "zabbix_file_id": "string",
  "source_label": "string"
}
```

Example input:

```json
{
  "zabbix_file_id": "<GOOGLE_DRIVE_FILE_ID>",
  "source_label": "zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv"
}
```

### Node 2B: Build Download URL

Use this node only if Start receives `zabbix_file_id`.

Node type:

```text
Template / Set variable / Code Executor
```

Output:

```json
{
  "download_url": "https://drive.google.com/uc?export=download&id={{zabbix_file_id}}"
}
```

If Alpha has a built-in expression field, no code is needed; build the URL directly in the HTTP Request node.

### Node 3B: Download Zabbix CSV

Node type:

```text
HTTP Request
```

Method:

```text
GET
```

URL:

```text
{{download_url}}
```

Expected output mapping:

```text
body -> zabbix_export_body
```

Recommended checks:

- HTTP status is `200`.
- Response body is not empty.
- Response body starts with the CSV header, for example:

```text
event_id,r_event_id,trigger_id,...
```

If the response starts with:

```text
<!doctype html
<html
```

then the Drive sharing/link is wrong.

### Node 4B: Normalize Zabbix

Node type:

```text
Code Executor
```

Language:

```text
Python 3
```

Code:

```text
Copy all code from alpha-zabbix-processor-node-lite.py in this folder.
```

Input variables:

```text
zabbix_export_body
```

Optional input variables:

```text
zabbix_export_file
source_label
max_patterns
return_markdown
```

For the Google Drive flow, prefer:

```text
One file:
  zabbix_export_body = HTTP Request / body
  source_label = HTTP Request / file_name, if available

One downloaded file object:
  zabbix_export_file = Google Drive Download / file
  source_label = Google Drive Download / file_name
```

The lite script supports one downloaded CSV body or one CSV file object. It is
the simplest path for the completed bundled Knowledge flow.

Output variables:

```text
json_text
alert_patterns_text
json_result
alert_patterns_result
markdown
knowledge_file
knowledge_filename
package_section
summary
```

Expected successful `summary` for the latest May-to-June impact-only file:

```json
{
  "ok": true,
  "source_type": "zabbix_csv",
  "input_rows": 5199,
  "record_count": 5199,
  "alert_pattern_count": 365,
  "rejected_row_count": 0,
  "duplicate_rows": 0,
  "reconciliation_passed": true,
  "upload_ready": true,
  "is_normalized_input": true
}
```

Expected file outputs:

```text
knowledge_file = file-like object
knowledge_file.name = 04_alert_patterns.md
knowledge_filename = 04_alert_patterns.md
package_section = 04_alert_patterns
```

Expected markdown sections:

```text
# Raw Zabbix Alert Patterns
## Site Pattern Family Summary
## Alert Pattern ALP-...
```

### Node 5B: Validate Zabbix Output

Node type:

```text
Condition / Code Executor / Result validation
```

Validation rules:

```text
summary.ok == true
summary.record_count > 0
summary.alert_pattern_count > 0
summary.rejected_row_count == 0
summary.reconciliation_passed == true
summary.upload_ready == true
knowledge_file exists
knowledge_filename == "04_alert_patterns.md"
```

Validate one sample alert pattern contains:

```text
record_type
alert_pattern_id
host
site_code
first_seen_at
last_seen_at
last_recovered_at
alert_count
problem_signature
pattern_family
investigation_priority
signal_assessment
why_it_matters
evidence_label
source_refs
```

Important invariant:

```text
No Zabbix-only record may be labeled as CONFIRMED_INCIDENT.
```

Expected Zabbix record type:

```text
ZABBIX_ALERT_PATTERN
```

Expected assessment text:

```text
RAW ALERT PATTERN - NOT A CONFIRMED INCIDENT
```

### Node 6B: Upload AK Knowledge

Node type:

```text
Upload AK Knowledge
```

Input mapping:

```text
expert_id = <target SuperAgent / AK expert id>
file = Normalize Zabbix / knowledge_file
citation_title = Normalize Zabbix / knowledge_filename
format = markdown
knowledge_id = optional; leave blank to create, set when replacing an existing Knowledge file
```

Important:

```text
Use `knowledge_file`, not the raw `markdown` string.
Use `knowledge_filename` as the citation title so Alpha preserves 04_alert_patterns.md.
```

Expected upload artifact:

```text
04_alert_patterns.md
```

### Node 7B: Result

Return:

```json
{
  "ok": "{{summary.ok}}",
  "summary": "{{summary}}",
  "knowledge_filename": "{{knowledge_filename}}",
  "package_section": "{{package_section}}",
  "upload_ready": "{{summary.upload_ready}}"
}
```

Optional debugging outputs:

```text
markdown
json_text
alert_patterns_text
```

Human-friendly labels:

```text
Processing summary
Knowledge filename
Knowledge package section
Upload readiness
```

## Alpha Test Case

Use the file:

```text
zbx_problems_impact_All_VNM_Average_High_Disaster_2026-05_to_2026-06.csv
```

Expected processor-level result:

```text
input_rows = 5199
record_count = 5199
alert_pattern_count = 365
rejected_row_count = 0
duplicate_rows = 0
reconciliation_passed = true
upload_ready = true
```

Expected generated Knowledge file:

```text
filename = 04_alert_patterns.md
extension = .md
alert_pattern_headings = 365
site_family_sections = 50
validation_status = PASS
```

Required markdown markers:

```text
# Raw Zabbix Alert Patterns
## Site Pattern Family Summary
package_section: 04_alert_patterns
knowledge_filename: 04_alert_patterns.md
```

Expected CPL family counts in the combined file:

```text
HTTP monitoring: 21 patterns / 1167 alerts
Network reachability: 25 patterns / 29 alerts
Zabbix agent/active check: 2 patterns / 5 alerts
Host restart/uptime: 2 patterns / 4 alerts
```

Note: These CPL counts are for the combined May-to-June file, not only May.

## Troubleshooting

### HTML/login page detected

Cause:

```text
Google Drive file is not shared correctly, or the workflow used a folder/preview URL.
```

Fix:

```text
Use direct file URL:
https://drive.google.com/uc?export=download&id=<FILE_ID>
```

### Missing required columns

Cause:

```text
The uploaded file is not the normalized Zabbix CSV or has a changed header.
```

Fix:

```text
Use the CSV exported by scripts/zabbix_data_pull_tool.py with --impact-only.
```

### Code Executor timeout

Cause:

```text
The file is too large or the node is also trying to download the file.
The Code Executor may also be killed while serializing large outputs, even when
CSV parsing already completed.
```

Fix:

```text
Keep HTTP download in a separate node.
Keep Code Executor only for parsing/grouping.
If needed, process one month per workflow run instead of a multi-month combined file.
```

If the normal processor still times out, use the lite processor:

```text
04-Alpha workflow scripts/clean-rawdata-zabbix/alpha-zabbix-processor-node-lite.py
```

Lite processor behavior:

```text
Reads CSV rows incrementally.
Does not keep normalized records in output.
Aggregates alert patterns while reading rows.
Returns summary + markdown + compact pattern collection + knowledge_file.
Sets knowledge_file.name to 04_alert_patterns.md.
```

First lite test input:

```text
zabbix_export_file = Download CSV from Folder / file
source_label = Download CSV from Folder / file_name
return_markdown = false
```

First lite test End output:

```text
summary only
```

Expected summary:

```text
record_count = 5199
alert_pattern_count = 365
rejected_row_count = 0
upload_ready = true
```

After summary passes, set:

```text
return_markdown = true
```

Then map these fields into Upload AK Knowledge:

```text
file = knowledge_file
citation_title = knowledge_filename
format = markdown
```

Do not expose `json_text` or `alert_patterns_text` in the End node unless
debugging.

If Alpha downloads a generated file as `.txt`, check whether the Upload AK
Knowledge node is receiving the raw `markdown` string. The successful flow
uploads the file-like `knowledge_file`, whose name is `04_alert_patterns.md`.

### Output too large

Cause:

```text
json_text and alert_patterns_text are large for multi-month data.
```

Fix:

```text
For validation, return summary first.
For Knowledge upload, pass knowledge_file internally.
For connector workflow, pass object outputs internally.
If Alpha UI becomes slow, split by month.
```
