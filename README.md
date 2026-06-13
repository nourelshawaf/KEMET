# KEMET

Autonomous maze-solving robot for the Óbuda University Labyrinth Competition.

## Project Goal

KEMET navigates a maze autonomously using RFID-based navigation, wall-following via IR and ToF sensors, encoder-based motor control, and second-run path optimisation.

## Competition Context

Robot must fit inside `280 × 280 × 150 mm`, operate fully autonomously with no remote communication during the run, and respond to RFID navigation markers (`START`, `STOP`, `LEFT`, `RIGHT`, `DEAD END`). Maze corridor width is `28.5 ± 1 cm`. Qualification includes a straight-track and a curved-track task.

## System Overview

| Subsystem | Component |
|-----------|-----------|
| Navigation controller | ESP32 (ESP-WROOM-32) |
| Motor controller | Raspberry Pi Pico |
| Motor driver | TB6612FNG |
| Motors | 2× DC gear motors, Ø 37 mm wheels |
| Encoders | 2× HC-89 optical sensors (35 pulses/rev) |
| RFID | RC522 (3.3 V only) |
| Front distance | VL53L1X ToF |
| Side/wall sensing | 4× Sharp GP2Y0A51SK0F IR |
| IMU | MPU6050 (planned — angle correction) |
| Power | 2S Li-ion → main switch → buck (5 V logic) + direct (motor rail) |

## Development Status

| Phase | Status | Description |
|-------|--------|-------------|
| Phase 1 | **In progress** | Pico standalone: encoder-based straight + 90° turns |
| Phase 2 | Planned | ESP32 ↔ Pico UART integration |
| Phase 3 | Planned | Front ToF wall detection |
| Phase 4 | Planned | RFID reading and command relay |
| Phase 5 | Planned | Maze mapping and path optimisation |

## Quick Start — Phase 1

1. Flash `Code/Pico/motor_control/phase1_motor_calibration.ino` to the Pico (Arduino IDE, board: Raspberry Pi Pico).
2. Open Serial Monitor at **115200 baud**.
3. Robot runs: **Straight → Right → Right → Left → Left**, then repeats.
4. Follow [`Docs/calibration.md`](Docs/calibration.md) for the full tuning procedure.

Key constants at the top of the sketch:

```cpp
static const int BASE_PWM        = 160;  // Straight drive speed
static const int TURN_PWM        = 130;  // Turn speed
static const int STRAIGHT_PULSES =  70;  // ~23 cm straight distance
static const int TURN_90_PULSES  =  28;  // Pulses for 90° pivot — main thing to tune
```

## Repository Structure

- [`Code/`](Code/) — firmware for ESP32, Pico, and integration
- [`Hardware/`](Hardware/) — wiring diagrams, schematics, BOM
- [`Docs/`](Docs/) — full technical documentation
- [`Tests/`](Tests/) — test logs and calibration results
- [`Media/`](Media/) — photos, videos, diagrams

## Documentation Index

- [System Architecture](Docs/system_architecture.md)
- [Competition Rules Summary](Docs/competition_rules_summary.md)
- [Hardware Design](Docs/hardware_design.md)
- [Electronics & Power System](Docs/electronics_power_system.md)
- [Motor Control](Docs/motor_control.md)
- [RFID Navigation](Docs/rfid_navigation.md)
- [Wall Following](Docs/wall_following.md)
- [Calibration](Docs/calibration.md)
- [Testing Protocol](Docs/testing_protocol.md)
- [Troubleshooting](Docs/troubleshooting.md)
- [Prototype V1](Docs/prototypes/prototype_v1.md)
- [Prototype V2](Docs/prototypes/prototype_v2.md)

## Prototype Photos

![Prototype V1 wiring top](Media/photos/prototype_v1/prototype_v1_wiring_top.jpg)
*Prototype V1 — top view after full wiring integration.*

![Prototype V2 top overview](Media/photos/prototype_v2/prototype_v2_top_overview.jpg)
*Prototype V2 — current build with all subsystems integrated.*

See [Prototype V1](Docs/prototypes/prototype_v1.md) and [Prototype V2](Docs/prototypes/prototype_v2.md) for full documentation.

## Team

KEMET Maze Robot Team — Óbuda University
