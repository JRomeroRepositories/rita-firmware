#include <Arduino.h>

class led_driver {
    public:
        void init_led_out(int pin);
        void led_turn_on(int pin);
        void led_turn_off(int pin);
        void led_toggle(int pin);
        void blink_led(int pin, int times, int on_time, int off_time);
};