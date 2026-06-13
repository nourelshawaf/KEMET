// =============================================================================
//  KEMET Robot — Raspberry Pi Pico
//  Phase 1: Standalone Motor + Encoder Calibration
//
//  Sequence on each loop: Straight → Right → Right → Left → Left
//
//  Open Serial Monitor at 115200 baud.
//  Read the printed pulse counts after each move.
//  Adjust TURN_90_PULSES until each turn visually lands at exactly 90°.
//  Adjust BASE_PWM / TURN_PWM if motors stall or overshoot.
//
//  Hardware assumptions:
//    - TB6612FNG breakout with single DIR pin per channel (handles AIN1/AIN2 inversion).
//    - TB6612 STBY pin is tied HIGH on the breakout or externally.
//    - Right motor wires physically reversed → both motors use same DIR logic.
//    - HC-89 encoders output 35 pulses per full wheel revolution (measured).
//    - Encoder output is active-high; INPUT_PULLUP used for safety.
// =============================================================================

#include "Arduino.h"

// ─── CALIBRATION CONSTANTS ────────────────────────────────────────────────────
// Change these to tune movement. Everything else stays fixed once verified.

static const int BASE_PWM        = 160; // Straight speed   (0–255). Start here; raise if motors stall.
static const int TURN_PWM        = 130; // Turn speed        (0–255). Lower = more accurate, more time.
static const int STRAIGHT_PULSES =  70; // ~2 revolutions forward ≈ 23 cm. Scale to your corridor.
static const int TURN_90_PULSES  =  28; // Pulses per wheel for 90° pivot. Tune by observation.
                                        // Math: π×115/4 ÷ (π×37) × 35 ≈ 27.2 → start at 28.

// ─── PIN DEFINITIONS ──────────────────────────────────────────────────────────
// Left motor  — TB6612 Channel A
static const uint8_t PWM_L = 2;  // GP2 → TB6612 PWMA
static const uint8_t DIR_L = 3;  // GP3 → TB6612 AIN (direction)

// Right motor — TB6612 Channel B (motor wires physically reversed)
static const uint8_t PWM_R = 4;  // GP4 → TB6612 PWMB
static const uint8_t DIR_R = 5;  // GP5 → TB6612 BIN (direction)

// HC-89 encoder outputs
static const uint8_t ENC_L = 6;  // GP6 ← Left  HC-89 OUT
static const uint8_t ENC_R = 7;  // GP7 ← Right HC-89 OUT

// Direction convention (applies to BOTH motors after physical reversal of right motor):
//   HIGH (FWD) → wheel spins to push robot forward
//   LOW  (BWD) → wheel spins to push robot backward
static const bool FWD = HIGH;
static const bool BWD = LOW;

// ─── ENCODER STATE ────────────────────────────────────────────────────────────
// volatile: modified in ISRs, read in main loop.
volatile uint32_t pulseL = 0;
volatile uint32_t pulseR = 0;

void isrLeft()  { pulseL++; }
void isrRight() { pulseR++; }

// ─── LOW-LEVEL MOTOR HELPERS ──────────────────────────────────────────────────

void resetCounters() {
    noInterrupts();
    pulseL = 0;
    pulseR = 0;
    interrupts();
}

void setLeft(int pwm, bool dir) {
    digitalWrite(DIR_L, dir);
    analogWrite(PWM_L, pwm);
}

void setRight(int pwm, bool dir) {
    digitalWrite(DIR_R, dir);
    analogWrite(PWM_R, pwm);
}

void stopAll() {
    analogWrite(PWM_L, 0);
    analogWrite(PWM_R, 0);
}

// Print last move's pulse counts — call immediately after a motion completes.
void printPulses(const char* label) {
    Serial.print("  ");
    Serial.print(label);
    Serial.print(" → L=");
    Serial.print(pulseL);
    Serial.print("  R=");
    Serial.print(pulseR);
    Serial.print("  avg=");
    Serial.println((pulseL + pulseR) / 2);
}

// ─── MOTION PRIMITIVES ────────────────────────────────────────────────────────
// All primitives: reset counters → drive → wait for pulse target → stop.
// Pulse condition uses average of both wheels to handle minor speed imbalance.

void goStraight(int targetPulses) {
    resetCounters();
    setLeft(BASE_PWM, FWD);
    setRight(BASE_PWM, FWD);
    // Spin-wait — acceptable for Phase 1 calibration.
    while (((pulseL + pulseR) / 2) < (uint32_t)targetPulses) { /* wait */ }
    stopAll();
    delay(200);  // Brief motor settle before reading Serial.
}

// Pivot RIGHT in place: left wheel forward, right wheel backward.
// Robot rotates clockwise when viewed from above.
void pivotRight() {
    resetCounters();
    setLeft(TURN_PWM, FWD);
    setRight(TURN_PWM, BWD);
    while (((pulseL + pulseR) / 2) < (uint32_t)TURN_90_PULSES) { /* wait */ }
    stopAll();
    delay(300);
}

// Pivot LEFT in place: left wheel backward, right wheel forward.
// Robot rotates counter-clockwise when viewed from above.
void pivotLeft() {
    resetCounters();
    setLeft(TURN_PWM, BWD);
    setRight(TURN_PWM, FWD);
    while (((pulseL + pulseR) / 2) < (uint32_t)TURN_90_PULSES) { /* wait */ }
    stopAll();
    delay(300);
}

// ─── SETUP ────────────────────────────────────────────────────────────────────
void setup() {
    Serial.begin(115200);
    delay(2000);  // Wait for USB Serial and power rails to stabilise.

    // Motor pins
    pinMode(PWM_L, OUTPUT);
    pinMode(DIR_L, OUTPUT);
    pinMode(PWM_R, OUTPUT);
    pinMode(DIR_R, OUTPUT);
    stopAll();    // Ensure motors are off at boot.

    // Encoder pins — INPUT_PULLUP covers open-collector HC-89 outputs.
    pinMode(ENC_L, INPUT_PULLUP);
    pinMode(ENC_R, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(ENC_L), isrLeft,  RISING);
    attachInterrupt(digitalPinToInterrupt(ENC_R), isrRight, RISING);

    Serial.println("====================================");
    Serial.println("  KEMET Phase 1 — Motor Calibration");
    Serial.println("====================================");
    Serial.print("  BASE_PWM=");       Serial.println(BASE_PWM);
    Serial.print("  TURN_PWM=");       Serial.println(TURN_PWM);
    Serial.print("  STRAIGHT_PULSES=");Serial.println(STRAIGHT_PULSES);
    Serial.print("  TURN_90_PULSES="); Serial.println(TURN_90_PULSES);
    Serial.println("  Sequence: Straight → R → R → L → L");
    Serial.println("  Starting in 3 s ...");
    delay(3000);
}

// ─── MAIN LOOP ────────────────────────────────────────────────────────────────
void loop() {
    Serial.println("\n--- Begin sequence ---");

    // 1. Move straight
    Serial.println("[1] Straight");
    goStraight(STRAIGHT_PULSES);
    printPulses("straight");
    delay(500);

    // 2. First right turn
    Serial.println("[2] Turn RIGHT");
    pivotRight();
    printPulses("right turn");
    delay(500);

    // 3. Second right turn
    Serial.println("[3] Turn RIGHT again");
    pivotRight();
    printPulses("right turn");
    delay(500);

    // 4. First left turn
    Serial.println("[4] Turn LEFT");
    pivotLeft();
    printPulses("left turn");
    delay(500);

    // 5. Second left turn
    Serial.println("[5] Turn LEFT again");
    pivotLeft();
    printPulses("left turn");

    Serial.println("--- Sequence done. Waiting 5 s before repeat. ---");
    delay(5000);
}
