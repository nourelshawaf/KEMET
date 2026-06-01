#pragma once
#include <Arduino.h>


//  maze_types.h — ESP32
//  Direction helpers, MapNode, SensorData


enum class Dir : uint8_t { N = 0, E = 1, S = 2, W = 3 };

inline Dir turnRight(Dir d) { return static_cast<Dir>((uint8_t(d) + 1) % 4); }
inline Dir turnLeft (Dir d) { return static_cast<Dir>((uint8_t(d) + 3) % 4); }
inline Dir opposite (Dir d) { return static_cast<Dir>((uint8_t(d) + 2) % 4); }
inline const char* dirName(Dir d) {
    static const char* n[] = {"N","E","S","W"};
    return n[uint8_t(d)];
}   

//  One RFID tag = one node in the maze graph 
struct RFIDNode {
    String  uid;
    bool    wall[4]      = {true,true,true,true};  // indexed by Dir
    String  neighbour[4] = {"","","",""};
    bool    visited      = false;
    bool    isStart      = false;
    bool    isFinish     = false;

    bool   getWall(Dir d)      const { return wall[uint8_t(d)]; }
    void   setWall(Dir d, bool v)    { wall[uint8_t(d)] = v; }
    String getNeighbour(Dir d) const { return neighbour[uint8_t(d)]; }
    void   setNeighbour(Dir d, const String& u) {
        neighbour[uint8_t(d)] = u;
        wall[uint8_t(d)]      = false;   // passage exists
    }
};

//  Raw sensor snapshot 
struct SensorData {
    int      irLeftOuter;   // raw ADC (12-bit, 0-4095)
    int      irLeftInner;
    int      irRightInner;
    int      irRightOuter;
    uint16_t tofMM;

    // Convenience: true = obstacle in that zone
    bool wallFront() const;   // defined in sensor_manager.cpp
    bool wallLeft()  const;
    bool wallRight() const;
};
