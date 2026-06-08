# ITCenter Ticket Comment Intelligence Plan

## Goal

Turn ITCenter monthly CSV raw exports into Alpha-ready Knowledge files that can answer user-impact questions by month, site/business scope, symptom family, and ticket lifecycle evidence.

## Problem

The ITCenter raw export is comment-level, not ticket-level. A single ticket can have many comment rows. Early comments usually describe the first symptom, while later comments often contain the real operational conclusion: escalation, pending status, restoration, user confirmation, or final handling.

Keeping only the first few comments makes the output small, but it can miss the most important evidence. Keeping the full transcript makes Alpha Knowledge files too large.

## Chosen Approach

Use deterministic lifecycle sampling:

- Group all raw comment rows by `itcenter.ticket.id`.
- Preserve all `source_refs` for audit.
- Keep `ticket_created_at` as the primary user/business impact timestamp.
- Keep activity timestamps from comment created/updated times.
- Emit monthly partitions so Alpha only needs the relevant time window.
- Keep selected comment samples:
  - `initial_comments_sample`: first 2 unique comments.
  - `key_comments_sample`: up to 3 middle comments with strong signals.
  - `final_comments_sample`: last 3 unique comments.
- Extract deterministic signals:
  - `detected_comment_signals`
  - `resolution_signal`
  - `symptom_family`
  - `symptom_family_basis`
- Excerpt long comments with `[truncated; see source_refs]`.

## Deliverables

Code:

- `src/itops_alpha/converter.py`
- `tests/test_converter.py`

Presentation / cleaning-logic docs:

- `03-Data clean logic/itcenter-ticket-data-cleaning-logic.html`

Technical docs:

- `docs/technical-data-processing.md`
- `docs/build-alpha-knowledge-package.md`
- `docs/build-on-alpha-intelligence.md`
- `docs/sample-package-validation.md`
- `openspec/changes/alpha-processing-tool/design.md`
- `openspec/changes/alpha-processing-tool/tasks.md`

Alpha upload output:

- `02-Output/alpha-knowledge-package/05_ticket_impact_index.md`
- `02-Output/alpha-knowledge-package/05_ticket_impact_2026_04.md`
- `02-Output/alpha-knowledge-package/05_ticket_impact_2026_05.md`
- `02-Output/alpha-knowledge-package/05_ticket_impact_2026_06.md`
- plus the rest of the validated Markdown package.

## Verification

Local tests:

```text
python -m unittest discover -s tests
```

Expected:

```text
Ran 29 tests
OK
```

Package build:

```text
python scripts\build_alpha_knowledge_package.py --raw-dir 01-RawData --master-data "03-Data clean logic\reference doc\it-operations-master-data-template.xlsx" --output-dir "02-Output\alpha-knowledge-package"
```

Expected:

```text
validation_status = PASS
upload_allowed = true
issue_comment_rows = 9525
aggregated_ticket_comment_count = 9525
normalized_tickets = 2681
ticket_partition_count = 3
```

## Alpha Upload Test

Upload this minimum set first:

```text
00_report_context.md
01_executive_summary.md
02_operational_timeline.md
02_confirmed_incidents.md
03_recurrence_patterns.md
04_alert_patterns.md
05_ticket_impact_index.md
05_ticket_impact_2026_05.md
06_data_quality.md
```

Use `05_ticket_impact_index.md` to choose the month. Upload only the needed monthly ticket partition when Alpha file size is tight.

## Super Agent Test Prompts

```text
For May 2026 ITCenter tickets, what are the top symptom families?
Show VPN-related ITCenter tickets in May 2026 and their resolution signals.
Which tickets have user confirmation or resolution signals?
For a ticket with truncated comments, can you still audit the raw source?
```

Expected answer behavior:

- Cite ticket IDs and source refs.
- Use monthly partition data instead of recounting retrieved fragments.
- Treat `symptom_family` and `resolution_signal` as deterministic computed fields.
- Explain `[truncated; see source_refs]` as an excerpt marker, not missing evidence.
- Do not infer confirmed incidents from tickets alone.
