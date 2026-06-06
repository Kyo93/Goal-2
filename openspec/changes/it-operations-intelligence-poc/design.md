# Design: IT Operations Knowledge Package for Alpha Intelligence

## Context and Technical Approach

The implementation is a local Python converter, not an application server.

It converts three raw Excel exports into a package designed for Alpha Intelligence Knowledge Expert ingestion. A Super Agent uses the Knowledge Expert to answer flexible operational questions.

The design separates:

1. **Source fact:** a row or group of rows from an imported file.
2. **Computed fact:** deterministic output calculated by Python.
3. **AI inference:** a Super Agent explanation or hypothesis grounded in retrieved facts.

The primary retrieval path is timeline-first. Source-specific documents remain
available for drill-down and audit, but the Super Agent should start with an
operational timeline when the user asks what happened during a period.

## Proposed Changes

### 1. Converter Entry Point

Add a CLI:

```powershell
python scripts/build_alpha_knowledge_package.py `
  --raw-dir 01-RawData `
  --master-data "03-Data clean logic/reference doc/it-operations-master-data-template.xlsx" `
  --output-dir 02-Output/alpha-knowledge-package
```

The master-data argument is optional. Only rows with `review_status=CONFIRMED` affect factual mappings.

### 2. Source Adapters

Implement one adapter per source:

- `issue_report_adapter`
- `incident_form_adapter`
- `zabbix_adapter`
- `master_data_adapter`

Each adapter:

- Verifies required columns.
- Skips empty sheets and blank rows.
- Normalizes whitespace.
- Preserves source filename, sheet name, and source row number.
- Emits validation warnings rather than inventing missing values.

### 3. Canonical Records

#### Confirmed Incident

Important fields:

- `incident_id`
- `source_ref`
- `started_at`
- `resolved_at`
- `duration_minutes`
- `site_code`
- `site_name`
- `isp`
- `incident_type`
- `severity`
- `description`
- `initial_cause`
- `troubleshooting_actions`
- `root_cause`
- `preventive_action`
- `resolution_status`
- `recurrence_key`

#### Alert Pattern

Important fields:

- `alert_pattern_id`
- `source_refs`
- `first_seen_at`
- `last_seen_at`
- `alert_count`
- `resolved_count`
- `open_count`
- `host`
- `site_code`
- `severity`
- `problem_signature`
- `domain`
- `component`
- `scope`
- `assessment`

#### Ticket Evidence

Important fields:

- `ticket_id`
- `source_refs`
- `first_comment_at`
- `last_comment_at`
- `classification`
- `title`
- `business_unit`
- `department`
- `user_name`
- `user_email`
- `assignee`
- `comment_count`
- `comments_summary`
- `impact_evidence`

#### Operational Episode

Important fields:

- `episode_id`
- `episode_type`: `CONFIRMED_INCIDENT` or `MONITORING_SIGNAL`
- `started_at`
- `ended_at`
- `site_code`
- `summary`
- ordered `milestones`
- `signal_assessment`
- `responsibility_domain`: `INHOUSE`, `ISP`, `EXTERNAL`, or `UNKNOWN`
- `responsibility_basis`
- `user_impact_status`: `CONFIRMED`, `ESTIMATED`, `NO_EVIDENCE`, or `UNKNOWN`
- `related_incident_ids`
- `related_alert_pattern_ids`
- `related_ticket_ids`
- `correlation_basis`
- `source_refs`

Timeline correlation is conservative:

- A confirmed incident is always represented as an operational story.
- A grouped Zabbix alert pattern is always represented as a monitoring-signal story.
- A Zabbix pattern is linked to an incident only when the site matches and the
  time windows overlap within a small deterministic buffer.
- A ticket is linked to an incident only when its text explicitly contains the
  incident site code and its comment window overlaps the same deterministic buffer.
- A correlation link is evidence context. It never changes a raw alert into a
  confirmed incident and never becomes RCA by itself.

### 4. Deterministic Summaries

Compute in Python:

- Source profile and date ranges.
- Confirmed incident counts by month, site, ISP, type, and severity.
- Incident recurrence grouped by normalized `site_code + ISP + incident_type`.
- Alert patterns grouped by `host + normalized problem signature`.
- Ticket counts and selected impact evidence.
- Missing RCA and missing preventive-action counts.
- Master-data coverage and unconfirmed mapping warnings.
- Operational stories and coverage period.
- Signal-assessment counts for confirmed-incident correlation, direct user-impact
  evidence, noise or threshold review, and unconfirmed monitoring signals.
- Responsibility-domain counts from deterministic RCA classification rules.

### 5. Alpha Knowledge Package

Generate:

```text
02-Output/alpha-knowledge-package/
  manifest.json
  validation_report.json
  validation_report.md
  00_report_context.md
  01_executive_summary.md
  02_operational_timeline.md
  02_confirmed_incidents.md
  03_recurrence_patterns.md
  04_alert_patterns.md
  05_ticket_impact.md
  06_data_quality.md
  normalized_data.xlsx
```

Markdown documents are primary Knowledge Expert inputs. `normalized_data.xlsx` is for audit and manual inspection.

`validation_report.json` and `validation_report.md` are mandatory release-gate artifacts. Do not upload the package to Alpha when the final status is `FAIL`.

Each Markdown record must:

- Use stable headings for chunk retrieval.
- Include a stable record ID.
- Include source references.
- State whether content is `SOURCE FACT`, `COMPUTED FACT`, `ESTIMATED`, or `UNKNOWN`.

`02_operational_timeline.md` is the primary date-range investigation entry point.
The remaining detailed documents are evidence drill-down sources.

### 6. Alpha Configuration

For the PoC:

1. Create an Alpha project space.
2. Create a native Knowledge Expert for the generated package.
3. Upload the Markdown files.
4. Create a Super Agent.
5. Attach the Knowledge Expert as a skill.
6. Add the provided instruction template and preset questions.
7. Use Inspect Mode during validation.

## Verification

- Converter fails clearly when required source columns are missing.
- Supplied sample files produce 923 unique tickets, 52 confirmed incidents, and 1,000 alert rows before grouping.
- Incident recurrence includes `MS2 | VNPT | High latency = 16`.
- Incident recurrence includes `XAS | CMC | Fiber optic cable failure = 4`.
- Alert patterns retain source lineage and never inflate confirmed-incident statistics.
- Markdown package includes guardrails and data-quality limitations.
- Audit workbook opens and contains normalized tables.
- Reconciliation invariants hold for incidents, Zabbix alerts, and issue-report comment rows.
- A failed required invariant sets package validation status to `FAIL`.
- Unchanged input produces stable record IDs and package content except for generated timestamps.
- Super Agent validation prompts answer with retrieved evidence and explicit limitations.
- Operational timeline contains a milestone sequence and conclusion for every
  confirmed incident and every grouped Zabbix alert pattern without conflating the two types.
- Responsibility classification is explicit and auditable, and remains `UNKNOWN`
  when converter rules do not support a category.
