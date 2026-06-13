# Power Tests

Purpose: verify the power system stays stable under motor load, measure current draw, and confirm voltage rails do not sag during operation.

## What to Record Per Session

| Field | Description |
|-------|-------------|
| Date | YYYY-MM-DD |
| Battery voltage at rest | V |
| Battery voltage under motor load | V (both motors running at BASE_PWM) |
| Buck converter output at rest | V |
| Buck converter output under motor load | V |
| Current draw — motors only | A |
| Current draw — full system | A |
| ESP32/Pico resets during run | yes / no |

## Pass Criteria

- Buck output stays above 4.85 V under full motor load.
- No ESP32 or Pico resets during a 30-second run.
- Battery voltage under load does not drop below 6.8 V (2S cutoff threshold).

## File Naming

`YYYY-MM-DD_power_test.md`
