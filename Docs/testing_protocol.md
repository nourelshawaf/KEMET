# Testing Protocol

## Purpose

Defines the standard test procedure for each subsystem and the format for recording test results in `Tests/`.

## Test Log Format

Every test session gets one file in the appropriate subfolder under `Tests/`. File name: `YYYY-MM-DD_description.md`.

```md
# [Test Name]

Date: YYYY-MM-DD
Robot version: Prototype V1
Battery voltage: ___ V
Firmware commit: (git short hash)
Surface: (OSB / floor tile / smooth floor / carpet)
Test type: (describe exactly what is being tested)

## Setup

(Describe any physical setup, markings, tape lines used)

## Results

| Trial | Input / Target | Observed | Error | Notes |
|-------|---------------|---------|-------|-------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Conclusion

(What was learned. What to change next.)
```

## Phase 1 Test Sequence

Run these in order. Do not proceed to the next test until the current one passes consistently.

### 1. Encoder count verification

- Comment out all motor calls.
- Print `pulseL` and `pulseR` to Serial.
- Manually spin each wheel one full revolution.
- **Pass:** both counters increment by 35 ±2.

### 2. Forward direction

- Run sketch, observe straight segment only.
- **Pass:** robot moves forward (away from the start line).

### 3. Straight drift

- Drive straight for `STRAIGHT_PULSES = 70` pulses on a 2-metre tile floor.
- **Pass:** robot endpoint is within 3 cm of the start heading.

### 4. Right turn accuracy

- Mark heading with tape. Run one right turn.
- **Pass:** final heading is within ±5° of 90°.

### 5. Left turn accuracy

- Same as above for left turn.
- **Pass:** final heading is within ±5° of 90°.

### 6. 4-turn heading return

- Run R→R→L→L sequence.
- **Pass:** robot returns to within ±10° of starting heading.

## Where to Save Results

| Test type | Folder |
|-----------|--------|
| Straight distance | `Tests/straight_line_tests/` |
| 90° turns | `Tests/turn_tests/` |
| RFID reading | `Tests/rfid_tests/` |
| Wall following | `Tests/wall_following_tests/` |
| Full maze run | `Tests/full_run_tests/` |
