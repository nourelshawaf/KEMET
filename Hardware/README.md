# Hardware

## Current Prototype Version

**Prototype V2** — see [`Docs/prototypes/prototype_v2.md`](../Docs/prototypes/prototype_v2.md)

## Files

| File | Description |
|------|-------------|
| `bill_of_materials.md` | Full component list |
| `wiring_diagrams/KEMET_V1_Wiring_Table.md` | Pin-to-pin wiring table (V1) |
| `wiring_diagrams/prototype_v2_pin_map.md` | Pin map for Prototype V2 |
| `schematics/KEMET_V1_Schematic.json` | EasyEDA schematic (import directly) |
| `schematics/generate_schematic.py` | Script to regenerate JSON from source |

## Critical Electrical Rules

1. **RC522 is 3.3 V ONLY.** Connecting to 5 V permanently destroys the chip.
2. **ESP32 and Pico must share a common GND.** A missing GND reference causes erratic behaviour.
3. **TB6612 VM must connect to the battery rail, NOT the buck converter output.** Motor current will overdraw the buck.
4. **TB6612 VCC must connect to Pico 3V3, NOT the 5 V rail.** Logic supply must match Pico drive voltage.
5. **All Sharp IR sensors need decoupling capacitors** (10 µF + 0.1 µF per sensor) to suppress motor switching noise on ADC reads.
6. **Buck converter output must be verified at 5.00 V ±0.1 V** before connecting any board.

## Prototype History

- [Prototype V1](../Docs/prototypes/prototype_v1.md)
- [Prototype V2](../Docs/prototypes/prototype_v2.md)
