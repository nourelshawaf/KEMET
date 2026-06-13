# Contributing

## Commit Style

```
docs: add motor control documentation
hardware: update Pico to TB6612 wiring diagram
firmware: add ESP32 RFID command sender
test: add left turn calibration log
fix: correct right motor direction flag
```

Prefix options: `docs`, `hardware`, `firmware`, `test`, `fix`, `refactor`.

## Where to Put Things

| Type of work | Location |
|-------------|---------|
| Stable technical explanations | `Docs/` |
| Test runs, calibration results | `Tests/` |
| Photos and videos | `Media/` |
| Wiring and schematics | `Hardware/` |
| Firmware | `Code/` |

Do not add long engineering notes to `README.md`. Put them in `Docs/` and link from there.

## Opening Issues

Use the provided templates in `.github/ISSUE_TEMPLATE/`:
- `bug_report.yml` — firmware bugs
- `hardware_issue.yml` — wiring or component problems
- `test_result.yml` — log a test session result

## Pull Requests

Use the PR template in `.github/pull_request_template.md`. Every PR should describe what changed and how it was tested.
