# Wall Following

## Purpose

The robot uses four Sharp IR sensors and one front-facing ToF sensor to detect walls, correct lateral drift, and stop before hitting obstacles.

## Hardware Used

- 4× Sharp GP2Y0A51SK0F analog IR sensors (left outer, left inner, right inner, right outer)
- VL53L1X Time-of-Flight sensor (front, I2C)
- ESP32 ADC (GPIO34, GPIO35, GPIO36, GPIO39)

## Pin Connections

| ESP32 GPIO | Sensor | Net |
|-----------|--------|-----|
| GPIO34 | Left Outer IR OUT | IR_LO |
| GPIO35 | Left Inner IR OUT | IR_LI |
| GPIO36 | Right Inner IR OUT | IR_RI |
| GPIO39 | Right Outer IR OUT | IR_RO |
| GPIO21 | VL53L1X SDA | I2C_SDA |
| GPIO22 | VL53L1X SCL | I2C_SCL |

All Sharp IR VCC → +5V rail. All Sharp IR GND → common GND.
Decoupling required: 10 µF + 0.1 µF per sensor.

## Software Logic

**Lateral correction (planned):**
- Read left and right inner IR distance values.
- Compute error: `error = IR_LI - IR_RI`.
- Send trim command to Pico if error exceeds threshold: slow down one motor slightly.

**Front wall stop (planned):**
- Read VL53L1X distance continuously while moving.
- If distance < `WALL_STOP_MM`, send `STOP` to Pico immediately.
- This prevents the robot from hitting a dead-end wall before RFID detects DEAD END.

**Corridor detection (planned):**
- If both left IR and right IR read near-wall distances, robot is in a corridor — use lateral correction.
- If one side reads open, robot is at an intersection — use RFID command.

## Calibration

- Wall distance threshold `WALL_STOP_MM`: TBD (depends on corridor width and sensor mounting position).
- IR balance point (desired left/right difference = 0): depends on robot centering in corridor.

## Current Status

Not implemented. Phase 3 (ToF stop) and later (IR wall following) are planned.

## Known Problems

- Sharp IR sensors have nonlinear output voltage curves. ADC values must be mapped to mm using the datasheet curve or empirical calibration.
- ESP32 ADC has known non-linearity at the high end (>3.1 V). Use voltage dividers or characterise the ADC before relying on distance values.

## Next Steps

- Wire all four IR sensors and read raw ADC values.
- Map ADC voltage to distance using the Sharp datasheet characteristic curve.
- Implement front wall stop using VL53L1X.
- Implement lateral correction loop.
