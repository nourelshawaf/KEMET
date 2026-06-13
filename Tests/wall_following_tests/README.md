# Wall Following Tests

Purpose: verify IR sensor readings are accurate and that the lateral correction loop keeps the robot centred in the corridor.

## What to Record Per Session

| Field | Description |
|-------|-------------|
| Date | YYYY-MM-DD |
| Battery voltage | Measured at test start |
| Surface | OSB / tile |
| Left IR raw ADC | Value at known distances |
| Right IR raw ADC | Value at known distances |
| Correction threshold | PWM deadband used |
| Result | Robot stayed centred / drifted / oscillated |

## Pass Criteria

- Robot stays within ±2 cm of corridor centre over 1 m straight run.
- No wall contact.
- No oscillation (side-to-side overcorrection).

## File Naming

`YYYY-MM-DD_wall_following_test.md`
