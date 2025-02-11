#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>

#include <FreeRTOS.h>
// #include "Scheduler.h"

#include "led_driver.hpp"
#include "motor_driver.hpp"
#include "sensor_driver.hpp"
#include "lcd_driver.hpp"
#include "buttons_driver.hpp"

// void button_interrupt() {
//     Serial.println("Button Pressed");
// }

void setup() {
    // createTasks(); // Start FreeRTOS tasks
    // vTaskStartScheduler(); // Start the RTOS
    int RED_LED_PIN = 3; // GPIO 3
    int MOTOR_PIN = 22; // GPIO 22
    int SENSOR_PIN = 28; // GPIO28 and/or ADC2
    int SDA_PIN = 0; // I2C0 SDA
    int SCL_PIN = 1; // I2C0 SCL
    int INC_BTTN_PIN = 6; // GPIO 6
    int SEL_BTTN_PIN = 7; // GPIO 7

    LedDriver red_led(RED_LED_PIN);
    MotorDriver motor(MOTOR_PIN);
    LcdDriver lcd;
    ButtonDriver inc_bttn(INC_BTTN_PIN);


    Serial.begin(115200);
    Serial.printf("Serial Initialized\n");

    Serial.printf("LED Test\n");
    red_led.led_turn_on();
    delay(2000);
    red_led.led_turn_off();

    Serial.printf("Motor Test\n");
    motor.motor_turn_on();
    delay(2000);
    motor.motor_turn_off();
    
    Serial.printf("LCD Test\n");
    // Place holder for LCD test


    Serial.printf("Serial Initialized\n");

    Serial.printf("Initializing button interrupts\n");
    // void button_interrupt();
    // pinMode(6, INPUT_PULLUP);
    // attachInterrupt(digitalPinToInterrupt(6), button_interrupt, LOW);
    // Note button interrupt should be fully set up at initialization.

    // Serial.printf("sensor_test\n");    
    // SensorDriver m_sensor(28);
    // while (1) {
    //     int moisture;
    //     moisture = m_sensor.sensor_read_val();
    //     Serial.println(moisture);
    //     delay(500);
    // }
}

void loop() {
    Serial.println("Nothing is happening");
    delay(1000);
    // Not used with FreeRTOS
}


// ////////////////////////////////////////////////////

// #include <Arduino.h>

// // Define the button pin
// #define BUTTON_PIN 6

// void setup() {
//     Serial.begin(115200);  // Start Serial Monitor
//     pinMode(BUTTON_PIN, INPUT_PULLUP);  // Set button as input with internal pull-up
//     Serial.println("Simple Button Press Detection Started...");
// }

// void loop() {
//     // Read button state
//     if (digitalRead(BUTTON_PIN) == LOW) {
//         Serial.println("Button Pressed!");
//         while (digitalRead(BUTTON_PIN) == LOW);  // Wait for button release (debounce)
//     } else {
//         Serial.println("Button Unpressed");
//         delay(200);  // Simple debounce delay
//     }
// }


// ////////////////////////////////////////////////////


