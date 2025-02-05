#include "lcd_driver.hpp"
#include <Arduino.h>
#include <Wire.h>
#include <string>
#include <LiquidCrystal_PCF8574.h>


LcdDriver::LcdDriver(int sda_pin, int scl_pin) : SDA_PIN(sda_pin), SCL_PIN(scl_pin) {
  LiquidCrystal_PCF8574 lcd(0x27);  // set the LCD address to 0x27 for a 16 chars and 2 line display

  // Manualy set I2C pins
  Wire.setSDA(SDA_PIN);  // Set SDA to GP0
  Wire.setSCL(SCL_PIN);  // Set SCL to GP1

  // Initialize wire library
  Wire.begin();
  Wire.beginTransmission(0x27);

  int error;
  error = Wire.endTransmission();
  Serial.print("Error: ");
  Serial.print(error);

  // Begin lcd on the initialized liquid crystal instance
  lcd.begin(16, 2);
  lcd.print("LCD INITIALIZED");

}

// void LcdDriver::lcd_write_line(int lin, std::string msg) {
//     lcd.setBacklight(255);

// }
