# Calibration

## Purpose

Records the measured and tuned constants that control all robot movement. Every firmware version must start from the last stable values in this file.

## Current Motor Constants

| Constant | Current Value | Meaning |
|----------|-------------:|---------|
| `BASE_PWM` | 160 | Straight drive speed (0–255) |
| `TURN_PWM` | 130 | Turn speed (lower = more accurate) |
| `STRAIGHT_PULSES` | 70 | One forward step (~23 cm) |
| `TURN_90_PULSES` | 28 | Initial 90° pivot value (calculated, not yet tuned) |

These values are defined at the top of `Code/Pico/motor_control/phase1_motor_calibration.ino`.

## Measured Physical Parameters

| Parameter | Value | Source |
|-----------|------:|--------|
| Wheel diameter | 37 mm | Measured on robot |
| Wheel-to-wheel distance (L) | 115 mm | Measured on robot |
| Encoder pulses per revolution | 35 | Measured (HC-89, RISING edge) |
| 90° pulse target (calculated) | 27.2 → start at 28 | π × L/4 ÷ (π × d) × PPR |

Calculation:
```
Wheel circumference  = π × 37 mm = 116.24 mm
Arc for 90° pivot    = π × 115 mm / 4 = 90.32 mm
Revolutions needed   = 90.32 / 116.24 = 0.777
Pulse target         = 0.777 × 35 = 27.2  → start at 28
```

## Left vs Right Turn Calibration

Left and right turns must be calibrated separately. A single `TURN_90_PULSES` value is not sufficient if the robot consistently overshoots one direction and undershoots the other due to chassis asymmetry, gear wear, or mounting differences.

| Direction | Calibrated Pulse Count | Last Tested | Notes |
|-----------|----------------------:|-------------|-------|
| Left 90° | TBD | — | |
| Right 90° | TBD | — | |

## Straight Line Drift Correction

Software trim applied inside `goStraight()` when one encoder leads the other by more than 2 pulses:

```cpp
if (pulseL > pulseR + 2) {
    analogWrite(PWM_L, BASE_PWM - 15);  // slow down leading wheel
} else if (pulseR > pulseL + 2) {
    analogWrite(PWM_R, BASE_PWM - 15);
}
```

Trim offset of 15 is a starting point. Increase if still drifting, decrease if oscillating.

## Calibration Procedure

See [`Docs/testing_protocol.md`](testing_protocol.md) for the step-by-step test sequence.

Short version:
1. Verify encoder counting (35 pulses per manual wheel revolution).
2. Confirm forward direction.
3. Tune `BASE_PWM` and drift trim for straight movement.
4. Tune `TURN_90_PULSES` for right turns.
5. Tune separately for left turns if asymmetric.
6. Run 4-turn heading-return test (R→R→L→L) and measure accumulated error.

## Locked Values After Calibration

Fill in after successful calibration sessions:

| Parameter | Locked Value | Surface | Date |
|-----------|------------:|---------|------|
| `BASE_PWM` | | | |
| `TURN_PWM` | | | |
| `STRAIGHT_PULSES` | | | |
| `LEFT_90_PULSES` | | | |
| `RIGHT_90_PULSES` | | | |

## Test Logs

See `Tests/turn_tests/` and `Tests/straight_line_tests/` for dated test session files.
