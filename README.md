# KEMET

Autonomous maze-solving robot designed for the Óbuda University Labyrinth Competition.

The robot combines:
- RFID-guided navigation
- wall-following algorithms
- distributed embedded control
- Webots simulation
- autonomous maze solving

The system is currently developed as modular subsystems using ESP32 and Raspberry Pi Pico microcontrollers. The robot follows maze walls using IR and ToF sensing, detects navigation markers using RFID, and aims to optimize maze traversal speed through path memorization and second-run optimization.

Current prototype focus:
- qualification track completion
- stable wall-following
- open-loop motor control with sensor-based correction
- subsystem integration and validation

| Component | Selected Part | Purpose |
|---|---|---|
| Main Controller | ESP32 | Main decision-making, RFID reading, maze logic, wall-following strategy |
| Motor Controller | Raspberry Pi Pico | Motor PWM control, encoder reading, PID speed control |
| Motor Driver | TB6612FNG | Efficient dual DC motor driver for N20 motors |
| Motors | 2× N20E 12V 1000 rpm Encoder Motors | Robot movement with encoder feedback |
| Encoder Type | Magnetic Hall-effect Quadrature Encoder | Measures motor speed, direction, and distance |
| RFID Reader | RC522 RFID Module | Reads START, STOP, LEFT, RIGHT, and DEAD-END markers |
| Distance Sensors | ToF (VL53L1X) / IR Distance Sensors | Wall-following and obstacle distance measurement |
| IMU | Gy- 521 || MPU6050 | angle correction and turn stabilization |
| Battery | 2S Li-ion | Main power source for motors and electronics |
| Voltage Regulation | Step-down converter 5V and step-up 12V | Provides stable voltage for ESP32, Pico, and sensors |
| Chassis |Universal PCB design| Mechanical base of the robot |
| Wheels | Small robot wheels, approx. 32 mm | Movement and speed control |
| Caster Wheel | Ball caster  | Stability and balance |
--------------------------------------------------------------------------------------------------------------------------
## Day 1 – Prototype Development Update

The first day of development focused on building the initial hardware prototype of **KEMET**, our autonomous maze-solving robot for the Óbuda University Labyrinth Competition. The core chassis was assembled on a universal PCB platform, integrating the ESP32, Raspberry Pi Pico, RFID module, power regulation system, battery pack, and initial sensor layout. Early prototyping concentrated on validating subsystem integration, power distribution, and mechanical stability while preparing the platform for wall-following and navigation testing. Initial bring-up confirmed successful power delivery and basic hardware communication, establishing a solid foundation for future motor control, sensor calibration, and autonomous maze-solving development.

<img width="920" height="1024" alt="Mazer Runner" src="https://github.com/user-attachments/assets/918c590f-e338-48ba-94ac-6212cc0694cc" />

