#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_PCF8574.h>
// // #include <FreeRTOS.h>
// // #include "Scheduler.h"
#include "led_driver.hpp"
#include "motor_driver.hpp"
#include "sensor_driver.hpp"
#include "lcd_driver.hpp"





// void setup() {
//     // createTasks(); // Start FreeRTOS tasks
//     // vTaskStartScheduler(); // Start the RTOS
//     int RED_LED_PIN = 3; // GPIO 3
//     int MOTOR_PIN = 22; // GPIO 22
//     int SENSOR_PIN = 28; // GPIO28 and/or ADC2
//     // int SDA_PIN = 0; // I2C0 SDA
//     // int SCL_PIN = 1; // I2C0 SCL

//     LedDriver red_led(RED_LED_PIN);
//     MotorDriver motor(MOTOR_PIN);
//     LcdDriver lcd;


//     Serial.begin(115200);
//     Serial.printf("Serial Initialized\n");

//     Serial.printf("LED Test\n");
//     red_led.led_turn_on();
//     delay(1000);
//     red_led.led_turn_off();
//     delay(1000);
//     red_led.led_turn_on();
//     delay(1000);
//     red_led.led_toggle();

//     Serial.printf("Motor Test\n");
//     motor.motor_turn_on();
//     delay(1000);
//     motor.motor_turn_off();
//     delay(1000);
//     motor.motor_turn_on();
//     delay(1000);
//     motor.motor_toggle();

//     Serial.printf("LCD Test\n");


//     Serial.printf("sensor_test\n");    
//     SensorDriver m_sensor(28);
//     while (1) {
//         int moisture;
//         moisture = m_sensor.sensor_read_val();
//         Serial.println(moisture);
//         delay(500);
//     }
// }

// void loop() {
//     // Not used with FreeRTOS
// }








////////////////////////////////////////////////////

// This example shows various featues of the library for LCD with 16 chars and 2 lines.

// // #include <Arduino.h>


// int RED_LED_PIN = 3; // GPIO 3
// LedDriver red_led(RED_LED_PIN);

// void setup() {
//     red_led.led_turn_on();
//     Serial.begin(115200);
//     delay(1000);
//     red_led.led_turn_off();
//     while (!Serial);
//     red_led.led_turn_on();
//     Serial.println("Scanning for I2C devices...");

//     // Manually initialize I2C0 on GP0 (SDA) and GP1 (SCL)
//     Wire.setSDA(0);  // Set SDA to GP0
//     Wire.setSCL(1);  // Set SCL to GP1
//     Wire.begin();
//     delay(1000);
//     for (byte addr = 1; addr < 127; addr++) {
//         red_led.led_toggle();
//         Wire.beginTransmission(addr);
//         if (Wire.endTransmission() == 0) {
//             Serial.print("I2C device found at 0x");
//             Serial.println(addr, HEX);
//         }
//     }
// }


// void loop() {
//     // Not used with FreeRTOS
// // }




LiquidCrystal_PCF8574 lcd(0x27);  // set the LCD address to 0x27 for a 16 chars and 2 line display

int show = -1;

int RED_LED_PIN = 3; // GPIO 3
LedDriver red_led(RED_LED_PIN);

// 2 custom characters

byte dotOff[] = { 0b00000, 0b01110, 0b10001, 0b10001,
                  0b10001, 0b01110, 0b00000, 0b00000 };
byte dotOn[] = { 0b00000, 0b01110, 0b11111, 0b11111,
                 0b11111, 0b01110, 0b00000, 0b00000 };

//   Serial.begin(115200);
//   Serial.println("LCD...");
  

void setup() {
  int error;
  Serial.begin(115200);
  Serial.println("LCD...");


  // while (1);  // Wait for serial monitor to open
  //   Serial.println("Scanning for I2C devices...");

  //   Wire.begin();  // Initialize I2C (uses default SDA=GP4, SCL=GP5 on I2C0)

  //   for (byte addr = 1; addr < 127; addr++) {
  //       Wire.beginTransmission(addr);
  //       if (Wire.endTransmission() == 0) {
  //           Serial.print("I2C device found at 0x");
  //           Serial.println(addr, HEX);
  //       }
  //   }
  //   delay(5000);



//   // wait on Serial to be available on Leonardo
//   while (!Serial);

  Serial.println("Probing for PCF8574 on address 0x27...");

  // See http://playground.arduino.cc/Main/I2cScanner how to test for a I2C device.
  // Manually initialize I2C0 on GP0 (SDA) and GP1 (SCL)
  Wire.setSDA(0);  // Set SDA to GP0
  Wire.setSCL(1);  // Set SCL to GP1
  Wire.begin();
  Wire.beginTransmission(0x27);
  error = Wire.endTransmission();
  Serial.print("Error: ");
  Serial.print(error);

  if (error == 0) {
    Serial.println(": LCD found.");
    show = 0;
    lcd.begin(16, 2);  // initialize the lcd

    lcd.createChar(1, dotOff);
    lcd.createChar(2, dotOn);

  } else {
    Serial.println(": LCD not found.");
  }  // if

  Serial.printf("LCD init complete\n");

  int RED_LED_PIN = 3; // GPIO 3
  LedDriver red_led(RED_LED_PIN);
  red_led.led_turn_on();
  delay(1000);
  red_led.led_turn_off();
  delay(1000);
  red_led.led_turn_on();

  Serial.printf("LED test complete\n");


}  // setup()


void loop() {
  Serial.println("LCD loop...");
  Serial.printf("starting main loop\n");
  // int RED_LED_PIN = 3; // GPIO 3
  // LedDriver red_led(RED_LED_PIN);
  red_led.led_toggle();

  if (show == 0) {
    lcd.setBacklight(255);
    lcd.home();
    lcd.clear();
    lcd.print("Hello LCD");
    Serial.println("Hello LCD");
    delay(1000);

    lcd.setBacklight(0);
    delay(1000);
    lcd.setBacklight(255);

  } else if (show == 1) {
    lcd.clear();
    lcd.print("[Cursor On]");
    Serial.println("Cursor On");
    lcd.cursor();

  } else if (show == 2) {
    lcd.clear();
    lcd.print("Cursor Blink");
    Serial.println("Cursor Blink");
    lcd.blink();

  } else if (show == 3) {
    lcd.clear();
    lcd.print("Cursor OFF");
    Serial.println("Cursor OFF");
    lcd.noBlink();
    lcd.noCursor();

  } else if (show == 4) {
    lcd.clear();
    lcd.print("[Display Off]");
    Serial.println("Display Off");
    lcd.noDisplay();

  } else if (show == 5) {
    lcd.clear();
    lcd.print("Display On");
    Serial.println("Display On");
    lcd.display();

  } else if (show == 7) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("*** first line.");
    Serial.println("first line");
    lcd.setCursor(0, 1);
    lcd.print("*** second line.");
    Serial.println("second line");

  } else if (show == 8) {
    lcd.scrollDisplayLeft();
  } else if (show == 9) {
    lcd.scrollDisplayLeft();
  } else if (show == 10) {
    lcd.scrollDisplayLeft();
  } else if (show == 11) {
    lcd.scrollDisplayRight();

  } else if (show == 12) {
    lcd.clear();
    lcd.print("write-");

  } else if (show == 13) {
    lcd.clear();
    lcd.print("custom 1:<\01>");
    Serial.println("custom 1");
    lcd.setCursor(0, 1);
    lcd.print("custom 2:<\02>");
    Serial.println("custom 2");

  } else {
    lcd.print(show - 13);
  }  // if

  delay(1400);
  show = (show + 1) % 16;
}  // loop()