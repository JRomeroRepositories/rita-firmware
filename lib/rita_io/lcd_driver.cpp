#include "lcd_driver.hpp"
#include <Arduino.h>
#include <Wire.h>
#include <string>
#include <assert.h>
#include <LiquidCrystal_PCF8574.h>

// // Custom Characters
// const byte DOT_OFF[] = { 0b00000, 0b01110, 0b10001, 0b10001,
//                   0b10001, 0b01110, 0b00000, 0b00000 };
// const byte DOT_ON[]; = { 0b00000, 0b01110, 0b11111, 0b11111,
//                 0b11111, 0b01110, 0b00000, 0b00000 };

// const btye




LcdDriver::LcdDriver() : lcd(0x27) {   // Use member initializer list to initialize lcd for address 0x27
  const int SDA_PIN = 0;
  const int SCL_PIN = 1;

  // Manualy set I2C pins
  Wire.setSDA(SDA_PIN);  // Set SDA to GP0
  Wire.setSCL(SCL_PIN);  // Set SCL to GP1

  // Initialize wire library
  Wire.begin();
  Wire.beginTransmission(0x27);

  // error check and lcd init.
  int error = Wire.endTransmission();
  if (error == 0) {
    Serial.println(": LCD found.");
    lcd.begin(16, 2);  // initialize the lcd
    lcd.setBacklight(255);
    lcd.print("LCD INITIALIZED");
    Serial.print("LCD Initialized");
  } else {
    Serial.println(": LCD not found.");
  }  // if
}

// lcd run
// Takes two strings of exactly 16 characters and displays it on the screen.
void LcdDriver::lcd_run(std::string lin_1, std::string lin_2) {
  // Only update lcd if the state being passed is different than 
  // the previous state stored by the class.
  if (!((lin_1 == prev_lcd_state[0]) &&  (lin_2 == prev_lcd_state[1]))) {
    lcd.setCursor(0, 0);
    lcd.print(lin_1.c_str()); // Must convert to c string, liquid crystal is c lib.
    lcd.setCursor(0, 1);
    lcd.print(lin_2.c_str());

    // Update the prev_state
    prev_lcd_state[0] = lin_1;
    prev_lcd_state[1] = lin_2;
  }
}


