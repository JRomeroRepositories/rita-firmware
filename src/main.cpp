#include <Arduino.h>
#include <FreeRTOS.h>
// #include "Scheduler.h"

void read_from_analog_pin(int pin) {
    int analog_pin = pin;
    int analog_value = 0;
    pinMode(analog_pin, INPUT);
    while (true) {
        analog_value = analogRead(analog_pin);
        Serial.printf("Analog value: %d\n", analog_value);
        delay(1000);
    }
}


void setup() {
    // createTasks(); // Start FreeRTOS tasks
    // vTaskStartScheduler(); // Start the RTOS
    int RED_LED_PIN = 3; // GPIO 3
    int MOTOR_PIN = 22; // GPIO 22

    pinMode(RED_LED_PIN, OUTPUT);
    pinMode(MOTOR_PIN, OUTPUT);

    digitalWrite(RED_LED_PIN, HIGH);
    digitalWrite(MOTOR_PIN, HIGH);
    delay(1000);
    digitalWrite(RED_LED_PIN, LOW);
    digitalWrite(MOTOR_PIN, LOW);
    delay(1000);
    digitalWrite(RED_LED_PIN, HIGH);
    digitalWrite(MOTOR_PIN, HIGH);
    delay(3000);
    digitalWrite(RED_LED_PIN, LOW);
    digitalWrite(MOTOR_PIN, LOW);

    
    read_from_analog_pin(28);

}

void loop() {
    // Not used with FreeRTOS
}


// // Demonstrates a simple use of the setup1()/loop1() functions
// // for a multiprocessor run.

// // Will output something like, where C0 is running on core 0 and
// // C1 is on core 1, in parallel.

// // 11:23:07.507 -> C0: Blue leader standing by...
// // 11:23:07.507 -> C1: Red leader standing by...
// // 11:23:07.507 -> C1: Stay on target...
// // 11:23:08.008 -> C1: Stay on target...
// // 11:23:08.505 -> C0: Blue leader standing by...
// // 11:23:08.505 -> C1: Stay on target...
// // 11:23:09.007 -> C1: Stay on target...
// // 11:23:09.511 -> C0: Blue leader standing by...
// // 11:23:09.511 -> C1: Stay on target...
// // 11:23:10.015 -> C1: Stay on target...

// #include <Arduino.h>
// #include <FreeRTOS.h>
// #include <task.h>
// #include <map>
// #include <EEPROM.h>


// std::map<eTaskState, const char *> eTaskStateName { {eReady, "Ready"}, { eRunning, "Running" }, {eBlocked, "Blocked"}, {eSuspended, "Suspended"}, {eDeleted, "Deleted"} };
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
