# KEMET
Autonomous maze-solving robot using ESP32/Pico control, RFID-based path detection, N20 encoder motors, and TB6612FNG motor driving. The robot records the maze route during the first run and follows the saved path in the second run for faster performance.
| Component | Selected Part | Purpose |
|---|---|---|
| Main Controller | ESP32 | Main decision-making, RFID reading, maze logic, wall-following strategy |
| Motor Controller | Raspberry Pi Pico | Motor PWM control, encoder reading, PID speed control |
| Motor Driver | TB6612FNG | Efficient dual DC motor driver for N20 motors |
| Motors | 2× N20E 12V Encoder Motors | Robot movement with encoder feedback |
| Encoder Type | Magnetic Hall-effect Quadrature Encoder | Measures motor speed, direction, and distance |
| RFID Reader | RC522 RFID Module | Reads START, STOP, LEFT, RIGHT, and DEAD-END markers |
| Distance Sensors | ToF / IR Distance Sensors | Wall-following and obstacle distance measurement |
| IMU | Gy- 521 || MPU6050 | angle correction and turn stabilization |
| Battery | 2S Li-ion | Main power source for motors and electronics |
| Voltage Regulation | Step-down converter 5V and step-up 12V | Provides stable voltage for ESP32, Pico, and sensors |
| Chassis | 2WD Robot Platform | Mechanical base of the robot |
| Wheels | Small robot wheels, approx. 32 mm | Movement and speed control |
| Caster Wheel | Ball caster  | Stability and balance |