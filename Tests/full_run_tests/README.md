# Full Run Tests

Purpose: test the complete robot behaviour through a maze section or full maze — RFID reading, movement execution, and wall avoidance combined.

## Prerequisites

All of the following must have passing test logs before a full run test:
- [ ] Straight line tests pass (`Tests/straight_line_tests/`)
- [ ] Turn calibration pass (`Tests/turn_tests/`)
- [ ] RFID UID mapping complete (`Tests/rfid_tests/`)
- [ ] Wall following stable (`Tests/wall_following_tests/`)

## What to Record Per Session

| Field | Description |
|-------|-------------|
| Date | YYYY-MM-DD |
| Battery voltage | At start and end |
| Maze layout | Sketch or photo of the test course |
| Commands issued (from RFID) | Sequence of commands the robot received |
| Commands executed | What the robot actually did |
| Wall contacts | Count and location |
| Completion | Yes / No / Partial |
| Time | Seconds from START to STOP |

## File Naming

`YYYY-MM-DD_full_run_test.md`
