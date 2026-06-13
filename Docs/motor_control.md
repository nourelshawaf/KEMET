# Motor Control

## Purpose

The Pico controls two DC gear motors through the TB6612FNG motor driver. It receives high-level ASCII movement commands from the ESP32 over UART and handles low-level PWM generation, encoder pulse counting, straight-line correction, and 90° pivot calibration.

## Hardware Used

- Raspberry Pi Pico
- TB6612FNG dual motor driver
- 2× DC gear motors (Ø 37 mm wheels)
- 2× HC-89 optical encoders (35 pulses per full wheel revolution, measured)

## Pin Connections

| Pico GP | TB6612 Pin | Function |
|---------|-----------|---------|
| GP2 | PWMA | Left motor speed (PWM) |
| GP3 | AIN (DIR) | Left motor direction |
| GP4 | PWMB | Right motor speed (PWM) |
| GP5 | BIN (DIR) | Right motor direction |
| 3V3(OUT) | VCC | TB6612 logic supply |
| GND | GND | Common ground |

| Pico GP | Encoder |
|---------|--------|
| GP6 | Left HC-89 OUT |
| GP7 | Right HC-89 OUT |

> TB6612 STBY must be tied HIGH to enable the driver.
> Right motor wires are physically reversed so both channels share the same direction logic.

## Movement Commands

| Command | Action |
|---------|--------|
| `FWD` | Drive forward — straight, encoder-controlled |
| `LEFT_90` | Pivot left 90° using encoder pulse count |
| `RIGHT_90` | Pivot right 90° using encoder pulse count |
| `STOP` | Stop all motors |
| `U_TURN` | Planned — 180° pivot |
| `LEFT_45` | Planned |
| `RIGHT_45` | Planned |

## Software Logic

**Straight movement:**
Both motors run at `BASE_PWM`. Encoder counts are compared every loop; if one wheel is ahead by more than 2 pulses, it is slowed by a trim offset until both counts re-align. Movement stops when the average pulse count reaches `STRAIGHT_PULSES`.

**90° pivot:**
One motor runs forward, the other backward, both at `TURN_PWM`. Movement stops when the average pulse count across both wheels reaches `TURN_90_PULSES`. Both wheels move to reduce wheel slip vs. a single-wheel pivot.

## Calibration Parameters

| Parameter | Value |
|-----------|-------|
| Wheel diameter | 37 mm |
| Wheel-to-wheel distance (L) | 115 mm |
| Encoder pulses per revolution | 35 (HC-89, RISING edge) |
| BASE_PWM | 160 |
| TURN_PWM | 130 |
| STRAIGHT_PULSES | 70 (~23 cm) |
| TURN_90_PULSES | 28 (calculated: 27.2, tune per floor) |

Calculated starting point for `TURN_90_PULSES`:
```
Wheel circumference  = π × 37 mm = 116.24 mm
Arc for 90° pivot    = π × 115 mm / 4 = 90.32 mm
Revolutions needed   = 90.32 / 116.24 = 0.777
Pulse target         = 0.777 × 35 = 27.2 → start at 28
```

## Current Status

Phase 1 in progress. Straight movement implemented. Encoder-based turns implemented. Calibration values not yet locked.

## Known Problems

- Turn angle error accumulates after multiple turns. After two rights and two lefts, heading may have drifted.
- Left and right turns may need separate calibration values due to chassis asymmetry.
- Mechanical wheel slip on smooth floors increases turn error.
- Drift correction trim value (currently 15 PWM units) not yet verified on all floor surfaces.

## Next Steps

- Lock `TURN_90_PULSES` per floor surface.
- Run 4-turn heading-return test and measure accumulated error.
- Store separate left/right correction constants if turns are asymmetric.
- Add closed-loop heading correction using encoder difference or IMU in a later phase.
