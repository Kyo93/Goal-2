# Ticket Impact Partition Index

> Use this file to choose the monthly ticket partition before reading ticket details.

```yaml
record_type: TICKET_IMPACT_PARTITION_INDEX
partition_basis: comment_activity_month
dedupe_key: ticket_id
primary_impact_time: ticket_created_at
activity_time: comment_created_at/comment_updated_at
```

## Query Rules

- Select partitions by requested activity window, then dedupe by `ticket_id`.
- For user/business impact timing, prefer `ticket_created_at` / `evidence_started_at`.
- For ongoing evidence, use `evidence_last_seen_at` and comment activity fields.
- A ticket may appear in multiple month partitions when comments span months.

## Available Partitions

### 2026-04

```yaml
partition_month: 2026-04
knowledge_filename: 05_ticket_impact_2026_04.md
ticket_count: 1561
comment_row_count: 4056
source_files: Goal2- Ticket Issue raw 04-2026.csv, Goal2- Ticket Issue raw 05-2026.csv, Goal2- Ticket Issue raw 06-2026.csv
ticket_created_at_min: 2025-07-31T04:43:41
evidence_last_seen_at_max: 2026-06-06T19:03:18
```

- Top classifications: `General IT Inquiry` (1301), `Computer` (162), `IT Security` (48), `Equipment` (31), `IT Asset` (4), `IT Infrastructure` (4), `Peripheral` (3), `System & Network Access` (3)
- Top locations: `Hub - Mien Bac` (254), `SPX - HCM HUB` (242), `SPX - HN HUB` (219), `Hub - Mien Trung` (144), `Hub - Tay Nam Bo` (111), `Hub - Dong Nam Bo` (75), `SOC - Mien Trung` (60), `Sonatus Building` (57)
- Top symptom families: `hardware_or_device` (694), `vpn_or_remote_access` (208), `other_or_unclear` (205), `request_or_howto` (192), `application_error` (141), `account_or_permission` (43), `network_slow_or_latency` (32), `security_alert_or_malicious_domain` (32)
- Top resolution signals: `RESOLVED` (615), `PENDING` (484), `UNKNOWN` (390), `ESCALATED` (72)
- Top comment signals: `PENDING_SIGNAL` (750), `PROBLEM_SIGNAL` (687), `RESOLUTION_SIGNAL` (559), `ESCALATION_SIGNAL` (472), `USER_CONFIRMATION_SIGNAL` (106)

### 2026-05

```yaml
partition_month: 2026-05
knowledge_filename: 05_ticket_impact_2026_05.md
ticket_count: 1282
comment_row_count: 4315
source_files: Goal2- Ticket Issue raw 04-2026.csv, Goal2- Ticket Issue raw 05-2026.csv, Goal2- Ticket Issue raw 06-2026.csv
ticket_created_at_min: 2025-10-10T10:05:24
evidence_last_seen_at_max: 2026-06-06T21:47:47
```

- Top classifications: `General IT Inquiry` (1044), `Computer` (155), `IT Security` (43), `Equipment` (22), `IT Asset` (10), `HR Management` (2), `IT Infrastructure` (2), `Other Hardware` (1)
- Top locations: `SPX - HCM HUB` (234), `Hub - Mien Bac` (211), `SPX - HN HUB` (165), `Hub - Mien Trung` (104), `Hub - Tay Nam Bo` (78), `Sonatus Building` (56), `Warehouse - Bac Ninh` (55), `Hub - Dong Nam Bo` (54)
- Top symptom families: `hardware_or_device` (875), `application_error` (150), `vpn_or_remote_access` (101), `request_or_howto` (42), `security_alert_or_malicious_domain` (33), `account_or_permission` (31), `other_or_unclear` (18), `network_slow_or_latency` (15)
- Top resolution signals: `PENDING` (538), `RESOLVED` (506), `UNKNOWN` (130), `ESCALATED` (108)
- Top comment signals: `PROBLEM_SIGNAL` (1059), `PENDING_SIGNAL` (932), `ESCALATION_SIGNAL` (874), `RESOLUTION_SIGNAL` (380), `USER_CONFIRMATION_SIGNAL` (196)

### 2026-06

```yaml
partition_month: 2026-06
knowledge_filename: 05_ticket_impact_2026_06.md
ticket_count: 500
comment_row_count: 1154
source_files: Goal2- Ticket Issue raw 04-2026.csv, Goal2- Ticket Issue raw 05-2026.csv, Goal2- Ticket Issue raw 06-2026.csv
ticket_created_at_min: 2025-10-27T10:15:38
evidence_last_seen_at_max: 2026-06-07T10:30:16
```

- Top classifications: `General IT Inquiry` (428), `Computer` (49), `Equipment` (11), `IT Security` (7), `IT Asset` (3), `HR Management` (1), `Peripheral` (1)
- Top locations: `SPX - HCM HUB` (111), `Hub - Mien Bac` (65), `SPX - HN HUB` (64), `Hub - Mien Trung` (47), `Hub - Dong Nam Bo` (36), `Warehouse - Bac Ninh` (27), `Hub - Tay Nam Bo` (26), `SOC - Binh Duong` (21)
- Top symptom families: `hardware_or_device` (376), `application_error` (54), `vpn_or_remote_access` (29), `request_or_howto` (14), `network_slow_or_latency` (9), `account_or_permission` (7), `security_alert_or_malicious_domain` (5), `other_or_unclear` (3)
- Top resolution signals: `PENDING` (217), `RESOLVED` (190), `UNKNOWN` (63), `ESCALATED` (30)
- Top comment signals: `PROBLEM_SIGNAL` (428), `PENDING_SIGNAL` (381), `ESCALATION_SIGNAL` (374), `RESOLUTION_SIGNAL` (119), `USER_CONFIRMATION_SIGNAL` (95)
