# Hardware Design

## Purpose

Documents the physical hardware choices, component selection rationale, and prototype V1 configuration.

## Hardware Used

| Component | Part | Notes |
|-----------|------|-------|
| Navigation controller | ESP32 (ESP-WROOM-32) | Hardware SPI, I2C, multiple ADC channels |
| Motor controller | Raspberry Pi Pico | Dedicated PWM hardware; predictable timing |
| Motor driver | TB6612FNG | Dual DC motor driver, 3.3 V logic compatible |
| Motors | 2× DC gear motors | Wheel Ø = 37 mm |
| Encoders | 2× HC-89 optical sensors | 35 pulses per wheel revolution (measured) |
| RFID reader | RC522 | 3.3 V only — never connect to 5 V |
| Front distance | VL53L1X ToF | I2C, Adafruit library |
| Side distance | 4× Sharp GP2Y0A51SK0F | Analog output, 5 V supply |
| Power | 2S Li-ion + buck converter | Buck → 5 V logic; battery direct → motor rail |

## Chassis

- Prototype V1 is assembled on a custom chassis.
- Robot width must remain under 280 mm (competition constraint).
- Wheel-to-wheel distance (L): 115 mm (measured, used in turn calculations).

## Power Architecture

```
2S Li-ion Battery
    │
    ├── Main power switch
    │       │
    │       ├── Buck converter → 5 V regulated
    │       │       ├── ESP32 VIN
    │       │       ├── Pico VSYS
    │       │       └── Sharp IR VCC (×4)
    │       │
    │       └── TB6612 VM (motor power rail, ~7.2–8.4 V)
    │
    └── Common GND bus (all modules)
```

## Key Design Decisions

| Decision | Reason |
|----------|--------|
| ESP32 handles sensing | Hardware SPI + I2C + ADC on one chip |
| Pico handles motors | Hardware PWM; no interrupt conflicts with sensing |
| UART inter-board link | Simple, 3.3 V native, sufficient bandwidth |
| 5 V for Sharp IR | Sharp sensors spec'd at 4.5–5.5 V; better range accuracy |
| 3.3 V for RC522 | RC522 is 3.3 V only; 5 V destroys it permanently |
| Battery direct to TB6612 VM | Motor current must not pass through the buck converter |
| Pico 3.3 V to TB6612 VCC | TB6612 logic must match Pico drive voltage |

## Prototype V1 Limitations

- Right motor wires are physically reversed so both channels share the same direction logic in firmware.
- TB6612 STBY pin is tied permanently HIGH (no software control of enable/disable).
- No fault detection on TB6612.

## Current Status

Prototype V1 is assembled. Motor control (Phase 1) is in progress. Sensors not yet integrated.

## Known Problems

- Sharp IR sensors require decoupling capacitors (10 µF + 0.1 µF per sensor) to avoid noisy ADC readings.
- VL53L1X breakout board regulator must be verified before powering from 5 V.

## Next Steps

- Verify VL53L1X I2C addressing on ESP32.
- Mount all four Sharp IR sensors and check ADC readings.
- Add RC522 and test SPI communication with ESP32.
