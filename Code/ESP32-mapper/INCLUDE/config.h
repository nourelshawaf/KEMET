#pragma once
//  config.h — ESP32 Maze Mapper
//  Single source of truth for all pins, bus settings and
//  tuning constants. Edit ONLY this file.

//  VSPI bus — RC522 RFID 
//  (VSPI hardware defaults: SCK=18 MOSI=23 MISO=19)
static constexpr int  RFID_SS_PIN   = 5;
static constexpr int  RFID_RST_PIN  = 4;
// SCK=18, MOSI=23, MISO=19  (hardware VSPI — no define needed)

//  HSPI bus — SPI to Pico (ESP32 = master) 
static constexpr int  PICO_SCK_PIN  = 14;   // ESP32 GPIO14 → Pico GP18
static constexpr int  PICO_MOSI_PIN = 13;   // ESP32 GPIO13 → Pico GP19
static constexpr int  PICO_MISO_PIN = 32;   // ESP32 GPIO32 ← Pico GP16
static constexpr int  PICO_CS_PIN   = 33;   // ESP32 GPIO33 → Pico GP17
static constexpr long PICO_SPI_FREQ = 1000000; // 1 MHz — safe for wires

//  I2C — VL53L1X ToF
//  (I2C hardware defaults: SDA=21, SCL=22)
static constexpr uint16_t TOF_WALL_MM    = 150;  // wall if distance < this
static constexpr uint32_t TOF_TIMEOUT_MS = 500;

//  IR sensors  Sharp analog (GPIO 34/35/36/39 input-only) 
static constexpr int  IR_LEFT_OUTER  = 34;
static constexpr int  IR_LEFT_INNER  = 35;
static constexpr int  IR_RIGHT_INNER = 36;
static constexpr int  IR_RIGHT_OUTER = 39;
// ADC threshold: readings below this = obstacle detected
// Sharp GP2Y0A21 at ~3 cm gives ~2500 ADC counts (12-bit)
static constexpr int  IR_THRESHOLD   = 1800;

//  Special RFID tag UIDs
//  Read your tags first with MFRC522 DumpInfo, paste hex here
static constexpr char START_UID[]   = "A1B2C3D4";
static constexpr char FINISH_UID[]  = "DEADBEEF";

//  Timing
static constexpr uint32_t TAG_SETTLE_MS  = 300;  // pause before reading sensors
static constexpr uint32_t INTER_CMD_MS   = 80;
static constexpr uint32_t LOOP_DELAY_MS  = 40;

//  Map
static constexpr uint8_t  MAX_NODES      = 64;
