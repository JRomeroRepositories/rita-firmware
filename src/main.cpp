#include <Arduino.h>
#include <FreeRTOS.h>
// #include "Scheduler.h"
#include "led_driver.hpp"



void setup() {
    // createTasks(); // Start FreeRTOS tasks
    // vTaskStartScheduler(); // Start the RTOS
    int RED_LED_PIN = 3; // GPIO 3
    int MOTOR_PIN = 22; // GPIO 22

    LedDriver red_led(RED_LED_PIN);

    red_led.led_turn_on();
    delay(3000);
    red_led.led_turn_off();
    delay(3000);
    red_led.led_turn_on();


}

void loop() {
    // Not used with FreeRTOS
    
}