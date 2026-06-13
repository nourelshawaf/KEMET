# 90° Turn Calibration — 2026-06-14

Robot version: Prototype V2
Battery voltage: ___ V
Surface: ___
`BASE_PWM`: 160
`TURN_PWM`: 130
`TURN_90_PULSES`: 28
Firmware commit: ___

## Setup

Marked heading with tape on floor. Robot placed on tape line. Observed turn by eye and measured deviation from tape with a protractor / angle reference.

## Results

| Trial | Direction | Target | Actual | Error | Notes |
|------:|-----------|-------:|-------:|------:|-------|
| 1 | Right | 90° | | | |
| 2 | Right | 90° | | | |
| 3 | Right | 90° | | | |
| 4 | Left | 90° | | | |
| 5 | Left | 90° | | | |
| 6 | Left | 90° | | | |

## 4-Turn Heading Return

Run sequence: R → R → L → L  
Expected final heading: same as start  
Actual heading deviation: ___°

## Conclusion

TBD after testing.

## Next Change

TBD — increase/decrease `TURN_90_PULSES`, or split into separate left/right constants.
