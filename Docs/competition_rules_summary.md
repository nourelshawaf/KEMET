# Competition Rules Summary

Only the rules that directly affect engineering decisions are listed here.

## Robot Size Constraint

- Maximum: `280 × 280 × 150 mm`
- The robot must fit through the maze corridor at any heading.

## Autonomy Requirement

- The robot must move autonomously after the start signal.
- No remote control, no wireless commands during the run.
- No external computing — all logic runs on the robot.

## Navigation Markers

RFID tags (or pictograms) are placed at intersections and decision points.

| Marker | Robot Action |
|--------|-------------|
| `START` | Begin run |
| `STOP` | End run, stop robot |
| `LEFT` | Turn left at next intersection |
| `RIGHT` | Turn right at next intersection |
| `DEAD END` | U-turn |

The robot must be able to read the marker and execute the corresponding movement.

## Maze Physical Dimensions

- Corridor width: `28.5 ± 1 cm`
- Wall height: `15 cm`
- Wall thickness: `15 mm`
- Floor material: OSB

## Qualification Tasks

1. **Straight track** — robot must drive a straight corridor without hitting walls.
2. **Curved track** — robot must navigate a curved corridor, following the wall.

Both qualification tasks must be completed before the main maze run.

## Engineering Implications

| Rule | Impact on Design |
|------|-----------------|
| 280 mm max width | Robot chassis must be narrower than corridor; leaves ~4–5 cm margin |
| Autonomous only | No Bluetooth/WiFi during run; ESP32 Wi-Fi kept off |
| RFID navigation | RC522 reader required; reading must be reliable at driving speed |
| Straight + curve quals | Wall-following must work before maze logic is needed |
| Dead end handling | U-turn (180°) movement must be implemented and calibrated |
