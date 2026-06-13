# Electronics & Power System

## Purpose

Documents the power subsystem design, voltage rails, current budgets, and wiring safety rules.

## Hardware Used

- 2S Li-ion battery (~7.2–8.4 V nominal range)
- Main power switch (inline, 20 AWG minimum)
- Step-down (buck) converter — output: 5.00 V regulated
- TB6612FNG VM rail (motor power, direct from battery)

## Voltage Rails

| Rail | Source | Voltage | Consumers |
|------|--------|---------|-----------|
| `+BATT` | Battery through switch | 7.2–8.4 V | TB6612 VM only |
| `+5V` | Buck converter output | 5.00 V ±0.1 V | ESP32 VIN, Pico VSYS, Sharp IR VCC |
| `+3V3_ESP` | ESP32 internal regulator | 3.3 V | RC522 VCC |
| `+3V3_PICO` | Pico internal regulator | 3.3 V | TB6612 VCC (logic supply) |
| `GND` | Battery negative | 0 V | All modules, common bus |

## Pre-Power Checklist

- [ ] Buck output measured = **5.00 V ±0.1 V** before connecting any board
- [ ] All GNDs verified continuous to battery negative (multimeter continuity)
- [ ] RC522 VCC confirmed on ESP32 3V3 — NOT the 5 V rail
- [ ] TB6612 VM confirmed on battery rail — NOT buck output
- [ ] TB6612 VCC confirmed on Pico 3V3 — NOT 5 V rail
- [ ] TB6612 STBY pin tied HIGH (3.3 V or VCC)
- [ ] All Sharp IR decoupling capacitors installed (10 µF + 0.1 µF per sensor)
- [ ] UART TX/RX cross-connected (ESP32 TX → Pico RX, Pico TX → ESP32 RX)

## Decoupling Requirements

Each Sharp IR sensor requires two capacitors placed close to the sensor:
- 10 µF electrolytic: VCC to GND
- 0.1 µF ceramic: VCC to GND (in parallel)

Without decoupling, motor switching noise corrupts ADC readings.

## Safety Rules

> **RC522:** 3.3 V ONLY. 5 V permanently destroys the chip.

> **TB6612 VM vs VCC:** VM is motor power (battery voltage). VCC is logic supply (3.3 V). Do not swap.

> **Buck converter:** Never power boards before verifying 5.00 V output.

> **Common GND:** All subsystems must share one GND reference. A missing GND causes erratic or non-functional behaviour.

## Current Status

Power system is wired on Prototype V1. Buck output verified at 5 V. Full load test not yet performed.

## Known Problems

- Motor current draw under stall not measured yet. Buck converter rating must be verified against actual motor current.

## Next Steps

- Measure motor current draw at BASE_PWM = 160 under loaded conditions.
- Add main fuse inline with battery positive.
