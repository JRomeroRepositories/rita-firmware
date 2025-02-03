#include <Arduino.h>
#include "led_driver.hpp"


void init_led_out(int pin) {
    pinMode(pin, OUTPUT);
}

void led_turn_on(int pin) {
    digitalWrite(pin, HIGH);
}

void led_turn_off(int pin) {
    digitalWrite(pin, LOW);
}

void led_toggle(int pin) {
    digitalWrite(pin, !digitalRead(pin));
}

void blink_led(int pin, int times, int on_time, int off_time) {
    for (int i = 0; i < times; i++) {
        digitalWrite(pin, HIGH);
        delay(on_time);
        digitalWrite(pin, LOW);
        delay(off_time);
    }
}


