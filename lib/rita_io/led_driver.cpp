#include <Arduino.h>
#include "led_driver.hpp"

// Constructor
LedDriver::LedDriver(int pin) : LED_PIN(pin) {
    pinMode(LED_PIN, OUTPUT);
}

void LedDriver::led_turn_on() {
    digitalWrite(LED_PIN, HIGH);
}

void LedDriver::led_turn_off() {
    digitalWrite(LED_PIN, LOW);
}

void LedDriver::led_toggle() {
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
}

void LedDriver::blink_led(int times, int on_time, int off_time) {
    for (int i = 0; i < times; i++) {
        digitalWrite(LED_PIN, HIGH);
        delay(on_time);
        digitalWrite(LED_PIN, LOW);
        delay(off_time);
    };
}


