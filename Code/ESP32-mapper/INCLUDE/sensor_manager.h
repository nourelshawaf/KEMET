#pragma once
#include <VL53L1X.h>
#include "maze_types.h"
#include "config.h"

// ============================================================
//  SensorManager
//  Owns: 4× Sharp IR (analog ADC) + VL53L1X ToF (I2C)
//  Returns a SensorData snapshot on demand.
// ============================================================
class SensorManager {
public:
    bool       begin();          // returns false if ToF not found
    SensorData read() const;

private:
    VL53L1X _tof;
    bool    _tofOk = false;
};
