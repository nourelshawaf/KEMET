## Final Connection Table

| Subsystem | From | To | Purpose / Notes |
|---|---|---|---|
| Power | Battery + | TB6612 VM | Motor power input |
| Power | Battery + | Buck converter IN+ | Input to 5V regulator |
| Power | Battery - | Common GND | Main ground |
| Power | Battery - | Buck converter IN- | Buck converter ground |
| Power | 5V buck OUT+ | ESP32 VIN / 5V | ESP32 power |
| Power | 5V buck OUT+ | Pico VSYS | Pico power |
| Power | 5V buck OUT+ | Sharp IR VCC | Power for all 4 IR sensors |
| Power | 5V buck OUT+ | VL53L1X VIN | Only if the module supports 5V |
| Power | 5V buck OUT- | Common GND | 5V rail ground |
| Power | Pico 3V3 | TB6612 VCC | TB6612 logic power |
| Power | ESP32 3V3 | RC522 VCC | RC522 must use 3.3V only |
| Ground | Common GND | ESP32 GND | Shared ground |
| Ground | Common GND | Pico GND | Shared ground |
| Ground | Common GND | TB6612 GND | Shared ground |
| Ground | Common GND | Sharp IR GND | Shared ground |
| Ground | Common GND | VL53L1X GND | Shared ground |
| Ground | Common GND | RC522 GND | Shared ground |
| Pico to TB6612 | Pico GP2 | TB6612 PWM1 | Motor 1 speed control |
| Pico to TB6612 | Pico GP3 | TB6612 DIR1 | Motor 1 direction |
| Pico to TB6612 | Pico GP4 | TB6612 PWM2 | Motor 2 speed control |
| Pico to TB6612 | Pico GP5 | TB6612 DIR2 | Motor 2 direction |
| Motor Output | TB6612 M1+ / M1- | Left N20 motor | Left motor output |
| Motor Output | TB6612 M2+ / M2- | Right N20 motor | Right motor output |
| ESP32 IR Sensors | IR Left Outer OUT | ESP32 GPIO34 | Analog input |
| ESP32 IR Sensors | IR Left Inner OUT | ESP32 GPIO35 | Analog input |
| ESP32 IR Sensors | IR Right Inner OUT | ESP32 GPIO36 | Analog input |
| ESP32 IR Sensors | IR Right Outer OUT | ESP32 GPIO39 | Analog input |
| ESP32 ToF | VL53L1X SDA | ESP32 GPIO21 | I2C data |
| ESP32 ToF | VL53L1X SCL | ESP32 GPIO22 | I2C clock |
| ESP32 RFID | RC522 SS / SDA | ESP32 GPIO5 | RFID chip select |
| ESP32 RFID | RC522 SCK | ESP32 GPIO18 | RFID SPI clock |
| ESP32 RFID | RC522 MOSI | ESP32 GPIO23 | RFID SPI MOSI |
| ESP32 RFID | RC522 MISO | ESP32 GPIO19 | RFID SPI MISO |
| ESP32 RFID | RC522 RST | ESP32 GPIO4 | RFID reset |
| ESP32 to Pico SPI | ESP32 GPIO14 | Pico GP18 | SPI SCK |
| ESP32 to Pico SPI | ESP32 GPIO13 | Pico GP19 | SPI MOSI |
| ESP32 to Pico SPI | ESP32 GPIO32 | Pico GP16 | SPI MISO |
| ESP32 to Pico SPI | ESP32 GPIO33 | Pico GP17 | SPI CS / SS |
| ESP32 to Pico SPI | ESP32 GND | Pico GND | Required shared ground |

## Notes

- ESP32 is the **SPI master**.
- Raspberry Pi Pico is the **SPI slave**.
- RC522 uses its own SPI pins on the ESP32.
- Pico uses a separate SPI bus on the ESP32, so there is no pin conflict.
- TB6612 **VM** is motor power.
- TB6612 **VCC** is logic power from Pico **3.3V**.
- RC522 must be powered from **3.3V only**.
- All grounds must be common.
- Start motor testing with low PWM values, around **50–80**, not full speed.
- This is a prototype connector-level wiring plan, not a verified PCB layout.
