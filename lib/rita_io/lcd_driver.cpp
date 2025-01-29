// #include <Arduino.h>
// #include <Wire.h>
// #include <SerialUSB.h>
// #include <LiquidCrystal_PCF8574.h>


// class LcdDriver {
//     public:
//         void setup() {
//             LiquidCrystal_PCF8574 lcd(0x27);  // set the LCD address to 0x27 for a 16 chars and 2 line display
//             int error;

//             Serial.begin(115200);
//             Serial.println("LCD...");

//             // wait on Serial to be available on Leonardo
//             while (!Serial)
//                 ;

//             Serial.println("Probing for PCF8574 on address 0x27...");

//             // See http://playground.arduino.cc/Main/I2cScanner how to test for a I2C device.
//             Wire.begin();
//             Wire.beginTransmission(0x27);
//             error = Wire.endTransmission();
//             Serial.print("Error: ");
//             Serial.print(error);

//             if (error == 0) {
//                 Serial.println(": LCD found.");
//                 show = 0;
//                 lcd.begin(16, 2);  // initialize the lcd

//                 lcd.createChar(1, dotOff);
//                 lcd.createChar(2, dotOn);

//             } else {
//                 Serial.println(": LCD not found.");
//             }  // if

//             }  // setup()
//         }
// }
