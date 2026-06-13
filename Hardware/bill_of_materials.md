# Bill of Materials — KEMET Prototype V1

| # | Component | Part Number / Model | Qty | Notes |
|---|-----------|-------------------|-----|-------|
| 1 | Main controller | ESP32 ESP-WROOM-32 | 1 | Navigation, sensing, RFID |
| 2 | Motor controller | Raspberry Pi Pico | 1 | PWM, encoder counting |
| 3 | Motor driver | TB6612FNG breakout | 1 | Dual channel, 3.3 V logic |
| 4 | DC gear motor | N20-style, Ø 37 mm wheel | 2 | |
| 5 | Wheel encoder | HC-89 optical sensor | 2 | 35 pulses/rev measured |
| 6 | RFID reader | RC522 module | 1 | 3.3 V only |
| 7 | Front ToF sensor | VL53L1X breakout | 1 | I2C, front wall detection |
| 8 | Side IR sensor | Sharp GP2Y0A51SK0F | 4 | Analog, 5 V supply |
| 9 | Battery | 2S Li-ion pack | 1 | ~7.2–8.4 V nominal |
| 10 | Buck converter | 5 V step-down module | 1 | Min 2 A rated |
| 11 | Power switch | Inline rocker switch | 1 | 20 AWG rated |
| 12 | Decoupling cap | 10 µF electrolytic | 4 | One per Sharp IR sensor |
| 13 | Decoupling cap | 0.1 µF ceramic | 4 | One per Sharp IR sensor |
| 14 | Wiring | 20 AWG silicone wire | — | Power rails |
| 15 | Wiring | 26–28 AWG signal wire | — | Data lines |
