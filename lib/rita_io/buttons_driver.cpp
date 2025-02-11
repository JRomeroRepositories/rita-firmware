#include <Arduino.h>
#include "buttons_driver.hpp"

// The button driver has to record value into a queue when pressed. 
// This queue holds the action
// The os is always checking this queue for actions.
// When the os finds a actions in the queue, it converts those to actual moves


ButtonDriver::ButtonDriver(int pin) : PIN(pin) {
  instance = this;
  PinMode(PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(pin), ButtonDriver::ISR_function, RISING); // NOTE: Must verify rising is the correct move.
}

void ButtonDriver::ISR_function() {
  Serial.println("This is a placeholder");
  // ISRs cannot return anything
  // Here is where the button semaphore should be 'mutated'
}

