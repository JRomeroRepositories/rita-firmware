// #include <unity.h>
// #include <Arduino.h>
// #include "led_driver.hpp"


// class blink_test {
//   public:
//     int LED_PIN;
//     led_driver driver;

//     void test_init_led_out(void) {
//       int pin = LED_PIN;
//       driver.blink_led(pin);
//       TEST_ASSERT_EQUAL(OUTPUT, digitalPinToPinMode(pin));
//       }

//     void test_led_turn_on(void) {
//         int pin = LED_PIN;
//         driver.led_turn_on(pin);
//         TEST_ASSERT_EQUAL(HIGH, digitalRead(pin));
//         }

//     void test_led_turn_off(void) {
//         int pin = LED_PIN;
//         driver.led_turn_off(pin);
//         TEST_ASSERT_EQUAL(LOW, digitalRead(pin));
//         }

//     void test_led_toggle(void) {
//         int pin = LED_PIN;
//         driver.led_turn_on(pin);
//         driver.led_toggle(pin);
//         TEST_ASSERT_EQUAL(LOW, digitalRead(pin));
//         driver.led_toggle(pin);
//         TEST_ASSERT_EQUAL(HIGH, digitalRead(pin));
//         }

//     void test_blink_led(void) {
//         int pin = LED_PIN;
//         int times = 3;
//         int on_time = 100;
//         int off_time = 100;
//         driver.blink_led(pin, times, on_time, off_time);
//         TEST_ASSERT_EQUAL(HIGH, digitalRead(pin));
//         delay(on_time);
//         TEST_ASSERT_EQUAL(LOW, digitalRead(pin));
//         delay(off_time);
//         TEST_ASSERT_EQUAL(HIGH, digitalRead(pin));
//         delay(on_time);
//         TEST_ASSERT_EQUAL(LOW, digitalRead(pin));
//         delay(off_time);
//         TEST_ASSERT_EQUAL(HIGH, digitalRead(pin));
//         delay(on_time);
//         TEST_ASSERT_EQUAL(LOW, digitalRead(pin));
//         }

//     void run_tests(void){
//         UNITY_BEGIN();
//         RUN_TEST(test_init_led_out);
//         RUN_TEST(test_led_turn_on);
//         RUN_TEST(test_led_turn_off);
//         RUN_TEST(test_led_toggle);
//         RUN_TEST(test_blink_led);
//         UNITY_END();
//         }
//   }
