# Prototype V2

## Overview

Prototype V2 is the current breadboard-based hardware integration version of KEMET. It combines the motor platform, encoder feedback, power system, ESP32/Pico control architecture, RFID reader, and distance sensors into one testable robot body. The primary goal of this version is to validate all subsystems together before moving to soldered protoboard or PCB.

## Main Visible Components

- Raspberry Pi Pico (motor controller, top rear)
- ESP32 (navigation controller, left side)
- RC522 RFID reader (mounted rear/top for tag detection testing)
- 2× HC-89 optical encoder modules (mounted near motor wheels)
- Front-mounted DC-DC power regulation module (buck converter)
- 2-cell Li-ion battery holder (front-bottom)
- Breadboard-based temporary wiring (full chassis width)
- 2WD robot chassis (MDF/laser-cut, yellow wheels)
- Sharp IR sensor visible on right side (wall sensing)

## Changes from Prototype V1

- Full electronics placed on the robot chassis (V1 had partial placement)
- Battery and power converter repositioned to front of chassis
- Encoder sensors mounted and wired to motor shafts
- RFID reader mounted and wired at rear for detection testing
- More sensors integrated into the main breadboard layout

## Current Status

Prototype V2 is suitable for:
- Firmware testing
- Motor and encoder calibration
- RFID detection tests
- Encoder counting verification
- Power system load testing

It is **not yet final competition hardware** because:
- Wiring is temporary breadboard/jumper-based
- Component height not yet verified against 150 mm competition limit
- Full robot dimensions not yet measured
- Wiring is mechanically exposed to vibration during turns

## Known Issues

- Jumper wires may move during turns, causing intermittent encoder or sensor faults.
- Long signal wires routed alongside power wires may pick up motor switching noise.
- Breadboard connections are not reliable under repeated vibration.
- Wiring is difficult to inspect from photos alone — needs a labeled diagram.
- Power wiring not yet separated from signal wiring.

## Required Next Improvements

- [ ] Measure full robot dimensions (L × W × H) against 280 × 280 × 150 mm limit
- [ ] Replace breadboard wiring with soldered protoboard or PCB
- [ ] Add strain relief on battery and motor wires
- [ ] Document exact pin map for this prototype version in `Hardware/wiring_diagrams/prototype_v2_pin_map.md`
- [ ] Add decoupling capacitors to all Sharp IR sensors
- [ ] Separate power and signal wire routing physically

## Photos

![Prototype V2 front overview](../../Media/photos/prototype_v2/prototype_v2_front_overview.jpg)
*Front overview of Prototype V2 showing battery position, front power module, HC-89 encoder sensors, main breadboard wiring, Pico controller, and rear RFID reader placement.*

![Prototype V2 top overview](../../Media/photos/prototype_v2/prototype_v2_top_overview.jpg)
*Top view of Prototype V2 showing component layout and temporary breadboard-based wiring before protoboard cleanup.*

![Prototype V2 side power system](../../Media/photos/prototype_v2/prototype_v2_side_power_system.jpg)
*Side view of Prototype V2 showing battery holder, DC-DC converter module, wiring route, and sensor/controller stacking.*
