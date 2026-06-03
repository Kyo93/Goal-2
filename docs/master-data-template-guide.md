# IT Operations Master Data Template Guide

## File

Use `input/it-operations-master-data-template.xlsx`.

The workbook was seeded from:

- `RawData/IssueReport.xlsx`
- `RawData/SEA - Corp IT- ILL- Incident Report   (Responses).xlsx`
- `RawData/zbx_problems_export.xlsx`

Seed values are not automatically authoritative. Confirm each row before the PoC treats it as master data.

## Review Order

1. Review `sites`.
   - Fill missing `site_name`, `location`, `business_unit`, and `criticality`.
   - Pay special attention to `CPL` and `RVF`: these codes were inferred only from Zabbix hostnames.
   - Change `review_status` to `CONFIRMED` after validation.

2. Review `hosts`.
   - Validate `site_code` and `device_type`.
   - Fill `service_code` where possible.
   - Change `review_status` to `CONFIRMED` after validation.

3. Review `network_links`.
   - Replace `TBD` in `link_code` with the actual circuit or logical-link identifier where available.
   - Fill `link_role`, such as `primary`, `backup`, or `unknown`.

4. Review `user_groups`.
   - Fill `site_code` only when a group maps to a specific site.
   - Add `estimated_user_count` where available.

5. Review `services` and `service_dependencies`.
   - Confirm the seeded service list.
   - Replace the disabled dependency example with real mappings as data becomes available.

## Status Rules

- `CONFIRMED`: validated by IT Ops and safe to treat as authoritative.
- `NEEDS_REVIEW`: derived from raw data or naming conventions.
- `DRAFT`: manually added but not validated yet.
- `REJECTED`: exclude from later ingest.

## Minimum Completion Target

For the first PoC iteration:

- Confirm all known rows in `sites`.
- Confirm Zabbix host-to-site mappings in `hosts`.
- Fill criticality for the most important sites.
- Confirm or correct the ISP rows in `network_links`.

The remaining sheets can be enriched incrementally.
