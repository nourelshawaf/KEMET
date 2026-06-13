# KEMET Robot V1 — Pin-to-Pin Wiring Table

Prototype V1 | Autonomous Maze-Solving Robot  
Status: **Development / No Encoders / Open-Loop Motor Control**

---

## 1. Power Subsystem

| From | To | Wire / Note |
|------|----|-------------|
| 2S Li-ion Battery `[+]` | Main Power Switch IN | Red, 20 AWG min |
| Main Power Switch OUT | 5 V Buck Converter IN | Red |
| Main Power Switch OUT | TB6612FNG `VM` | Red — motor power rail (~7.2–8.4 V) |
| 5 V Buck Converter OUT `[+]` | ESP32 `VIN` | Red |
| 5 V Buck Converter OUT `[+]` | Raspberry Pi Pico `VSYS` | Red |
| 5 V Buck Converter OUT `[+]` | All Sharp IR `VCC` (×4) | Red — 5 V sensor supply |
| 5 V Buck Converter OUT `[+]` | VL53L1X `VIN` | Red — 5 V if breakout has regulator |
| 2S Li-ion Battery `[−]` | Common GND bus | Black, 20 AWG min |
| Buck Converter GND | Common GND bus | Black |

> **⚠ VERIFY** buck converter output = **5.00 V ±0.1 V** with a multimeter **before** connecting any board.

---

## 2. ESP32 — Sensing & Navigation

### 2a. Power

| ESP32 Pin | Connects To | Net |
|-----------|-------------|-----|
| `VIN` | 5 V Buck OUT | `+5V` |
| `3V3` | RC522 `3.3V`, internal reference | `+3V3_ESP` |
| `GND` | Common GND | `GND` |

### 2b. SPI — RC522 RFID (3.3 V ONLY)

| ESP32 GPIO | RC522 Pin | Net | Direction |
|-----------|-----------|-----|-----------|
| `GPIO5` | `SDA / SS` | `RFID_SS` | ESP32 → RC522 |
| `GPIO18` | `SCK` | `SPI_SCK` | ESP32 → RC522 |
| `GPIO23` | `MOSI` | `SPI_MOSI` | ESP32 → RC522 |
| `GPIO19` | `MISO` | `SPI_MISO` | RC522 → ESP32 |
| `GPIO4` | `RST` | `RFID_RST` | ESP32 → RC522 |
| `3V3` | `3.3V` | `+3V3_ESP` | Power |
| `GND` | `GND` | `GND` | Power |

> **⚠ RC522 MUST be powered from 3.3 V ONLY. 5 V will permanently destroy it.**

### 2c. I2C — VL53L1X Time-of-Flight

| ESP32 GPIO | VL53L1X Pin | Net | Direction |
|-----------|-------------|-----|-----------|
| `GPIO21` | `SDA` | `I2C_SDA` | Bidirectional |
| `GPIO22` | `SCL` | `I2C_SCL` | ESP32 → ToF |
| `VIN` or `3V3` | `VIN` | `+5V` or `+3V3_ESP` | Power (check breakout) |
| `GND` | `GND` | `GND` | Power |

> I2C address: `0x29` (default). Use 3.3 V supply if breakout has no onboard regulator.

### 2d. ADC — Sharp IR Sensors

| ESP32 GPIO | Sensor | Net | Note |
|-----------|--------|-----|------|
| `GPIO34` | Left Outer IR `OUT` | `IR_LO` | Input-only ADC pin |
| `GPIO35` | Left Inner IR `OUT` | `IR_LI` | Input-only ADC pin |
| `GPIO36` | Right Inner IR `OUT` | `IR_RI` | Input-only ADC pin |
| `GPIO39` | Right Outer IR `OUT` | `IR_RO` | Input-only ADC pin |

> GPIO 34/35/36/39 are **input-only** — no internal pull-up/pull-down.  
> All IR `VCC` → `+5V` rail.  All IR `GND` → Common GND.

### 2e. UART — to Raspberry Pi Pico

| ESP32 GPIO | Pico GP | Net | Direction |
|-----------|---------|-----|-----------|
| `GPIO17` (TX) | `GP1` (RX) | `UART_TX` | ESP32 → Pico |
| `GPIO16` (RX) | `GP0` (TX) | `UART_RX` | Pico → ESP32 |
| `GND` | `GND` | `GND` | Shared reference |

> Both devices are 3.3 V logic. No level shifter required.  
> Recommended baud rate: **115200**.

---

## 3. Raspberry Pi Pico — Motor Control

### 3a. Power

| Pico Pin | Connects To | Net |
|---------|-------------|-----|
| `VSYS` | 5 V Buck OUT | `+5V` |
| `3V3(OUT)` | TB6612FNG `VCC` | `+3V3_PICO` |
| `GND` | Common GND + TB6612 GND | `GND` |

### 3b. UART — to ESP32

| Pico GP | ESP32 GPIO | Net | Direction |
|---------|-----------|-----|-----------|
| `GP0` (TX) | `GPIO16` (RX) | `UART_RX` | Pico → ESP32 |
| `GP1` (RX) | `GPIO17` (TX) | `UART_TX` | ESP32 → Pico |

### 3c. Motor Control — to TB6612FNG

| Pico GP | TB6612 Pin | Net | Function |
|---------|-----------|-----|---------|
| `GP2` | `PWM1` | `MOTOR_PWM1` | Left motor speed |
| `GP3` | `DIR1` | `MOTOR_DIR1` | Left motor direction |
| `GP4` | `PWM2` | `MOTOR_PWM2` | Right motor speed |
| `GP5` | `DIR2` | `MOTOR_DIR2` | Right motor direction |
| `3V3(OUT)` | `VCC` | `+3V3_PICO` | TB6612 logic supply |
| `GND` | `GND` | `GND` | Common GND |

> Recommended PWM frequency: **10–20 kHz** to avoid audible motor whine.

---

## 4. TB6612FNG Motor Driver

### 4a. Power

| TB6612 Pin | Connects To | Net | Note |
|-----------|-------------|-----|------|
| `VM` | Battery rail (switch output) | `+BATT` | Motor power, 7.2–8.4 V |
| `VCC` | Pico `3V3(OUT)` | `+3V3_PICO` | Logic supply — 3.3 V ONLY |
| `GND` | Common GND | `GND` | Both GND pins |

### 4b. Control Inputs

| TB6612 Pin | Pico GP | Net |
|-----------|---------|-----|
| `PWM1` | `GP2` | `MOTOR_PWM1` |
| `DIR1` | `GP3` | `MOTOR_DIR1` |
| `PWM2` | `GP4` | `MOTOR_PWM2` |
| `DIR2` | `GP5` | `MOTOR_DIR2` |
| `STBY` | `3V3` or `VCC` | Tie HIGH to enable driver |

### 4c. Motor Outputs

| TB6612 Pin | Motor | Net |
|-----------|-------|-----|
| `M1+` | Left N20 motor `[+]` | `M1P` |
| `M1−` | Left N20 motor `[−]` | `M1N` |
| `M2+` | Right N20 motor `[+]` | `M2P` |
| `M2−` | Right N20 motor `[−]` | `M2N` |

> Swap `M1+`/`M1−` (or `M2+`/`M2−`) to reverse a motor's spin direction.

---

## 5. Sharp IR Sensors (×4)

All four sensors share the same wiring pattern:

| IR Sensor Pin | Connects To | Net |
|--------------|-------------|-----|
| `VCC` | 5 V Buck OUT | `+5V` |
| `GND` | Common GND | `GND` |
| `OUT` | See table below | sensor-specific |

| Sensor | OUT → ESP32 | Net |
|--------|------------|-----|
| Left Outer | `GPIO34` | `IR_LO` |
| Left Inner | `GPIO35` | `IR_LI` |
| Right Inner | `GPIO36` | `IR_RI` |
| Right Outer | `GPIO39` | `IR_RO` |

**Decoupling (mandatory per sensor):**
- 10 µF electrolytic capacitor: VCC to GND, placed **close to sensor**
- 0.1 µF ceramic capacitor: VCC to GND, in parallel with electrolytic

---

## 6. Net Name Reference

| Net Name | Description |
|----------|-------------|
| `+BATT` | Raw battery rail post-switch (~7.2–8.4 V) |
| `+5V` | Regulated 5 V from buck converter |
| `+3V3_ESP` | ESP32 3.3 V output (powers RC522) |
| `+3V3_PICO` | Pico 3.3 V output (powers TB6612 logic) |
| `GND` | Common ground (all modules share this) |
| `UART_TX` | ESP32 GPIO17 TX → Pico GP1 RX |
| `UART_RX` | Pico GP0 TX → ESP32 GPIO16 RX |
| `IR_LO` | Left Outer IR analog output → GPIO34 |
| `IR_LI` | Left Inner IR analog output → GPIO35 |
| `IR_RI` | Right Inner IR analog output → GPIO36 |
| `IR_RO` | Right Outer IR analog output → GPIO39 |
| `I2C_SDA` | I2C data — GPIO21 ↔ VL53L1X SDA |
| `I2C_SCL` | I2C clock — GPIO22 → VL53L1X SCL |
| `SPI_SCK` | SPI clock — GPIO18 → RC522 SCK |
| `SPI_MOSI` | SPI MOSI — GPIO23 → RC522 MOSI |
| `SPI_MISO` | SPI MISO — GPIO19 ← RC522 MISO |
| `RFID_SS` | RC522 chip-select — GPIO5 → RC522 SS |
| `RFID_RST` | RC522 reset — GPIO4 → RC522 RST |
| `MOTOR_PWM1` | Left motor PWM — Pico GP2 → TB6612 PWM1 |
| `MOTOR_DIR1` | Left motor dir — Pico GP3 → TB6612 DIR1 |
| `MOTOR_PWM2` | Right motor PWM — Pico GP4 → TB6612 PWM2 |
| `MOTOR_DIR2` | Right motor dir — Pico GP5 → TB6612 DIR2 |
| `M1P` | Left motor + terminal |
| `M1N` | Left motor − terminal |
| `M2P` | Right motor + terminal |
| `M2N` | Right motor − terminal |

---

## 7. Pre-Power Checklist

- [ ] Buck converter output measured = 5.00 V ±0.1 V (no boards connected)
- [ ] All GNDs verified continuous to battery negative (multimeter continuity)
- [ ] RC522 VCC wire confirmed connected to ESP32 3V3 — NOT the 5V rail
- [ ] TB6612 VM wire confirmed connected to battery rail — NOT buck output
- [ ] TB6612 VCC wire confirmed connected to Pico 3V3 — NOT 5V rail
- [ ] TB6612 STBY pin tied HIGH (3V3 or VCC)
- [ ] All IR sensor decoupling caps installed
- [ ] UART TX/RX cross-connected (ESP32 TX → Pico RX, Pico TX → ESP32 RX)
- [ ] No encoder wires (V1 — open-loop only)
