# KEMET Robot V1 — Schematic Files

This folder contains the full wiring architecture schematic for **KEMET Prototype V1**,
an autonomous maze-solving robot.

---

## Files

| File | Purpose |
|------|---------|
| `KEMET_V1_Schematic.json` | EasyEDA Standard Edition schematic (import directly) |
| `generate_schematic.py` | Python script that regenerates the JSON from source |
| `KEMET_V1_Wiring_Table.md` | Complete pin-to-pin wiring table with net names |
| `README.md` | This file |

---

## How to Open in EasyEDA Standard Edition

### Method 1 — Direct file open (recommended)

1. Open [EasyEDA Standard Edition](https://easyeda.com/editor) in your browser,
   or the desktop app.
2. Click **File → Open** (or press `Ctrl+O`).
3. Select `KEMET_V1_Schematic.json`.
4. The schematic opens immediately — no library installation required.

> **Note:** EasyEDA Standard Edition is the free web/desktop tool at easyeda.com.
> Do **not** use EasyEDA Pro — the JSON format is different and not compatible.

### Method 2 — Import into an existing project

1. Open your project in EasyEDA Standard.
2. Right-click the project in the left panel → **Import**.
3. Select `KEMET_V1_Schematic.json`.

---

## How to Regenerate the JSON

If you edit `generate_schematic.py` (e.g. to add a component or change a layout),
re-run it to produce a fresh `KEMET_V1_Schematic.json`:

```bash
cd KEMET/schematics
python generate_schematic.py
```

Requires Python 3.6+ with no external dependencies.

---

## Schematic Layout

```
+------------------+  +------------------------------------------+
|  1. POWER        |  |        5. SENSOR SUBSYSTEM                |
|  2S Li-ion       |  |  4x Sharp IR | VL53L1X ToF | RC522 RFID  |
|  Buck 5V reg     |  |                                           |
+------------------+  +------------------------------------------+
+------------------+      +--------------------+
|  2. ESP32        |      |  6. UART BRIDGE     |
|  Navigation/     |      |  ESP32 ↔ Pico       |
|  Sensing         |      +--------------------+
+------------------+
+------------------+  +------------------+  +------------------+
|  3. Pico         |  |  4. TB6612FNG    |  |  7. MOTORS        |
|  Motor Control   |  |  Motor Driver    |  |  2x N20 12V      |
+------------------+  +------------------+  +------------------+

+------------------------------------------------------------------+
|  WARNING NOTES                                                   |
+------------------------------------------------------------------+
|  TITLE BLOCK                                                     |
+------------------------------------------------------------------+
```

---

## Key Design Decisions

| Decision | Reason |
|----------|--------|
| ESP32 handles all sensors | ESP32 has hardware SPI, I2C, and multiple ADC channels |
| Pico handles all motors | Dedicated PWM hardware; keeps latency predictable |
| UART inter-board link | Simple, reliable; sufficient bandwidth for V1 commands |
| 5 V for Sharp IR sensors | Sensors spec'd for 4.5–5.5 V; better range accuracy at 5 V |
| 3.3 V for RC522 | RC522 is a 3.3 V device; 5 V destroys it |
| Battery → TB6612 VM direct | Motor voltage should not pass through the 5 V buck |
| Pico 3V3 → TB6612 VCC | TB6612 logic supply must match Pico's drive voltage |
| No encoders (V1) | Simplifies wiring; wall-correction via IR sensors instead |

---

## Prototype V1 Limitations

- **No wheel encoders** — speed/position is not measured
- **Open-loop motor control** — corrected by IR sensor wall distance only
- **No STBY control** — TB6612 STBY pin should be tied permanently HIGH (3.3 V)
- **No fault detection** — TB6612 fault output not connected

---

## Schematic Shape Types Used

EasyEDA Standard Edition shape types present in the JSON:

| Type | Purpose |
|------|---------|
| `POLYLINE` | Non-electrical module outlines and title bars |
| `ANNOTATION` | All text labels, pin names, warnings |
| `NETLABEL` | Electrical net connections (same name = same net) |
| `WIRE` | Electrical pin stub wires |

> Electrical connections are made entirely through **matching NETLABEL names**.
> No long crossing wires — the schematic is readable at any zoom level.

---

## Safety Warnings

> **RC522:** 3.3 V ONLY — connecting to 5 V will permanently destroy the chip.

> **TB6612 VM vs VCC:** VM is the motor power rail (battery voltage).
> VCC is the logic supply (3.3 V from Pico). They must NOT be swapped.

> **Buck converter:** Always verify 5.00 V output before connecting boards.

> **Common GND:** All subsystems (ESP32, Pico, TB6612, all sensors, battery negative)
> must share one common ground reference.
