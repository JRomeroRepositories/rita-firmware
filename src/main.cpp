// #include <Arduino.h>
// #include <Wire.h>
// #include <LiquidCrystal_PCF8574.h>
// #include <SerialUSB.h>

// int sdapin = 0;
// int sclpin = 1;
// bool setSDA(pin_size_t sdapin);
// bool setSCL(pin_size_t sclpin);

// LiquidCrystal_PCF8574 lcd(0x27);  // set the LCD address to 0x27 for a 16 chars and 2 line display

// int show = -1;

// // 2 custom characters

// byte dotOff[] = { 0b00000, 0b01110, 0b10001, 0b10001,
//                   0b10001, 0b01110, 0b00000, 0b00000 };
// byte dotOn[] = { 0b00000, 0b01110, 0b11111, 0b11111,
//                  0b11111, 0b01110, 0b00000, 0b00000 };

// void setup() {
//   int error;

//   Serial.begin(115200);
//   Serial.println("LCD...");

//   // wait on Serial to be available on Leonardo
//   while (!Serial)
//     ;

//   Serial.println("Probing for PCF8574 on address 0x27...");

//   // See http://playground.arduino.cc/Main/I2cScanner how to test for a I2C device.
//   Wire.begin();
//   Wire.beginTransmission(0x27);
//   error = Wire.endTransmission();
//   Serial.print("Error: ");
//   Serial.print(error);

//   if (error == 0) {
//     Serial.println(": LCD found.");
//     show = 0;
//     lcd.begin(16, 2);  // initialize the lcd

//     lcd.createChar(1, dotOff);
//     lcd.createChar(2, dotOn);

//   } else {
//     Serial.println(": LCD not found.");
//   }  // if

// }  // setup()


// void loop() {
//   if (show == 0) {
//     lcd.setBacklight(255);
//     lcd.home();
//     lcd.clear();
//     lcd.print("Hello LCD");
//     delay(1000);

//     lcd.setBacklight(0);
//     delay(400);
//     lcd.setBacklight(255);

//   } else if (show == 1) {
//     lcd.clear();
//     lcd.print("Cursor On");
//     lcd.cursor();

//   } else if (show == 2) {
//     lcd.clear();
//     lcd.print("Cursor Blink");
//     lcd.blink();

//   } else if (show == 3) {
//     lcd.clear();
//     lcd.print("Cursor OFF");
//     lcd.noBlink();
//     lcd.noCursor();

//   } else if (show == 4) {
//     lcd.clear();
//     lcd.print("Display Off");
//     lcd.noDisplay();

//   } else if (show == 5) {
//     lcd.clear();
//     lcd.print("Display On");
//     lcd.display();

//   } else if (show == 7) {
//     lcd.clear();
//     lcd.setCursor(0, 0);
//     lcd.print("*** first line.");
//     lcd.setCursor(0, 1);
//     lcd.print("*** second line.");

//   } else if (show == 8) {
//     lcd.scrollDisplayLeft();
//   } else if (show == 9) {
//     lcd.scrollDisplayLeft();
//   } else if (show == 10) {
//     lcd.scrollDisplayLeft();
//   } else if (show == 11) {
//     lcd.scrollDisplayRight();

//   } else if (show == 12) {
//     lcd.clear();
//     lcd.print("write-");

//   } else if (show == 13) {
//     lcd.clear();
//     lcd.print("custom 1:<\01>");
//     lcd.setCursor(0, 1);
//     lcd.print("custom 2:<\02>");

//   } else {
//     lcd.print(show - 13);
//   }  // if

//   delay(1400);
//   show = (show + 1) % 16;
// }  


////////////////////////////////////////

// #include <Arduino.h>
// #include "Scheduler.h"

// void setup() {
//     // createTasks(); // Start FreeRTOS tasks
//     // vTaskStartScheduler(); // Start the RTOS
// }

// void loop() {
//     // Not used with FreeRTOS
// }

////////////////////////////////////////

// Demonstrates a simple use of the setup1()/loop1() functions
// for a multiprocessor run.

// Will output something like, where C0 is running on core 0 and
// C1 is on core 1, in parallel.

// 11:23:07.507 -> C0: Blue leader standing by...
// 11:23:07.507 -> C1: Red leader standing by...
// 11:23:07.507 -> C1: Stay on target...
// 11:23:08.008 -> C1: Stay on target...
// 11:23:08.505 -> C0: Blue leader standing by...
// 11:23:08.505 -> C1: Stay on target...
// 11:23:09.007 -> C1: Stay on target...
// 11:23:09.511 -> C0: Blue leader standing by...
// 11:23:09.511 -> C1: Stay on target...
// 11:23:10.015 -> C1: Stay on target...

// #include <Arduino.h>
// #include <FreeRTOS.h>
// #include <task.h>
// #include <map>
// #include <EEPROM.h>


// std::map<eTaskState, const char *> eTaskStateName { {eReady, "Ready"}, { eRunning, "Running" }, {eBlocked, "Blocked"}, {eSuspended, "Suspended"}, {eDeleted, "Deleted"} };

// // ps is print status of a
// void ps() {
//   int tasks = uxTaskGetNumberOfTasks();
//   TaskStatus_t *pxTaskStatusArray = new TaskStatus_t[tasks];
//   unsigned long runtime;
//   tasks = uxTaskGetSystemState( pxTaskStatusArray, tasks, &runtime );
//   Serial.printf("# Tasks: %d\n", tasks);
//   Serial.println("ID, NAME, STATE, PRIO, CYCLES");
//   for (int i=0; i < tasks; i++) {
//     Serial.printf("%d: %-16s %-10s %d %lu\n", i, pxTaskStatusArray[i].pcTaskName, eTaskStateName[pxTaskStatusArray[i].eCurrentState], (int)pxTaskStatusArray[i].uxCurrentPriority, pxTaskStatusArray[i].ulRunTimeCounter);
//   }
//   delete[] pxTaskStatusArray;
// }


// void blink(void *param) {
//   (void) param;
//   delay(500);
//   pinMode(LED_BUILTIN, OUTPUT);
//   while (true) {
//     digitalWrite(LED_BUILTIN, LOW);
//     delay(100);
//     digitalWrite(LED_BUILTIN, HIGH);
//     delay(500);
//   }
// }


// void setup() {
//   TaskHandle_t blinkTask;
//   Serial.begin(115200);
//   xTaskCreate(blink, "BLINK", 256, nullptr, 1, &blinkTask);
// #if defined(PICO_CYW43_SUPPORTED)
//   // The PicoW WiFi chip controls the LED, and only core 0 can make calls to it safely
//   vTaskCoreAffinitySet(blinkTask, 1 << 0);
// #endif
//   delay(5000);
// }

// volatile int val = 0;
// void loop() {
//   Serial.printf("C0: Blue leader standing by...\n");
//   ps();
//   Serial.printf("val: %d\n", val);
//   delay(1000);
// }

// // Running on core1
// void setup1() {
//   delay(5000);
//   Serial.printf("C1: Red leader standing by...\n");
// }

// void loop1() {
//   static int x = 0;
//   Serial.printf("C1: Stay on target...\n");
//   val++;
//   if (++x < 10) {
//     EEPROM.begin(512);
//     EEPROM.write(0,x);
//     EEPROM.commit();
//   }
//   delay(1000);
// }


// ////////////////////////////////////////


// #include <Arduino.h>
// #include <map>
// #include <EEPROM.h>
// // #include "rita_io.h"
// #include "lib/utils/utils.h"

// // LedDriver:: led(13);  // Create LED driver for pin 13

// void setup() {
//     // led.blink_led(5);  // Blink 5 times
//     Serial.begin(115200); // Initialize serial communication at 115200 baud
//     Logger::log("Hello, World!");  // Log message to serial monitor
// }

// void loop() {
//   delay(1000);
//   Logger::log("Hi");
//   Logger::log("Ho");
//     // Nothing here, or you can add periodic blinking logic
// }



int main( int argc, char **argv) {
    return 0;
}
