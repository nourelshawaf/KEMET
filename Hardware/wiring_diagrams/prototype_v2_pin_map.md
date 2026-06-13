# Prototype V2 Pin Map

Status: **TBD — fill in from actual hardware before next firmware flash**

Verify each entry against the physical robot before trusting it.

---

## ESP32

| Module | Signal | ESP32 GPIO | Direction | Notes |
|--------|--------|-----------|-----------|-------|
| RC522 | SDA/SS | GPIO5 | OUT | RFID chip select |
| RC522 | SCK | GPIO18 | OUT | SPI clock |
| RC522 | MOSI | GPIO23 | OUT | SPI MOSI |
| RC522 | MISO | GPIO19 | IN | SPI MISO |
| RC522 | RST | GPIO4 | OUT | Reset |
| RC522 | 3.3V | 3V3 | PWR | 3.3 V only — never 5 V |
| VL53L1X | SDA | GPIO21 | Bidir | I2C data |
| VL53L1X | SCL | GPIO22 | OUT | I2C clock |
| Sharp IR LO | OUT | GPIO34 | IN | Left outer IR (input-only pin) |
| Sharp IR LI | OUT | GPIO35 | IN | Left inner IR (input-only pin) |
| Sharp IR RI | OUT | GPIO36 | IN | Right inner IR (input-only pin) |
| Sharp IR RO | OUT | GPIO39 | IN | Right outer IR (input-only pin) |
| Pico UART | TX | GPIO17 | OUT | ESP32 → Pico |
| Pico UART | RX | GPIO16 | IN | Pico → ESP32 |

---

## Raspberry Pi Pico

| Module | Signal | Pico GP | Direction | Notes |
|--------|--------|---------|-----------|-------|
| TB6612FNG | PWMA | GP2 | OUT | Left motor speed |
| TB6612FNG | AIN (DIR) | GP3 | OUT | Left motor direction |
| TB6612FNG | PWMB | GP4 | OUT | Right motor speed |
| TB6612FNG | BIN (DIR) | GP5 | OUT | Right motor direction |
| Left HC-89 | OUT | GP6 | IN | Left encoder interrupt |
| Right HC-89 | OUT | GP7 | IN | Right encoder interrupt |
| ESP32 UART | RX | GP1 | IN | Commands from ESP32 |
| ESP32 UART | TX | GP0 | OUT | ACK replies to ESP32 |

---

## TB6612FNG

| TB6612 Pin | Connected To | Net | Notes |
|-----------|-------------|-----|-------|
| VM | Battery rail | +BATT | Motor power, 7.2–8.4 V — NOT buck output |
| VCC | Pico 3V3(OUT) | +3V3_PICO | Logic supply — 3.3 V only |
| GND | Common GND | GND | Both GND pins |
| PWMA | Pico GP2 | MOTOR_PWM1 | Left motor |
| AIN | Pico GP3 | MOTOR_DIR1 | Left direction |
| PWMB | Pico GP4 | MOTOR_PWM2 | Right motor |
| BIN | Pico GP5 | MOTOR_DIR2 | Right direction |
| STBY | 3V3 | — | Tied HIGH permanently |
| M1+ | Left motor + | M1P | Swap M1+/M1− to reverse |
| M1− | Left motor − | M1N | |
| M2+ | Right motor + | M2P | |
| M2− | Right motor − | M2N | Right motor wires physically reversed |

---

## Power Rails

| Rail | Source | Voltage | Consumers |
|------|--------|---------|-----------|
| +BATT | Battery through switch | 7.2–8.4 V | TB6612 VM only |
| +5V | Buck converter | 5.00 V ±0.1 V | ESP32 VIN, Pico VSYS, Sharp IR VCC |
| +3V3_ESP | ESP32 internal | 3.3 V | RC522 VCC |
| +3V3_PICO | Pico internal | 3.3 V | TB6612 VCC |
| GND | Battery − | 0 V | All modules (common bus) |
