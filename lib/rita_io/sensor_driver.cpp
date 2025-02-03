#include <Arduino.h>
#include "sensor_driver.hpp"

SensorDriver::SensorDriver(int pin) : SENSOR_PIN(pin) {
  pinMode(SENSOR_PIN, INPUT);
}

int SensorDriver::sensor_read_val() {
  return analogRead(SENSOR_PIN);
}