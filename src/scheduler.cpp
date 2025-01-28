
#include "Scheduler.h"
#include <Arduino.h>
#include <FreeRTOS.h>



void idle_checks(void *pvParameters) {
    for (;;) {
        // Perform I/O logic
        vTaskDelay(100 / portTICK_PERIOD_MS); // Delay for 100ms
    }
}

void lcd(void *pvParameters) {
    for (;;) {
        // Perform I/O logic
        vTaskDelay(100 / portTICK_PERIOD_MS); // Delay for 100ms
    }
}

void (void *pvParameters) {
    for (;;) {
        // Perform I/O logic
        vTaskDelay(100 / portTICK_PERIOD_MS); // Delay for 100ms
    }
}

void buttons(void *pvParameters) {
    for (;;) {
        // Perform I/O logic
        vTaskDelay(100 / portTICK_PERIOD_MS); // Delay for 100ms
    }
}


void createTasks() {
    xTaskCreate(ioTask, "IOTask", 1024, NULL, 1, NULL);
}
