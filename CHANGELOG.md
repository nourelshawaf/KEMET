# Changelog

## [Unreleased]

### Added
- Full project documentation structure (`Docs/`, `Tests/`, `Hardware/`, `Media/`)
- `Docs/system_architecture.md` — dual-controller design and communication protocol
- `Docs/competition_rules_summary.md` — engineering-relevant competition constraints
- `Docs/hardware_design.md` — component selection and power architecture
- `Docs/electronics_power_system.md` — voltage rails and pre-power checklist
- `Docs/motor_control.md` — Pico motor control, calibration parameters, known issues
- `Docs/rfid_navigation.md` — RC522 integration and UID command mapping
- `Docs/wall_following.md` — Sharp IR and ToF sensor wall detection
- `Docs/calibration.md` — step-by-step Phase 1 motor calibration guide
- `Docs/testing_protocol.md` — standard test log format and Phase 1 test sequence
- `Docs/troubleshooting.md` — symptom → cause → fix table for all subsystems
- `Hardware/bill_of_materials.md` — full BOM for Prototype V1
- GitHub issue templates and PR template
- `CONTRIBUTING.md` — commit style and file location guide

### Changed
- `README.md` restructured to short overview with links to `Docs/`
- `pico/` moved to `Code/Pico/motor_control/`
- `docs/` moved to `Docs/`
- `schematics/` moved to `Hardware/schematics/` and `Hardware/wiring_diagrams/`

## [0.1.0] — 2026-06

### Added
- Prototype V1 assembled
- `pico/phase1_motor_calibration/` — encoder-based straight and 90° turn firmware
- `schematics/KEMET_V1_Schematic.json` — EasyEDA schematic for Prototype V1
- `schematics/KEMET_V1_Wiring_Table.md` — full pin-to-pin wiring table
- `docs/CALIBRATION_GUIDE.md` — Phase 1 calibration procedure
