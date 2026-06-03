from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timedelta, timezone
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from urllib3.util.retry import Retry


DEFAULT_ZABBIX_URL = "https://zabbix.cit.insea.io/api_jsonrpc.php"
DEFAULT_API_TOKEN = ""
DEFAULT_HOST_GROUP = "All VNM"
DEFAULT_MONTH = "2026-05"
DEFAULT_SEVERITIES = "High,Disaster"
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 1000
DEFAULT_INCLUDE_ROWS = True
DEFAULT_INCLUDE_ACTION_COUNT = False
DEFAULT_VERIFY_SSL = False
DEFAULT_TIMEOUT_SECONDS = 30
DEFAULT_RETRY_TOTAL = 3
DEFAULT_RETRY_BACKOFF_SECONDS = 0.6

SEVERITY_TO_ID = {
    "not classified": 0,
    "information": 1,
    "warning": 2,
    "average": 3,
    "high": 4,
    "disaster": 5,
}
ID_TO_SEVERITY = {str(value): key.title() for key, value in SEVERITY_TO_ID.items()}
BANGKOK_TZ = timezone(timedelta(hours=7))


class ZabbixToolError(RuntimeError):
    pass


def _to_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _session(verify_ssl: bool, retry_total: int, retry_backoff_seconds: float) -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=retry_total,
        connect=retry_total,
        read=retry_total,
        status=retry_total,
        backoff_factor=retry_backoff_seconds,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["POST"]),
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.verify = verify_ssl
    return session


def _api_call(
    session: requests.Session,
    zabbix_url: str,
    api_token: str,
    method: str,
    params: dict[str, Any],
    request_id: int,
    timeout_seconds: int,
) -> Any:
    try:
        response = session.post(
            zabbix_url,
            headers={
                "Authorization": f"Bearer {api_token}",
                "Content-Type": "application/json-rpc",
            },
            json={"jsonrpc": "2.0", "method": method, "params": params, "id": request_id},
            timeout=timeout_seconds,
        )
        response.raise_for_status()
        payload = response.json()
    except RequestException as exc:
        status_code = getattr(getattr(exc, "response", None), "status_code", None)
        status_text = f" HTTP {status_code}" if status_code else ""
        raise ZabbixToolError(
            f"Zabbix API request failed for {method}{status_text}. "
            f"The endpoint may be unavailable or overloaded; retry later, "
            f"increase retry_total, or increase timeout_seconds. Details: {exc}"
        ) from exc
    except ValueError as exc:
        raise ZabbixToolError(f"Zabbix API returned invalid JSON for {method}.") from exc

    if "error" in payload:
        raise ZabbixToolError(json.dumps(payload["error"], ensure_ascii=False))
    return payload.get("result")


def _parse_severities(severities: str | list[str]) -> list[int]:
    parts = severities.split(",") if isinstance(severities, str) else severities
    ids: list[int] = []
    for part in parts:
        key = str(part).strip().lower()
        if not key:
            continue
        if key not in SEVERITY_TO_ID:
            valid = ", ".join(sorted(name.title() for name in SEVERITY_TO_ID))
            raise ZabbixToolError(f"Unsupported severity '{part}'. Valid values: {valid}")
        ids.append(SEVERITY_TO_ID[key])
    if not ids:
        raise ZabbixToolError("At least one severity is required.")
    return ids


def _month_range(month: str) -> tuple[int, int, str, str]:
    try:
        start = datetime.strptime(month, "%Y-%m").replace(tzinfo=BANGKOK_TZ)
    except ValueError as exc:
        raise ZabbixToolError("month must use yyyy-mm format, for example 2026-05") from exc
    end = start.replace(year=start.year + 1, month=1) if start.month == 12 else start.replace(month=start.month + 1)
    return int(start.timestamp()), int(end.timestamp()), start.isoformat(timespec="seconds"), end.isoformat(timespec="seconds")


def _iso_local(clock: Any) -> str:
    if not clock or str(clock) == "0":
        return ""
    return datetime.fromtimestamp(int(clock), tz=BANGKOK_TZ).isoformat(timespec="seconds")


def _iso_utc(clock: Any) -> str:
    if not clock or str(clock) == "0":
        return ""
    return datetime.fromtimestamp(int(clock), tz=timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _duration_text(seconds: int) -> str:
    seconds = max(0, int(seconds))
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if seconds or not parts:
        parts.append(f"{seconds}s")
    return " ".join(parts)


def _site_code(host: str) -> str:
    match = re.match(r"^VNM([A-Z0-9]{3})", (host or "").upper())
    return match.group(1) if match else "UNKNOWN"


def _normalize_problem_signature(problem: str) -> str:
    text = (problem or "").lower()
    text = re.sub(r"\(current [^)]+\)", "", text)
    text = re.sub(r"current:\s*\d+(?:\.\d+)?\s*mbps", "current:<value> mbps", text)
    text = re.sub(r"\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?\s*(?:mbps|gbps|%|hz|m|s|c)\b", "<value>", text)
    return re.sub(r"\s+", " ", text).strip()


def _tag_map(tags: list[dict[str, Any]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for item in tags or []:
        key = str(item.get("tag", "")).strip()
        value = str(item.get("value", "")).strip()
        if not key or not value:
            continue
        result.setdefault(key, [])
        if value not in result[key]:
            result[key].append(value)
    return result


def _join_tag(tags: dict[str, list[str]], key: str) -> str:
    values = sorted(tags.get(key, []))
    return ",".join(values) if values else "UNKNOWN"


def _normalize_event(
    event: dict[str, Any],
    host_group: str,
    host_group_id: str,
    month: str,
    recovery_by_id: dict[str, int],
    exported_at_local: str,
) -> dict[str, Any]:
    hosts = event.get("hosts") or []
    host = hosts[0].get("name", "") if hosts else ""
    host_id = hosts[0].get("hostid", "") if hosts else ""
    started_clock = int(event["clock"])
    recovery_event_id = str(event.get("r_eventid") or "0")
    recovery_clock = recovery_by_id.get(recovery_event_id)
    duration_until = recovery_clock or int(datetime.now(tz=timezone.utc).timestamp())
    tags = event.get("tags") or []
    tags_by_key = _tag_map(tags)

    return {
        "event_id": str(event.get("eventid", "")),
        "r_event_id": recovery_event_id,
        "trigger_id": str(event.get("objectid", "")),
        "source": "zabbix_api",
        "host_group": host_group,
        "host_group_id": host_group_id,
        "export_month": month,
        "exported_at_local": exported_at_local,
        "severity": ID_TO_SEVERITY.get(str(event.get("severity")), str(event.get("severity", ""))),
        "severity_id": str(event.get("severity", "")),
        "status": "RESOLVED" if recovery_clock else "PROBLEM",
        "acknowledged": str(event.get("acknowledged")) == "1",
        "host": host,
        "host_id": str(host_id),
        "site_code": _site_code(host),
        "problem_raw": str(event.get("name", "")),
        "problem_signature": _normalize_problem_signature(str(event.get("name", ""))),
        "opdata": str(event.get("opdata", "")),
        "started_at_local": _iso_local(started_clock),
        "started_at_utc": _iso_utc(started_clock),
        "recovered_at_local": _iso_local(recovery_clock),
        "recovered_at_utc": _iso_utc(recovery_clock),
        "duration_seconds": max(0, int(duration_until) - started_clock),
        "duration_text": _duration_text(max(0, int(duration_until) - started_clock)),
        "action_count": len(event.get("alerts") or []),
        "domain": _join_tag(tags_by_key, "class"),
        "component": _join_tag(tags_by_key, "component"),
        "scope": _join_tag(tags_by_key, "scope"),
        "tags_text": ", ".join(f"{item.get('tag')}: {item.get('value')}" for item in tags),
        "tags_json": tags_by_key,
        "evidence_label": "SOURCE FACT",
    }


def _main_impl(
    zabbix_url: str | dict[str, Any] = DEFAULT_ZABBIX_URL,
    api_token: str = DEFAULT_API_TOKEN,
    host_group: str = DEFAULT_HOST_GROUP,
    month: str = DEFAULT_MONTH,
    severities: str = DEFAULT_SEVERITIES,
    page: int = DEFAULT_PAGE,
    page_size: int = DEFAULT_PAGE_SIZE,
    include_rows: bool = DEFAULT_INCLUDE_ROWS,
    include_action_count: bool = DEFAULT_INCLUDE_ACTION_COUNT,
    verify_ssl: bool = DEFAULT_VERIFY_SSL,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
    retry_total: int = DEFAULT_RETRY_TOTAL,
    retry_backoff_seconds: float = DEFAULT_RETRY_BACKOFF_SECONDS,
    payload: dict[str, Any] | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    raw_payload: dict[str, Any] = {}
    if isinstance(zabbix_url, dict):
        raw_payload.update(zabbix_url)
        zabbix_url = DEFAULT_ZABBIX_URL
    if isinstance(payload, dict):
        raw_payload.update(payload)
    for wrapper_name in ["input", "inputs", "params", "arguments", "root", "body", "request"]:
        wrapped = kwargs.get(wrapper_name)
        if isinstance(wrapped, dict):
            raw_payload.update(wrapped)
    raw_payload.update({key: value for key, value in kwargs.items() if value is not None})

    zabbix_url = str(raw_payload.get("zabbix_url") or zabbix_url)
    api_token = str(raw_payload.get("api_token") or raw_payload.get("zabbix_token") or raw_payload.get("token") or api_token or "")
    host_group = str(raw_payload.get("host_group") or raw_payload.get("group_name") or host_group)
    month = str(raw_payload.get("month") or month)
    severities = raw_payload.get("severities") or severities
    page = int(raw_payload.get("page", page))
    page_size = int(raw_payload.get("page_size", page_size))
    include_rows = _to_bool(raw_payload.get("include_rows", include_rows))
    include_action_count = _to_bool(raw_payload.get("include_action_count", include_action_count))
    verify_ssl = _to_bool(raw_payload.get("verify_ssl", verify_ssl))
    timeout_seconds = int(raw_payload.get("timeout_seconds", timeout_seconds))
    retry_total = int(raw_payload.get("retry_total", retry_total))
    retry_backoff_seconds = float(raw_payload.get("retry_backoff_seconds", retry_backoff_seconds))

    token = api_token or os.getenv("ZABBIX_TOKEN", "") or DEFAULT_API_TOKEN
    if not token:
        raise ZabbixToolError("Missing api_token. Pass it as a secret parameter.")
    if page < 1:
        raise ZabbixToolError("page must be >= 1")
    if page_size < 0:
        raise ZabbixToolError("page_size must be >= 0")

    severity_ids = _parse_severities(severities)
    time_from, time_till, period_start, period_end = _month_range(month)
    session = _session(verify_ssl, retry_total, retry_backoff_seconds)
    if not verify_ssl:
        requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]

    groups = _api_call(session, zabbix_url, token, "hostgroup.get", {"output": ["groupid", "name"], "filter": {"name": [host_group]}}, 100, timeout_seconds)
    if not groups:
        raise ZabbixToolError(f"Host group '{host_group}' was not found.")
    group_id = str(groups[0]["groupid"])

    event_params: dict[str, Any] = {
        "output": ["eventid", "objectid", "clock", "name", "severity", "acknowledged", "value", "r_eventid", "opdata"],
        "source": 0,
        "object": 0,
        "groupids": [group_id],
        "severities": severity_ids,
        "value": 1,
        "time_from": time_from,
        "time_till": time_till,
        "selectHosts": ["hostid", "host", "name"],
        "selectTags": "extend",
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC",
        "limit": 100000,
    }
    if include_action_count:
        event_params["selectAlerts"] = ["alertid", "p_eventid", "clock", "status", "error"]

    events = _api_call(session, zabbix_url, token, "event.get", event_params, 200, timeout_seconds) or []
    recovery_ids = sorted({str(event.get("r_eventid") or "0") for event in events if str(event.get("r_eventid") or "0") != "0"})
    recovery_by_id: dict[str, int] = {}
    for index in range(0, len(recovery_ids), 2000):
        chunk = recovery_ids[index : index + 2000]
        recoveries = _api_call(session, zabbix_url, token, "event.get", {"output": ["eventid", "clock"], "eventids": chunk}, 300 + index // 2000, timeout_seconds)
        for recovery in recoveries or []:
            recovery_by_id[str(recovery["eventid"])] = int(recovery["clock"])

    exported_at_local = datetime.now(tz=BANGKOK_TZ).isoformat(timespec="seconds")
    rows = [_normalize_event(event, host_group, group_id, month, recovery_by_id, exported_at_local) for event in events]
    total_rows = len(rows)
    start_index = (page - 1) * page_size if page_size else 0
    end_index = start_index + page_size if page_size else total_rows
    paged_rows = rows[start_index:end_index] if include_rows else []

    return {
        "ok": True,
        "summary": {
            "zabbix_url": zabbix_url,
            "host_group": host_group,
            "host_group_id": group_id,
            "month": month,
            "period_start_local": period_start,
            "period_end_local": period_end,
            "severities": severities,
            "total_rows": total_rows,
            "resolved_rows": sum(1 for row in rows if row["status"] == "RESOLVED"),
            "problem_rows": sum(1 for row in rows if row["status"] == "PROBLEM"),
            "recovery_events_joined": len(recovery_by_id),
            "page": page,
            "page_size": page_size,
            "returned_rows": len(paged_rows),
            "truncated": include_rows and end_index < total_rows,
            "next_page": page + 1 if include_rows and end_index < total_rows else None,
            "include_action_count": include_action_count,
            "verify_ssl": verify_ssl,
            "retry_total": retry_total,
            "retry_backoff_seconds": retry_backoff_seconds,
        },
        "rows": paged_rows,
    }


def main(**kwargs: Any) -> dict[str, Any]:
    try:
        return _main_impl(**kwargs)
    except ZabbixToolError as exc:
        return {"ok": False, "error": "zabbix_tool_error", "error_message": str(exc), "rows": []}


def _cli() -> int:
    parser = argparse.ArgumentParser(description="Pull normalized Zabbix problem events.")
    parser.add_argument("--zabbix-url", default=DEFAULT_ZABBIX_URL)
    parser.add_argument("--api-token", default=os.getenv("ZABBIX_TOKEN", "") or DEFAULT_API_TOKEN)
    parser.add_argument("--host-group", default=DEFAULT_HOST_GROUP)
    parser.add_argument("--month", default=DEFAULT_MONTH)
    parser.add_argument("--severities", default=DEFAULT_SEVERITIES)
    parser.add_argument("--page", type=int, default=DEFAULT_PAGE)
    parser.add_argument("--page-size", type=int, default=DEFAULT_PAGE_SIZE)
    parser.add_argument("--no-rows", action="store_true")
    parser.add_argument("--include-action-count", action="store_true")
    parser.add_argument("--verify-ssl", action="store_true")
    parser.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--retry-total", type=int, default=DEFAULT_RETRY_TOTAL)
    parser.add_argument("--retry-backoff-seconds", type=float, default=DEFAULT_RETRY_BACKOFF_SECONDS)
    args = parser.parse_args()
    result = _main_impl(
        zabbix_url=args.zabbix_url,
        api_token=args.api_token,
        host_group=args.host_group,
        month=args.month,
        severities=args.severities,
        page=args.page,
        page_size=args.page_size,
        include_rows=not args.no_rows,
        include_action_count=args.include_action_count,
        verify_ssl=args.verify_ssl,
        timeout_seconds=args.timeout_seconds,
        retry_total=args.retry_total,
        retry_backoff_seconds=args.retry_backoff_seconds,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
