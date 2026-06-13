# Code

## Structure

| Folder | Board | Status |
|--------|-------|--------|
| `Pico/motor_control/` | Raspberry Pi Pico | Phase 1 — in progress |
| `Pico/encoder_tests/` | Raspberry Pi Pico | Planned |
| `Pico/pid_speed_control/` | Raspberry Pi Pico | Planned |
| `ESP32/rfid_reader/` | ESP32 | Planned |
| `ESP32/maze_logic/` | ESP32 | Planned |
| `ESP32/sensor_tests/` | ESP32 | Planned |
| `integration/esp32_pico_uart/` | Both | Planned |

## ESP32

Handles RFID reading, ToF sensing, IR wall sensing, maze state machine, and high-level navigation decisions. Sends ASCII movement commands to the Pico over UART.

## Pico

Handles PWM generation, encoder pulse counting, straight-line drift correction, and 90° pivot execution. Replies `OK\n` over UART when a movement completes.

## Flashing Order

1. Flash `Pico/motor_control/phase1_motor_calibration.ino` to the Pico.
2. Open Serial Monitor at 115200 baud.
3. Test encoder counting and motor direction.
4. Calibrate `TURN_90_PULSES` per surface.
5. Flash ESP32 RFID/navigation code (Phase 4).
6. Test UART command round-trip between ESP32 and Pico.

## IDE Setup

- Board for Pico: **Raspberry Pi Pico** (Arduino-Pico core)
- Board for ESP32: **ESP32 Dev Module** (ESP32 Arduino core)
- Baud rate for all Serial Monitor: **115200**
