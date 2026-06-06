# Alpha IT Operations Workflow Architecture

## Muc tieu

Tai lieu nay mo ta kien truc de dua qua trinh xu ly ISP Incident Report, Zabbix Alert va ITcenter Ticket len Alpha Intelligent.

Muc tieu chinh:

- Chuan hoa 3 raw source thanh du lieu sach.
- Ket noi 3 source de tao operational timeline.
- Cho SuperAgent tra loi dung cac cau hoi theo site va khoang thoi gian.
- Khong de SuperAgent tu dem, tu group, hoac tu suy luan tu cac fragment Knowledge/RAG.
- Build thu cong tren Alpha; khong can Alpha connect toi repo/project nay bang API.

Cong thuc kien truc:

```text
Processing workflows = lam sach du lieu
Query workflow = tinh toan dung theo filter
Knowledge Markdown = ngu canh va rule dien giai
SuperAgent = viet cau tra loi cho nguoi doc
```

Hay nho ngan gon:

```text
Tool tinh dung
Knowledge hieu dung
SuperAgent noi dung
```

## Che do build da chot

```text
Repo nay = blueprint + processor code + local verification baseline.
Alpha = noi build workflow thu cong bang Code Executor/workflow nodes.
Khong can API integration tu Alpha ve repo nay.
```

He qua thuc te:

- Copy code tu `docs/alpha-incident-processor-node.py` vao Alpha Code Executor cho ISP.
- Copy code tu `docs/alpha-zabbix-processor-node.py` vao Alpha Code Executor cho Zabbix.
- Workflow connector/query duoc tao truc tiep tren Alpha bang cac node va contract trong tai lieu nay.
- Local scripts trong repo chi dung de test baseline, build thu, hoac tao file raw/processed mau.

## Tong quan kien truc

```text
Raw ISP Incident Report
  -> Workflow 1: Clean Rawdata - ISP
  -> confirmed_incidents.json / confirmed_incidents.md

Zabbix export file pulled outside Alpha
  -> Workflow 2: Clean Rawdata - Zabbix
  -> zabbix_alerts.json / alert_patterns.json / alert_patterns.md

Raw ITcenter Ticket
  -> Workflow 3: Clean Rawdata - ITcenter
  -> ticket_evidence.json / ticket_evidence.md

confirmed_incidents.json
zabbix_alerts.json
alert_patterns.json
ticket_evidence.json
  -> Workflow 4: Connect IT Ops Sources
  -> operational_timeline.json
  -> Markdown Knowledge Package

User question
  -> SuperAgent
  -> Workflow 5: Query IT Ops Timeline
  -> query_result JSON
  -> SuperAgent writes management-ready answer
```

## Phan tach workflow

### 1. Processing workflows

Processing workflow dung de nhan raw data va chuan hoa thanh record sach.

Khong nen dung processing workflow de tra loi truc tiep cau hoi cua user.

Co 3 workflow nho:

| Workflow | Input | Output chinh | Vai tro |
|---|---|---|---|
| Clean Rawdata - ISP | Google Sheet, CSV, XLSX incident report | `confirmed_incidents.json`, `confirmed_incidents.md` | Xac dinh confirmed incident |
| Clean Rawdata - Zabbix | Uploaded Zabbix CSV/XLSX export | `zabbix_alerts.json`, `alert_patterns.json`, `alert_patterns.md` | Chuan hoa raw alerts va group pattern |
| Clean Rawdata - ITcenter | Ticket export | `ticket_evidence.json`, `ticket_evidence.md` | Chuan hoa ticket/user evidence |

Input cua cac workflow nay la raw file hoac raw body.

Luu y rieng voi Zabbix:

```text
Alpha khong connect truc tiep den Zabbix noi bo.
Zabbix API pull phai chay ben ngoai Alpha tren may/co network truy cap duoc Zabbix.
Ket qua pull la normalized CSV/XLSX file.
File nay duoc upload vao Alpha de workflow Clean Rawdata - Zabbix process tiep.
Alpha cung khong can connect toi repo nay bang API; processor code duoc copy vao Code Executor node.
```

Local/VPN pull command mau:

```powershell
$env:ZABBIX_TOKEN = "<token>"
python scripts\zabbix_data_pull_tool.py `
  --month 2026-05 `
  --host-group "All VNM" `
  --severities "Average,High,Disaster" `
  --impact-only `
  --output-csv 02-Output\zabbix_exports\zbx_problems_impact_All_VNM_2026-05.csv
```

Sau do upload file CSV nay vao Alpha workflow `Clean Rawdata - Zabbix`.

Vi du workflow ISP:

```json
{
  "incident_report_body": "<csv body from Google Sheet>"
}
```

Output workflow ISP:

```json
{
  "ok": true,
  "record_count": 54,
  "records": [
    {
      "record_type": "CONFIRMED_INCIDENT",
      "incident_id": "INC-54",
      "site_code": "MBD",
      "started_at": "2026-05-31T13:10:00",
      "resolved_at": "2026-05-31T14:00:00",
      "incident_type": "Fiber optic cable failure",
      "resolution_status": "RESOLVED",
      "evidence_label": "SOURCE FACT",
      "source_ref": "google_sheet_csv:row-54"
    }
  ]
}
```

### 2. Connector workflow

Connector workflow nhan cac output da chuan hoa tu 3 workflow tren va tao timeline hop nhat.

Input:

```json
{
  "confirmed_incidents": [],
  "zabbix_alerts": [],
  "alert_patterns": [],
  "ticket_evidence": []
}
```

Output:

```text
operational_timeline.json
00_report_context.md
01_executive_summary.md
02_operational_timeline.md
02_confirmed_incidents.md
03_ticket_evidence.md
04_alert_patterns.md
...
```

Vai tro:

- Noi ISP incident, ticket va Zabbix theo site/time window.
- Phan loai evidence coverage.
- Tach monitoring signal khoi confirmed incident.
- Tao Markdown de upload Knowledge.
- Tao `operational_timeline.json` de query chinh xac.

### 3. Query workflow

Day la workflow quan trong nhat de SuperAgent tra loi dung cau hoi theo thoi gian.

Workflow nay nhan input:

```json
{
  "site_code": "CPL",
  "from_at": "2026-05-01T00:00:00",
  "to_at": "2026-06-01T00:00:00",
  "source_scope": "zabbix"
}
```

`source_scope` co the la:

```text
all
incident
ticket
zabbix
```

Output nen la JSON ngan, da filter va group san:

```json
{
  "ok": true,
  "site_code": "CPL",
  "from_at": "2026-05-01T00:00:00",
  "to_at": "2026-06-01T00:00:00",
  "source_scope": "zabbix",
  "matched_event_count": 37,
  "counts_by_episode_type": {
    "MONITORING_SIGNAL": 37
  },
  "monitoring_family_summary": [
    {
      "pattern_family": "Network reachability",
      "pattern_count": 12,
      "query_alert_count": 16,
      "investigation_priority": "HIGH",
      "why_it_matters": "May indicate network path loss, device down, or reachability instability."
    },
    {
      "pattern_family": "HTTP monitoring",
      "pattern_count": 21,
      "query_alert_count": 987,
      "investigation_priority": "MEDIUM/LOW",
      "why_it_matters": "Often indicates probe timeout or threshold sensitivity unless supported by incident/ticket evidence."
    },
    {
      "pattern_family": "Host restart/uptime",
      "pattern_count": 2,
      "query_alert_count": 2,
      "investigation_priority": "LOW"
    },
    {
      "pattern_family": "Zabbix agent/active check",
      "pattern_count": 2,
      "query_alert_count": 2,
      "investigation_priority": "LOW"
    }
  ],
  "confirmed_incidents": [],
  "related_tickets": [],
  "answer_contract": {
    "do_not_infer_user_impact": true,
    "do_not_describe_zabbix_as_confirmed_incident": true,
    "use_family_summary_first": true
  }
}
```

SuperAgent se dung JSON nay de viet cau tra loi.

## Khi nao dung Knowledge va khi nao dung Query workflow

### Dung Query workflow khi user hoi theo filter

Bat buoc dung Query workflow neu cau hoi co mot trong cac pattern sau:

```text
Trong khoang thoi gian A den B, site C co gi xay ra?
Site C trong thang 5 co alert gi?
Tu ngay A den ngay B co bao nhieu incident?
Alert Zabbix nao xay ra tai site C?
Co ticket nao trung voi incident nay khong?
```

Ly do:

- Can filter theo timestamp.
- Can count chinh xac.
- Can group pattern theo logic deterministic.
- RAG co the retrieve thieu fragment, dan den moi lan hoi tra loi khac nhau.

### Dung Knowledge khi can ngu canh

Knowledge Markdown van can upload va van duoc dung.

Dung Knowledge de:

- Doc rule va dinh nghia trong `00_report_context.md`.
- Doc cau truc timeline trong `02_operational_timeline.md`.
- Doc pattern family summary trong `04_alert_patterns.md`.
- Lay source reference va record ID.
- Giai thich SOURCE FACT, COMPUTED FACT, POTENTIAL_IMPACT, NO_DIRECT_EVIDENCE.
- Lam fallback neu tool khong kha dung.

Khong dung Knowledge de:

- Tu dem exact count theo thang/ngay.
- Tu group alert pattern.
- Tu quyet dinh mot Zabbix alert la confirmed incident.
- Tu ket luan user impact neu khong co ticket/incident evidence.

## Cac file upload len Alpha Knowledge

Upload cac file Markdown:

```text
00_report_context.md
01_executive_summary.md
02_operational_timeline.md
02_confirmed_incidents.md
03_ticket_evidence.md
04_alert_patterns.md
05_site_summary.md
06_validation_and_data_quality.md
```

Khong can upload:

```text
operational_timeline.json
confirmed_incidents.json
zabbix_alerts.json
alert_patterns.json
ticket_evidence.json
```

Ly do:

- Alpha Knowledge khong nhan `.json` hoac khong index JSON on dinh.
- JSON la data cho workflow/tool doc va query.
- Markdown la tai lieu cho SuperAgent doc va giai thich.

## Data contract toi thieu

### Confirmed incident record

```json
{
  "record_type": "CONFIRMED_INCIDENT",
  "incident_id": "INC-54",
  "site_code": "MBD",
  "site_name": "Mega SOC - Binh Duong",
  "started_at": "2026-05-31T13:10:00",
  "resolved_at": "2026-05-31T14:00:00",
  "duration_minutes": 50,
  "incident_type": "Fiber optic cable failure",
  "severity": "Minor",
  "resolution_status": "RESOLVED",
  "responsibility_domain": "ISP",
  "root_cause": "Fiber cable issue",
  "evidence_label": "SOURCE FACT",
  "source_ref": "google_sheet_csv:row-54"
}
```

### Zabbix monitoring pattern record

```json
{
  "record_type": "MONITORING_SIGNAL",
  "episode_id": "OPS-ALP-981B0724F60D",
  "site_code": "CPL",
  "pattern_family": "Zabbix agent/active check",
  "problem_signature": "windows: active checks are not available",
  "host": "VNMCPL-VSDHC02",
  "first_seen_at": "2026-05-23T01:11:37",
  "last_seen_at": "2026-05-23T01:11:37",
  "last_recovered_at": "2026-05-23T01:15:00",
  "query_alert_count": 1,
  "investigation_priority": "LOW",
  "signal_assessment": "UNCONFIRMED_MONITORING_SIGNAL",
  "user_impact": "UNKNOWN",
  "evidence_label": "SOURCE FACT",
  "source_ref": "zbx_problems_normalized_All_VNM_High_Disaster_2026-05.csv#csv:row-2838"
}
```

### Ticket evidence record

```json
{
  "record_type": "TICKET_EVIDENCE",
  "ticket_id": "TICKET-123",
  "site_code": "CPL",
  "created_at": "2026-05-17T16:42:00",
  "symptom": "Users report intermittent access issue",
  "affected_scope": "UNKNOWN",
  "evidence_label": "SOURCE FACT",
  "source_ref": "IssueReport.xlsx#row:123"
}
```

## SuperAgent routing rule

Prompt cua SuperAgent nen co rule:

```text
If the user asks about a site and a time range, call Query IT Ops Timeline workflow first.
Use the tool result as the primary source for counts, timelines, and grouping.
Use Knowledge only for context, definitions, evidence labels, and fallback.
Do not compute exact counts from retrieved Knowledge fragments.
If no tool result is available, state that exact time-range counts are unavailable from Knowledge-only context.
```

## Evidence priority

Khi khong du du lieu hoac 3 source mau thuan, uu tien theo thu tu:

1. ISP Incident Report
   - Confirmed incident existence.
   - Start/end time.
   - RCA.
   - Resolution status.
   - ISP/provider.
   - Responsibility domain.

2. ITcenter Ticket
   - Direct user evidence.
   - Affected users/scope.
   - User symptom.
   - Escalation.
   - Business impact.

3. Zabbix Alert
   - Monitoring signal.
   - Technical telemetry.
   - Timing context.
   - Recurrence.
   - Supporting or contextual signal only.

Zabbix alert khong duoc goi la confirmed incident neu khong co ISP Incident Report hoac ticket/source khac xac nhan.

## Cach SuperAgent tra loi cau hoi theo thoi gian

### Input user

```text
CPL trong thang 5/2026 co alert Zabbix gi?
```

### SuperAgent action

Call Query IT Ops Timeline:

```json
{
  "site_code": "CPL",
  "from_at": "2026-05-01T00:00:00",
  "to_at": "2026-06-01T00:00:00",
  "source_scope": "zabbix"
}
```

### Tool result

```json
{
  "matched_event_count": 37,
  "monitoring_family_summary": [
    {
      "pattern_family": "Network reachability",
      "pattern_count": 12,
      "query_alert_count": 16
    },
    {
      "pattern_family": "HTTP monitoring",
      "pattern_count": 21,
      "query_alert_count": 987
    },
    {
      "pattern_family": "Host restart/uptime",
      "pattern_count": 2,
      "query_alert_count": 2
    },
    {
      "pattern_family": "Zabbix agent/active check",
      "pattern_count": 2,
      "query_alert_count": 2
    }
  ],
  "confirmed_incidents": [],
  "related_tickets": []
}
```

### SuperAgent answer

```text
Trong thang 5/2026, CPL ghi nhan 37 Zabbix monitoring patterns.

Nhom dang chu y nhat la Network reachability voi 12 patterns / 16 alerts,
vi nhom nay co the lien quan den mat ket noi, thiet bi down, hoac monitoring-path instability.

HTTP monitoring co 21 patterns / 987 alerts, la nhom nhieu nhat ve so luong,
nhung thuong can review threshold/probe timeout truoc khi coi la su co nguoi dung.

Host restart/uptime va Zabbix agent/active check moi nhom co 2 patterns / 2 alerts,
nen duoc xem la context ky thuat hoac monitoring health.

Khong co confirmed incident hoac ITcenter ticket khop truc tiep trong tool result,
nen user impact la UNKNOWN / NO_DIRECT_EVIDENCE.
```

## Xu ly same-site/time Zabbix correlation

Khong duoc mac dinh rang alert Zabbix cung site/cung thoi gian la bang chung RCA.

Phan loai:

| Status | Y nghia |
|---|---|
| `RELATED_TO_CONFIRMED_INCIDENT` | Alert signature phu hop voi incident type/RCA |
| `TIME_ALIGNED_CONTEXT_ONLY` | Cung site/time nhung signature khong lien quan truc tiep |
| `NO_MATCHING_ZABBIX_SIGNAL` | Khong co Zabbix signal khop |
| `UNCONFIRMED_MONITORING_SIGNAL` | Zabbix-only signal, chua co incident/ticket xac nhan |
| `LIKELY_NOISE_OR_THRESHOLD_REVIEW` | Nhieu kha nang la threshold/probe/noise can review |

Vi du:

```text
Incident: Fiber optic cable failure
Zabbix alert: host has been restarted
=> TIME_ALIGNED_CONTEXT_ONLY, khong phai proof cua fiber fault.
```

```text
Incident: Fiber optic cable failure
Zabbix alert: unavailable by icmp ping / interface down / packet loss
=> RELATED_TO_CONFIRMED_INCIDENT hoac supporting context manh hon.
```

## Fallback neu Query workflow chua san sang

Neu chua tao duoc Query workflow tren Alpha:

1. SuperAgent co the tra loi tu Knowledge Markdown.
2. Bat dau voi `04_alert_patterns.md` -> `Site Pattern Family Summary`.
3. Chi noi la day la full-export/site-level summary neu khong co exact time-range query.
4. Khong dua exact count theo thang/ngay neu Knowledge khong ghi ro.
5. Neu context bi thieu, tra loi:

```text
Trong Knowledge context hien tai, toi chi thay mot phan Zabbix pattern cua site CPL.
Khong du de ket luan exact count cho rieng thang 5. Can chay Query IT Ops Timeline
de co count chinh xac theo khoang thoi gian.
```

## Thu tu build tren Alpha

### Phase 1. Hoan thien processing workflows

1. `Clean Rawdata - ISP`
2. `Clean Rawdata - Zabbix`
3. `Clean Rawdata - ITcenter`

Validation toi thieu:

```text
ISP: record_count dung voi so incident that
Zabbix: alert_patterns duoc group theo pattern_family
Ticket: ticket records co site_code va created_at
```

### Phase 2. Tao connector workflow

Workflow nay gom:

```text
confirmed_incidents
zabbix_alerts
alert_patterns
ticket_evidence
  -> connect/correlate
  -> operational_timeline.json
  -> Markdown Knowledge Package
```

Validation toi thieu:

```text
validation_status = PASS
upload_allowed = true
```

### Phase 3. Upload Markdown vao Knowledge

Upload cac file `.md` sau khi validation pass.

Khong upload `.json` vao Knowledge.

### Phase 4. Tao Query IT Ops Timeline workflow/tool

Input:

```json
{
  "site_code": "string",
  "from_at": "datetime",
  "to_at": "datetime",
  "source_scope": "all|incident|ticket|zabbix"
}
```

Output:

```json
{
  "ok": true,
  "matched_event_count": 0,
  "events": [],
  "monitoring_family_summary": [],
  "confirmed_incidents": [],
  "related_tickets": [],
  "answer_contract": {}
}
```

### Phase 5. Gan Query workflow lam tool cho SuperAgent

Trong SuperAgent prompt:

```text
For site/time-range questions, call Query IT Ops Timeline first.
Do not answer exact counts from Knowledge-only fragments.
```

### Phase 6. Test validation prompts

Test cac cau:

```text
1. Trong khoang 2025-12-03T00:00:00 den 2025-12-04T00:00:00, site MS2 co su kien gi?
2. CPL trong thang 5/2026 co alert Zabbix gi?
3. OPS-INC-53 co Zabbix alert nao lien quan khong?
4. Site MBD ngay 2026-05-31 co su kien gi?
5. Cac su co fiber optic cable failure trong thang 5 co lien quan ISP nao?
6. Co ticket nguoi dung nao khop voi incident INC-54 khong?
```

Expected behavior:

- Neu co tool result, answer phai dung tool result.
- Neu khong co ticket/user evidence, khong duoc ket luan user impact.
- Zabbix-only alert khong duoc goi la incident.
- Same-site/time alert khong duoc coi la RCA proof neu signature khong phu hop.

## Checklist build tren Alpha

```text
[ ] ISP processor workflow da pass
[ ] Zabbix processor workflow da pass
[ ] ITcenter processor workflow da pass
[ ] Connector workflow tao duoc operational_timeline.json
[ ] Markdown package validation PASS
[ ] Markdown files da upload Knowledge
[ ] Query IT Ops Timeline workflow nhan site_code/from_at/to_at/source_scope
[ ] Query workflow tra monitoring_family_summary cho Zabbix questions
[ ] SuperAgent prompt bat buoc call query workflow cho site/time-range questions
[ ] 6 validation prompts da pass
```

## Quyet dinh kien truc

Chon kien truc:

```text
Alpha orchestration + deterministic processing/query tools + Knowledge context + SuperAgent explanation
```

Khong chon:

```text
SuperAgent tu doc raw/Markdown roi tu dem va tu correlate
```

Ly do:

- Time-range query can exact filtering.
- Zabbix co nhieu raw alert de retrieve sai fragment.
- RAG khong on dinh cho counting/grouping.
- Manager can cau tra loi on dinh, co evidence va khong phong dai user impact.
