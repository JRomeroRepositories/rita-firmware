#include "lcd_driver.hpp"
#include <Arduino.h>
#include <Wire.h>
#include <string>
#include <LiquidCrystal_PCF8574.h>


LcdDriver::LcdDriver() : lcd(0x27) {   // Use member initializer list to initialize lcd for address 0x27
  const int SDA_PIN = 0;
  const int SCL_PIN = 1;

  // Manualy set I2C pins
  Wire.setSDA(SDA_PIN);  // Set SDA to GP0
  Wire.setSCL(SCL_PIN);  // Set SCL to GP1

  // Initialize wire library
  Wire.begin();
  Wire.beginTransmission(0x27);

  // error check.
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
  

  // Begin lcd on the initialized liquid crystal instance
}

// void LcdDriver::lcd_write_line(int lin, std::string msg) {
//     lcd.setBacklight(255);

// }
