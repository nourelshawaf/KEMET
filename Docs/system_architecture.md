# System Architecture

## Purpose

Defines how the ESP32 and Raspberry Pi Pico divide responsibilities and communicate, and how all sensors and actuators connect to each controller.

## Design Decision: Dual-Controller Split

| Controller | Responsibility |
|-----------|----------------|
| ESP32 | RFID reading, ToF sensing, IR wall sensing, maze logic, navigation decisions |
| Pico | PWM generation, encoder counting, motor speed control, movement execution |

The split keeps real-time motor control on a dedicated microcontroller (Pico) while the ESP32 handles slower, higher-level navigation logic. UART connects them at 115200 baud.

## Communication Protocol (ESP32 → Pico)

Commands are ASCII strings terminated with `\n`:

| Command | Meaning |
|---------|---------|
| `FWD\n` | Drive forward one corridor length |
| `LEFT_90\n` | Pivot left 90° |
| `RIGHT_90\n` | Pivot right 90° |
| `STOP\n` | Stop immediately |
| `U_TURN\n` | Pivot 180° (planned) |

The Pico executes the movement and sends back `OK\n` when complete.

## Data Flow

```
RFID card read
    → ESP32 decodes command
    → ESP32 sends movement string over UART
    → Pico drives motors, counts encoder pulses
    → Pico sends OK
    → ESP32 checks wall sensors and plans next move
```

## Hardware Connections Summary

See [`Hardware/wiring_diagrams/KEMET_V1_Wiring_Table.md`](../Hardware/wiring_diagrams/KEMET_V1_Wiring_Table.md) for the full pin-to-pin table.

## Current Status

Phase 1 (Pico standalone motor control) is in progress. UART integration between ESP32 and Pico is Phase 2.

## Known Problems

- Communication protocol is not yet implemented (Phase 2).
- Error handling for lost UART bytes not designed yet.

## Next Steps

- Implement UART send/receive on both boards.
- Define ACK/NACK protocol for command confirmation.
- Test latency of command round-trip.
