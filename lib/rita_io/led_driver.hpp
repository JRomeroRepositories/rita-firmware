
class LedDriver {
    public:
        LedDriver(int pin);
        void led_turn_on();
        void led_turn_off();
        void led_toggle();
        void blink_led(int times, int on_time, int off_time);

    private:
        const int LED_PIN;
};