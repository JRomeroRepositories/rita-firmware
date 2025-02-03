#include <Arduino.h>
// #include <FreeRTOS.h>
// #include "Scheduler.h"
#include "led_driver.hpp"
#include "motor_driver.hpp"
#include "sensor_driver.hpp"



void setup() {
    // createTasks(); // Start FreeRTOS tasks
    // vTaskStartScheduler(); // Start the RTOS
    int RED_LED_PIN = 3; // GPIO 3
    int MOTOR_PIN = 22; // GPIO 22
    int SENSOR_PIN = 28; // GPIO28 and/or ADC2

    LedDriver red_led(RED_LED_PIN);
    MotorDriver motor(MOTOR_PIN);

    red_led.led_turn_on();
    delay(1000);
    red_led.led_turn_off();
    delay(1000);
    red_led.led_turn_on();
    delay(1000);
    red_led.led_toggle();

    motor.motor_turn_on();
    delay(1000);
    motor.motor_turn_off();
    delay(1000);
    motor.motor_turn_on();
    delay(1000);
    motor.motor_toggle();


    SensorDriver m_sensor(28);
    while (1) {
        int moisture;
        moisture = m_sensor.sensor_read_val();
        Serial.println(moisture);
        delay(500);
    }
}

void loop() {
    // Not used with FreeRTOS
}