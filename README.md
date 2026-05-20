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


