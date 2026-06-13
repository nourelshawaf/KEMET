# RFID Navigation

## Purpose

The ESP32 reads RC522 RFID tags placed at maze intersections. Each tag encodes a navigation command. The ESP32 decodes the UID, maps it to a command, and relays the movement instruction to the Pico over UART.

## Hardware Used

- ESP32 (ESP-WROOM-32)
- RC522 RFID reader module (3.3 V only)
- RFID tags/cards with unique UIDs

## Pin Connections

| ESP32 GPIO | RC522 Pin | Net |
|-----------|-----------|-----|
| GPIO5 | SDA / SS | RFID_SS |
| GPIO18 | SCK | SPI_SCK |
| GPIO23 | MOSI | SPI_MOSI |
| GPIO19 | MISO | SPI_MISO |
| GPIO4 | RST | RFID_RST |
| 3V3 | 3.3V | Power |
| GND | GND | GND |

> RC522 must be powered from 3.3 V ONLY. 5 V permanently destroys the chip.

## UID-to-Command Mapping

UIDs must be measured from the actual cards used and stored in firmware:

| UID | Command | Robot Action |
|-----|---------|-------------|
| TBD | START | Begin run |
| TBD | STOP | End run |
| TBD | LEFT | Turn left |
| TBD | RIGHT | Turn right |
| TBD | DEAD END | U-turn |

## Software Logic

1. Poll for card presence using MFRC522 library `PICC_IsNewCardPresent()`.
2. Read UID with `PICC_ReadCardSerial()`.
3. Look up UID in the command table.
4. Send the corresponding command string to Pico over UART.
5. Wait for `OK\n` response from Pico before reading next card.

## Current Status

Not yet implemented. Phase 4 work. RC522 hardware is connected but code is not written.

## Known Problems

- UID table is empty — cards have not been measured yet.
- Reading speed at driving velocity is unknown; may need robot to slow down before tag.

## Next Steps

- Read and print UIDs for each navigation card.
- Build the UID → command lookup table in firmware.
- Test RFID reading reliability while stationary.
- Test reading while moving at Phase 1 drive speed.
