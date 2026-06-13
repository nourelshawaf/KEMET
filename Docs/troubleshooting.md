# Troubleshooting

## Motor Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Motors do not move at all | TB6612 STBY not HIGH | Tie STBY to 3.3 V |
| Motors do not move at all | TB6612 VM not connected | Connect VM to battery rail |
| Motors do not move at all | Wrong PWM pin | Check GP2 / GP4 wiring |
| One motor does not move | One channel wiring error | Verify PWM and DIR for that channel |
| Robot moves backward | FWD/BWD direction wrong | Swap FWD/BWD defines in sketch |
| Robot spins forever | Encoder wire disconnected | Check GP6 / GP7 and HC-89 power |
| Robot curves heavily | Encoder not counting | Verify encoder wiring and power |
| Robot oscillates in straight line | Drift trim too high | Reduce trim offset from 15 |

## Encoder Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Counter never increments | ISR not triggering | Verify attachInterrupt() and pin number |
| Counter jumps by 2–4 per slot | Double-triggering | Add 100 nF cap from OUT to GND near sensor |
| Very different counts (L=30, R=5) | One encoder misaligned | Realign HC-89 disc with sensor slot |
| Counts stop mid-move | Loose encoder wire | Reseat connector |

## Power Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| ESP32 / Pico resets during motor run | Buck cannot supply peak motor current | Check buck rated current; add bypass cap |
| RC522 not detected | Powered from 5 V rail | Move VCC wire to ESP32 3V3 pin |
| IR sensor reads garbage | Missing decoupling caps | Add 10 µF + 0.1 µF per sensor |
| Erratic behaviour after wiring change | Missing GND connection | Verify all modules share common GND |

## UART / Communication Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| No data received | TX/RX not crossed | ESP32 TX → Pico RX; Pico TX → ESP32 RX |
| Garbled data | Baud rate mismatch | Both sides must be set to 115200 |
| Commands lost | No flow control | Add software ACK; Pico replies OK before next command |

## RFID Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| RC522 not initialised | SPI wiring error | Check GPIO5/18/23/19/4 wiring |
| Card not detected | RC522 on wrong voltage | Must be 3.3 V — check with multimeter |
| UID reads as all zeros | Read too fast | Add `PICC_HaltA()` + delay before next read |
