#!/usr/bin/env python3
"""
KEMET Robot V1 - EasyEDA Standard Edition Schematic Generator
=============================================================
Run:    python generate_schematic.py
Output: KEMET_V1_Schematic.json   (import into EasyEDA Standard via File → Open)

Layout (canvas 2400 × 1720 px, 10 px/grid):
  Block 1  Power Subsystem          top-left
  Block 2  ESP32 Sensing/Nav        left column
  Block 3  Raspberry Pi Pico        bottom-left
  Block 4  TB6612FNG Motor Driver   bottom-centre
  Block 5  Sensor Subsystem         right area (4× IR, ToF, RFID)
  Block 6  UART Bridge              centre floating
  Block 7  Motor Outputs            bottom-right
  Notes    Warning strip            bottom
  Title    Title block              very bottom
"""

import json

# ---------------------------------------------------------------------------
# Low-level shape helpers
# ---------------------------------------------------------------------------
shapes = []
_gid = [1]

def _gge():
    g = f"gge{_gid[0]}"
    _gid[0] += 1
    return g

def ann(x, y, text, color="#000000", size=7, bold=False, rot=0):
    """Non-electrical text annotation."""
    w = "bold" if bold else "normal"
    shapes.append(
        f"ANNOTATION~{x}~{y}~{rot}~{text}~{color}~Arial~{size}~{w}~normal~comment~{_gge()}"
    )

def netlabel(x, y, net, rot=0):
    """Electrical net label – connects same-name labels."""
    shapes.append(
        f"NETLABEL~{x}~{y}~{rot}~{net}~#0000FF~Arial~7~bold~normal~comment~{_gge()}"
    )

def wire(x1, y1, x2, y2, color="#880000"):
    """Electrical wire segment."""
    shapes.append(f"WIRE~{x1} {y1} {x2} {y2}~{color}~1~0~none~{_gge()}")

def junction(x, y):
    shapes.append(f"JUNCTION~{x}~{y}~#880000~{_gge()}")

def polyline(pts_flat, color="#000000", lw=1, fill="none"):
    """Non-electrical polyline.  pts_flat = [(x,y), ...]"""
    pts = " ".join(f"{x} {y}" for x, y in pts_flat)
    shapes.append(f"POLYLINE~{pts}~{color}~{lw}~0~{fill}~{_gge()}")

def rect_poly(x, y, w, h, color="#003366", lw=2, fill="none"):
    """Draw rectangle as closed polyline (non-electrical)."""
    polyline([(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)], color=color, lw=lw, fill=fill)

def title_bar(x, y, w, title, bg="#003366", fg="#FFFFFF"):
    """Filled title bar + white text."""
    rect_poly(x, y, w, 22, color=bg, lw=0, fill=bg)
    ann(x+5, y+5, title, color=fg, size=8, bold=True)

def block(x, y, w, h, title, border="#003366"):
    """Module block: border rectangle + filled title bar."""
    rect_poly(x, y, w, h, color=border, lw=2)
    title_bar(x, y, w, title, bg=border)

# ---------------------------------------------------------------------------
# Higher-level helpers
# ---------------------------------------------------------------------------
STUB = 30   # wire stub length in px

def pin_r(bx_right, py, label, net=None):
    """Pin stub + label on RIGHT edge of a block; optional net label outside."""
    wire(bx_right, py, bx_right + STUB, py)
    ann(bx_right - len(label)*4 - 4, py - 7, label, size=6)
    if net:
        netlabel(bx_right + STUB + 4, py - 5, net)

def pin_l(bx_left, py, label, net=None):
    """Pin stub + label on LEFT edge of a block; optional net label outside."""
    wire(bx_left - STUB, py, bx_left, py)
    ann(bx_left + 3, py - 7, label, size=6)
    if net:
        netlabel(bx_left - STUB - 65, py - 5, net)

def section_hdr(x, y, text, color="#004400"):
    ann(x, y, f"── {text} ──", color=color, size=6, bold=True)


# ===========================================================================
# BLOCK 1 — POWER SUBSYSTEM
# ===========================================================================
BX1, BY1, BW1, BH1 = 60, 50, 370, 240
block(BX1, BY1, BW1, BH1, "1. POWER SUBSYSTEM", border="#003366")

ann(BX1+10, BY1+32,  "2S Li-ion Battery Pack",           size=7, bold=True)
ann(BX1+10, BY1+48,  "7.2 V nom / 8.4 V max  (~1500 mAh suggested)", size=6, color="#555555")
ann(BX1+10, BY1+68,  "Battery [−]  ──►  Common GND",      size=6)
ann(BX1+10, BY1+84,  "Battery [+]  ──►  Main Power Switch",size=6)
ann(BX1+10, BY1+100, "Switch OUT   ──►  5 V Buck Converter IN",   size=6)
ann(BX1+10, BY1+116, "Switch OUT   ──►  TB6612 VM (motor rail)",   size=6)
ann(BX1+10, BY1+136, "5 V Buck OUT ──►  ESP32 VIN",        size=6)
ann(BX1+10, BY1+152, "5 V Buck OUT ──►  Pico VSYS",        size=6)
ann(BX1+10, BY1+168, "5 V Buck OUT ──►  Sharp IR VCC (×4)", size=6)
ann(BX1+10, BY1+184, "5 V Buck OUT ──►  VL53L1X VIN",      size=6)
ann(BX1+10, BY1+204, "⚠  Measure buck output = 5.00 V ±0.1 V BEFORE connecting boards",
    color="#CC0000", size=6, bold=True)
ann(BX1+10, BY1+220, "⚠  ALL grounds share one common reference",
    color="#CC0000", size=6, bold=True)

# Power net stubs on right edge
for py, net in [(BY1+116, "+BATT"), (BY1+152, "+5V"), (BY1+204, "GND")]:
    wire(BX1+BW1, py, BX1+BW1+STUB, py)
    netlabel(BX1+BW1+STUB+4, py-5, net)


# ===========================================================================
# BLOCK 2 — ESP32
# ===========================================================================
BX2, BY2, BW2, BH2 = 60, 340, 370, 580
block(BX2, BY2, BW2, BH2, "2. ESP32 — Sensing / Navigation", border="#003366")

# Power
section_hdr(BX2+10, BY2+32, "Power")
pin_r(BX2+BW2, BY2+48,  "VIN (5 V in)",       "+5V")
pin_r(BX2+BW2, BY2+66,  "3V3 out",            "+3V3_ESP")
pin_r(BX2+BW2, BY2+84,  "GND",                "GND")

# SPI — RC522
section_hdr(BX2+10, BY2+106, "SPI  (RC522 RFID — 3.3 V ONLY)")
pin_r(BX2+BW2, BY2+122, "GPIO5   → RFID SS",  "RFID_SS")
pin_r(BX2+BW2, BY2+140, "GPIO18  → SPI SCK",  "SPI_SCK")
pin_r(BX2+BW2, BY2+158, "GPIO23  → SPI MOSI", "SPI_MOSI")
pin_r(BX2+BW2, BY2+176, "GPIO19  → SPI MISO", "SPI_MISO")
pin_r(BX2+BW2, BY2+194, "GPIO4   → RFID RST", "RFID_RST")

# I2C — VL53L1X
section_hdr(BX2+10, BY2+216, "I2C  (VL53L1X ToF)")
pin_r(BX2+BW2, BY2+232, "GPIO21  SDA",         "I2C_SDA")
pin_r(BX2+BW2, BY2+250, "GPIO22  SCL",         "I2C_SCL")

# UART — to Pico
section_hdr(BX2+10, BY2+272, "UART  (to Raspberry Pi Pico)")
pin_r(BX2+BW2, BY2+288, "GPIO17  TX → Pico RX","UART_TX")
pin_r(BX2+BW2, BY2+306, "GPIO16  RX ← Pico TX","UART_RX")

# ADC — Sharp IR
section_hdr(BX2+10, BY2+328, "ADC  (Sharp IR Sensors)")
pin_r(BX2+BW2, BY2+344, "GPIO34  ← IR Left Outer",  "IR_LO")
pin_r(BX2+BW2, BY2+362, "GPIO35  ← IR Left Inner",  "IR_LI")
pin_r(BX2+BW2, BY2+380, "GPIO36  ← IR Right Inner", "IR_RI")
pin_r(BX2+BW2, BY2+398, "GPIO39  ← IR Right Outer", "IR_RO")

ann(BX2+10, BY2+424, "⚠  Prototype V1 — NO wheel encoders",  color="#CC0000", size=6, bold=True)
ann(BX2+10, BY2+440, "⚠  Open-loop motor control only",      color="#CC0000", size=6)
ann(BX2+10, BY2+456, "⚠  RC522 powered from 3.3 V — NEVER 5 V", color="#CC0000", size=6, bold=True)
ann(BX2+10, BY2+476, "GPIO34/35/36/39 = input-only (no internal pullup)", size=6, color="#555555")
ann(BX2+10, BY2+494, "Shared GND with Pico required for UART",            size=6, color="#555555")
ann(BX2+10, BY2+514, "I2C addr: VL53L1X = 0x29",                          size=6, color="#555555")
ann(BX2+10, BY2+532, "SPI freq: RC522 ≤ 10 MHz",                          size=6, color="#555555")
ann(BX2+10, BY2+552, "UART baud: 115200 recommended",                     size=6, color="#555555")


# ===========================================================================
# BLOCK 3 — Raspberry Pi Pico
# ===========================================================================
BX3, BY3, BW3, BH3 = 60, 970, 370, 340
block(BX3, BY3, BW3, BH3, "3. Raspberry Pi Pico — Motor Control", border="#005588")

# Power (left stubs — inputs)
section_hdr(BX3+10, BY3+32, "Power")
pin_l(BX3, BY3+48,  "VSYS  (5 V in)",   "+5V")
pin_l(BX3, BY3+66,  "GND",              "GND")
# 3V3 output goes right → TB6612
pin_r(BX3+BW3, BY3+84, "3V3 out → TB6612 VCC", "+3V3_PICO")

# UART (right stubs — connect to ESP32 via net labels)
section_hdr(BX3+10, BY3+106, "UART  (to ESP32)")
pin_r(BX3+BW3, BY3+122, "GP0  TX → ESP32 RX", "UART_RX")
pin_r(BX3+BW3, BY3+140, "GP1  RX ← ESP32 TX", "UART_TX")

# Motor control (right stubs → TB6612)
section_hdr(BX3+10, BY3+162, "Motor Control  (to TB6612FNG)")
pin_r(BX3+BW3, BY3+178, "GP2  → PWM1", "MOTOR_PWM1")
pin_r(BX3+BW3, BY3+196, "GP3  → DIR1", "MOTOR_DIR1")
pin_r(BX3+BW3, BY3+214, "GP4  → PWM2", "MOTOR_PWM2")
pin_r(BX3+BW3, BY3+232, "GP5  → DIR2", "MOTOR_DIR2")
pin_r(BX3+BW3, BY3+250, "GND  → TB6612 GND", "GND")

ann(BX3+10, BY3+278, "RP2040 core — runs motor PID loop", size=6, color="#555555")
ann(BX3+10, BY3+294, "Receives UART commands from ESP32",  size=6, color="#555555")
ann(BX3+10, BY3+310, "PWM freq: 10–20 kHz recommended",   size=6, color="#555555")
ann(BX3+10, BY3+326, "Future: encoder inputs on GP6/GP7", size=6, color="#777777")


# ===========================================================================
# BLOCK 4 — TB6612FNG Motor Driver
# ===========================================================================
BX4, BY4, BW4, BH4 = 700, 970, 360, 340
block(BX4, BY4, BW4, BH4, "4. TB6612FNG Motor Driver", border="#550055")

# Power (left — inputs)
section_hdr(BX4+10, BY4+32, "Power")
pin_l(BX4, BY4+48,  "VM   motor rail (7.2–8.4 V)", "+BATT")
pin_l(BX4, BY4+66,  "VCC  logic 3.3 V",             "+3V3_PICO")
pin_l(BX4, BY4+84,  "GND",                           "GND")

# Control inputs (left)
section_hdr(BX4+10, BY4+106, "Control Inputs  (from Pico)")
pin_l(BX4, BY4+122, "PWM1", "MOTOR_PWM1")
pin_l(BX4, BY4+140, "DIR1", "MOTOR_DIR1")
pin_l(BX4, BY4+158, "PWM2", "MOTOR_PWM2")
pin_l(BX4, BY4+176, "DIR2", "MOTOR_DIR2")

# Motor outputs (right)
section_hdr(BX4+BW4-120, BY4+198, "Motor Outputs")
pin_r(BX4+BW4, BY4+214, "M1+", "M1P")
pin_r(BX4+BW4, BY4+232, "M1−", "M1N")
pin_r(BX4+BW4, BY4+250, "M2+", "M2P")
pin_r(BX4+BW4, BY4+268, "M2−", "M2N")

ann(BX4+10, BY4+296, "⚠  VM = battery rail (8.4 V max) — NOT 5 V",  color="#CC0000", size=6, bold=True)
ann(BX4+10, BY4+312, "⚠  VCC = logic voltage from Pico 3V3 ONLY",   color="#CC0000", size=6, bold=True)
ann(BX4+10, BY4+326, "Module form-factor: Pololu or compatible",      color="#555555", size=6)


# ===========================================================================
# BLOCK 5 — SENSOR SUBSYSTEM
# ===========================================================================
BSX, BSY, BSW, BSH = 490, 50, 1400, 680
block(BSX, BSY, BSW, BSH, "5. SENSOR SUBSYSTEM", border="#004400")

# ── 5a  Sharp IR Sensors (4×) ────────────────────────────────────────────
IR_DEFS = [
    ("IR-LO", "Left Outer",  "GPIO34", "IR_LO"),
    ("IR-LI", "Left Inner",  "GPIO35", "IR_LI"),
    ("IR-RI", "Right Inner", "GPIO36", "IR_RI"),
    ("IR-RO", "Right Outer", "GPIO39", "IR_RO"),
]
IR_POSITIONS = [
    (BSX+ 20, BSY+ 70),
    (BSX+300, BSY+ 70),
    (BSX+ 20, BSY+250),
    (BSX+300, BSY+250),
]
IW, IH = 250, 150

for (ir_id, desc, gpio, net), (ix, iy) in zip(IR_DEFS, IR_POSITIONS):
    rect_poly(ix, iy, IW, IH, color="#336600", lw=2)
    ann(ix+5, iy+4,  f"Sharp GP2Y0A21 — {desc}", size=7, bold=True, color="#225500")
    ann(ix+5, iy+22, "Analog out, 10–80 cm range",        size=6, color="#555555")
    ann(ix+5, iy+42, "VCC  ──►  +5 V",                    size=6)
    ann(ix+5, iy+58, "GND  ──►  Common GND",              size=6)
    ann(ix+5, iy+74, f"OUT  ──►  ESP32 {gpio}",           size=6)
    ann(ix+5, iy+92, "⚡  10 µF cap: VCC–GND, near sensor",size=6, color="#994400", bold=True)
    ann(ix+5, iy+110,"⚡  0.1 µF ceramic in parallel",     size=6, color="#994400")
    ann(ix+5, iy+128, f"Net: {net}",                       size=6, color="#0000AA")
    # Net label stubs on right
    wire(ix+IW, iy+42, ix+IW+STUB, iy+42);  netlabel(ix+IW+STUB+4, iy+37, "+5V")
    wire(ix+IW, iy+58, ix+IW+STUB, iy+58);  netlabel(ix+IW+STUB+4, iy+53, "GND")
    wire(ix+IW, iy+74, ix+IW+STUB, iy+74);  netlabel(ix+IW+STUB+4, iy+69, net)

# ── 5b  VL53L1X ToF sensor ───────────────────────────────────────────────
TX, TY, TW, TH = BSX+590, BSY+70, 280, 175
rect_poly(TX, TY, TW, TH, color="#007700", lw=2)
ann(TX+5, TY+4,   "VL53L1X — Time-of-Flight (Front)",       size=7, bold=True, color="#006600")
ann(TX+5, TY+22,  "I2C interface, up to 4 m range",          size=6, color="#555555")
ann(TX+5, TY+40,  "VIN  ──►  +5 V  (if breakout has reg)",  size=6)
ann(TX+5, TY+57,  "       ──►  3.3 V if bare module",        size=6, color="#777777")
ann(TX+5, TY+74,  "GND  ──►  Common GND",                   size=6)
ann(TX+5, TY+91,  "SDA  ──►  ESP32 GPIO21",                  size=6)
ann(TX+5, TY+108, "SCL  ──►  ESP32 GPIO22",                  size=6)
ann(TX+5, TY+126, "I2C addr:  0x29 (default)",               size=6, color="#555555")
ann(TX+5, TY+142, "⚠  Use 3.3 V if no onboard regulator",   size=6, color="#CC0000", bold=True)
ann(TX+5, TY+158, "XSHUT / GPIO1 optional — leave NC",       size=6, color="#777777")
wire(TX+TW, TY+40,  TX+TW+STUB, TY+40);  netlabel(TX+TW+STUB+4, TY+35, "+5V")
wire(TX+TW, TY+74,  TX+TW+STUB, TY+74);  netlabel(TX+TW+STUB+4, TY+69, "GND")
wire(TX+TW, TY+91,  TX+TW+STUB, TY+91);  netlabel(TX+TW+STUB+4, TY+86, "I2C_SDA")
wire(TX+TW, TY+108, TX+TW+STUB, TY+108); netlabel(TX+TW+STUB+4, TY+103,"I2C_SCL")

# ── 5c  RC522 RFID ───────────────────────────────────────────────────────
RX, RY, RW, RH = BSX+590, BSY+280, 280, 240
rect_poly(RX, RY, RW, RH, color="#770077", lw=2)
ann(RX+5, RY+4,   "RC522 RFID Reader",                       size=7, bold=True, color="#660066")
ann(RX+5, RY+22,  "SPI interface, 13.56 MHz",                size=6, color="#555555")
ann(RX+5, RY+40,  "3.3 V  ──►  ESP32 3V3",                  size=6)
ann(RX+5, RY+57,  "GND    ──►  Common GND",                  size=6)
ann(RX+5, RY+74,  "SCK    ──►  ESP32 GPIO18",                size=6)
ann(RX+5, RY+91,  "MOSI   ──►  ESP32 GPIO23",                size=6)
ann(RX+5, RY+108, "MISO   ──►  ESP32 GPIO19",                size=6)
ann(RX+5, RY+125, "SS/SDA ──►  ESP32 GPIO5",                 size=6)
ann(RX+5, RY+142, "RST    ──►  ESP32 GPIO4",                 size=6)
ann(RX+5, RY+162, "⚠⚠  3.3 V ONLY — NEVER connect to 5 V!",size=6, color="#CC0000", bold=True)
ann(RX+5, RY+178, "5 V WILL PERMANENTLY DESTROY the RC522",  size=6, color="#CC0000", bold=True)
ann(RX+5, RY+198, "IRQ pin: optional — leave NC for polling", size=6, color="#777777")
ann(RX+5, RY+214, "SPI freq: max 10 MHz",                    size=6, color="#555555")
wire(RX+RW, RY+40,  RX+RW+STUB, RY+40);  netlabel(RX+RW+STUB+4, RY+35, "+3V3_ESP")
wire(RX+RW, RY+57,  RX+RW+STUB, RY+57);  netlabel(RX+RW+STUB+4, RY+52, "GND")
wire(RX+RW, RY+74,  RX+RW+STUB, RY+74);  netlabel(RX+RW+STUB+4, RY+69, "SPI_SCK")
wire(RX+RW, RY+91,  RX+RW+STUB, RY+91);  netlabel(RX+RW+STUB+4, RY+86, "SPI_MOSI")
wire(RX+RW, RY+108, RX+RW+STUB, RY+108); netlabel(RX+RW+STUB+4, RY+103,"SPI_MISO")
wire(RX+RW, RY+125, RX+RW+STUB, RY+125); netlabel(RX+RW+STUB+4, RY+120,"RFID_SS")
wire(RX+RW, RY+142, RX+RW+STUB, RY+142); netlabel(RX+RW+STUB+4, RY+137,"RFID_RST")


# ===========================================================================
# BLOCK 6 — UART COMMUNICATION BRIDGE
# ===========================================================================
BX6, BY6, BW6, BH6 = 490, 790, 340, 150
block(BX6, BY6, BW6, BH6, "6. UART Communication Bridge", border="#664400")

ann(BX6+10, BY6+34, "ESP32 GPIO17 TX  ──────►  Pico GP1 RX",  size=7)
ann(BX6+10, BY6+54, "ESP32 GPIO16 RX  ◄──────  Pico GP0 TX",  size=7)
ann(BX6+10, BY6+74, "Logic levels compatible (both 3.3 V).",   size=6, color="#555555")
ann(BX6+10, BY6+90, "No level-shifter required.",              size=6, color="#555555")
ann(BX6+10, BY6+108,"⚠  Shared GND is mandatory for UART",    size=6, color="#CC0000", bold=True)
ann(BX6+10, BY6+124,"Recommended baud rate: 115200",           size=6, color="#555555")

# Net label stubs on left (towards ESP32 net names)
wire(BX6, BY6+34, BX6-STUB, BY6+34); netlabel(BX6-STUB-70, BY6+29, "UART_TX")
wire(BX6, BY6+54, BX6-STUB, BY6+54); netlabel(BX6-STUB-70, BY6+49, "UART_RX")


# ===========================================================================
# BLOCK 7 — MOTOR OUTPUTS
# ===========================================================================
BX7, BY7, BW7, BH7 = 1120, 970, 280, 340
block(BX7, BY7, BW7, BH7, "7. Motor Outputs", border="#555500")

# Left motor
rect_poly(BX7+15, BY7+40, BW7-30, 110, color="#888800", lw=2)
ann(BX7+20, BY7+45,  "Left Motor  — N20 12 V / 1000 rpm",  size=7, bold=True, color="#666600")
ann(BX7+20, BY7+63,  "M1+  ──►  Motor positive terminal",  size=6)
ann(BX7+20, BY7+79,  "M1−  ──►  Motor negative terminal",  size=6)
ann(BX7+20, BY7+96,  "Driven by TB6612 CH1 (STBY tied HIGH)", size=6, color="#555555")
ann(BX7+20, BY7+112, "Swap M1+/M1− to reverse spin dir",  size=6, color="#555555")
wire(BX7, BY7+63, BX7-STUB, BY7+63); netlabel(BX7-STUB-40, BY7+58, "M1P")
wire(BX7, BY7+79, BX7-STUB, BY7+79); netlabel(BX7-STUB-40, BY7+74, "M1N")

# Right motor
rect_poly(BX7+15, BY7+175, BW7-30, 110, color="#888800", lw=2)
ann(BX7+20, BY7+180, "Right Motor — N20 12 V / 1000 rpm",  size=7, bold=True, color="#666600")
ann(BX7+20, BY7+198, "M2+  ──►  Motor positive terminal",  size=6)
ann(BX7+20, BY7+214, "M2−  ──►  Motor negative terminal",  size=6)
ann(BX7+20, BY7+231, "Driven by TB6612 CH2 (STBY tied HIGH)", size=6, color="#555555")
ann(BX7+20, BY7+247, "Swap M2+/M2− to reverse spin dir",  size=6, color="#555555")
wire(BX7, BY7+198, BX7-STUB, BY7+198); netlabel(BX7-STUB-40, BY7+193, "M2P")
wire(BX7, BY7+214, BX7-STUB, BY7+214); netlabel(BX7-STUB-40, BY7+209, "M2N")

ann(BX7+15, BY7+298, "⚠  12 V motors on 8.4 V rail is OK",  size=6, color="#CC6600")
ann(BX7+15, BY7+314, "  (derated ops — fine for prototype)",  size=6, color="#777777")
ann(BX7+15, BY7+328, "Add freewheeling diodes if no module",  size=6, color="#777777")


# ===========================================================================
# WARNING / NOTES STRIP
# ===========================================================================
NY = 1380
rect_poly(60, NY, 2260, 150, color="#CC0000", lw=2)
title_bar(60, NY, 2260,
          "⚠   IMPORTANT NOTES — READ BEFORE FIRST POWER-ON   ⚠",
          bg="#CC0000", fg="#FFFFFF")

NOTES = [
    "1.  ALL grounds (Battery −, ESP32, Pico, TB6612, all sensors) MUST connect to one single common GND node.",
    "2.  TB6612 VCC (logic supply) = 3.3 V from Pico 3V3 pin.   TB6612 VM (motor supply) = battery rail (7.2–8.4 V).",
    "3.  RC522 RFID operates on 3.3 V ONLY.  Connecting to 5 V will PERMANENTLY DESTROY the device.",
    "4.  Verify buck converter output = 5.00 V (±0.1 V) with a multimeter BEFORE connecting any board.",
    "5.  PROTOTYPE V1: No wheel encoders installed.  Motor control is open-loop, corrected by IR sensor feedback.",
    "6.  Add 10 µF electrolytic + 0.1 µF ceramic decoupling caps at each Sharp IR VCC pin (close to sensor).",
]
for i, note in enumerate(NOTES):
    ann(80, NY+28+i*18, note, size=6)


# ===========================================================================
# TITLE BLOCK
# ===========================================================================
TB_Y = 1560
rect_poly(60, TB_Y, 2260, 90, color="#000000", lw=2)
ann(80, TB_Y+8,  "KEMET  —  Autonomous Maze-Solving Robot",   size=13, bold=True)
ann(80, TB_Y+34, "Document: Full Wiring Architecture  |  Prototype V1  |  Rev 1.0  |  2025", size=8, color="#333333")
ann(80, TB_Y+54, "Engineer: KEMET Project  |  MCU: ESP32 + Raspberry Pi Pico  |  Driver: TB6612FNG  |  Motors: 2× N20 12V 1000rpm", size=7, color="#555555")
ann(80, TB_Y+70, "⚠  DEVELOPMENT / EDUCATIONAL PROTOTYPE — NOT FOR MANUFACTURE", size=7, color="#CC0000", bold=True)
ann(1900, TB_Y+8, "DO NOT", size=10, bold=True, color="#CC0000")
ann(1880, TB_Y+28,"MANUFACTURE", size=10, bold=True, color="#CC0000")


# ===========================================================================
# ASSEMBLE & WRITE JSON
# ===========================================================================
schematic = {
    "head": {
        "type": 1,
        "title": "KEMET Robot V1 — Full Wiring Architecture",
        "description": (
            "Autonomous maze-solving robot Prototype V1. "
            "ESP32 (sensing/navigation) + Raspberry Pi Pico (motor control) via UART. "
            "TB6612FNG dual motor driver. 2× N20 12V 1000rpm motors. "
            "Sensors: 4× Sharp IR (analog), VL53L1X ToF (I2C), RC522 RFID (SPI). "
            "Power: 2S Li-ion → buck converter → 5V rail. "
            "No encoders. Open-loop + IR wall correction."
        ),
        "docType": "5",
        "schematicType": 0,
        "origin": "0,0"
    },
    "canvas": "CA~0~0~#FFFFFF~yes~#CCCCCC~10~2400~1720~line~10~pixel~5~0~0",
    "shape": shapes,
    "BBox": {"x": 0, "y": 0, "width": 2400, "height": 1720}
}

output_path = "KEMET_V1_Schematic.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(schematic, f, indent=2, ensure_ascii=False)

print(f"OK  Written:  {output_path}")
print(f"   Shapes:   {len(shapes)}")
types = sorted(set(s.split('~')[0] for s in shapes))
print(f"   Types:    {', '.join(types)}")
print()
print("Import into EasyEDA Standard Edition:")
print("   File -> Open EESchema -> select KEMET_V1_Schematic.json")
