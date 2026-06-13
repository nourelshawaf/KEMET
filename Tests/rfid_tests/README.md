# RFID Tests

Purpose: verify the RC522 can reliably read all navigation cards and map UIDs to the correct commands.

## What to Record Per Session

| Field | Description |
|-------|-------------|
| Date | YYYY-MM-DD |
| Card | Which tag (START / STOP / LEFT / RIGHT / DEAD END) |
| UID read | Hex bytes printed by firmware |
| Read distance | mm from sensor to card |
| Read speed | Stationary / slow / fast |
| Success rate | Reads / attempts |

## Required Before Navigation Testing

- [ ] All card UIDs measured and recorded
- [ ] UID → command lookup table complete in firmware
- [ ] Read tested at robot's normal driving speed

## File Naming

`YYYY-MM-DD_rfid_uid_mapping.md` or `YYYY-MM-DD_rfid_speed_test.md`
