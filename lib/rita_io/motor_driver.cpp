#include <Arduino.h>
#include "motor_driver.hpp"

MotorDriver::MotorDriver(int pin) : MOTOR_PIN(pin) {
  pinMode(MOTOR_PIN, OUTPUT);
}

void MotorDriver::motor_turn_on() {
  digitalWrite(MOTOR_PIN, HIGH);
}

void MotorDriver::motor_turn_off() {
  digitalWrite(MOTOR_PIN, LOW);
}

void MotorDriver::motor_toggle() {
  digitalWrite(MOTOR_PIN, !digitalRead(MOTOR_PIN));
}


