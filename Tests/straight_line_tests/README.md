# Straight Line Tests

Purpose: verify the robot can drive one corridor section without touching walls and without accumulated drift.

## What to Record Per Session

| Field | Description |
|-------|-------------|
| Date | YYYY-MM-DD |
| Battery voltage | Measured at test start |
| Surface | OSB / tile / smooth laminate |
| `BASE_PWM` | Value used |
| `STRAIGHT_PULSES` | Value used |
| Left encoder pulses | Actual count at stop |
| Right encoder pulses | Actual count at stop |
| Measured distance | Physical tape measurement |
| Lateral drift | cm left or right of start heading |
| Wall contact | yes / no |

## Pass Criteria

- Endpoint within 3 cm of start heading after one corridor length.
- No wall contact.
- Left and right encoder counts differ by ≤ 3 pulses.

## File Naming

`YYYY-MM-DD_straight_calibration.md`
