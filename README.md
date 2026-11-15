# Panel Schedule Generator (Canadian Commercial Format)

Build a panel schedule the way Canadian commercial drawings carry it: header block (designation, system, bus, main, AIC, fed-from), circuits with A-B-C phase rotation, connected VA per phase, and a phase-balance check — in the browser, or from a JSON circuit list on the command line, ready to paste into a drawing set or a panel door directory.

**Live web tool:** https://dust2engineering.github.io/ontario-panel-schedule-generator/web/

## How it works

- Enter circuits with description, load type, connected VA, poles and breaker size; 1-pole circuits rotate A-B-C, 2-pole circuits rotate AB-BC-CA, 3-pole circuits split across all three phases.
- The schedule totals connected VA per phase and reports the balance spread as a percentage of the average phase load.
- On the command line, feed it a JSON file (see examples/) and it prints the same schedule as a text table.
- Demand factors stay visible as designer inputs: the generator totals connected load; applying CEC Section 8 demand rules remains the designer's step, and the schedule says so.

## Data in this repository

- `panel-schedule-format.json` — the standard field set (header, per-circuit columns, summary block), the phase-assignment rules and the demand-factor note, as machine-readable JSON.
- Field set confirmed against a published 42-circuit Canadian commercial panel-schedule template.

## Command line

```bash
python3 panel_schedule.py examples/example-panel.json
```

## Worked examples

- [example-panel.json](examples/example-panel.json)
- [example-output.txt](examples/example-output.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Electrical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
