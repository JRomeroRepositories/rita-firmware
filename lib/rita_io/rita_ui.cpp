#include <Arduino.h>
// #include <FreeRTOSConfig.h>
#include "rita_ui.h"

// the ui class will contain all the functions to create the user flow 
// for the user.

// User features to be implemented:
// 1. User can see the current state of the device (e.g. last watering, next watering, etc.)
// 2. User can see the state of the ML model and how close it is to consistently watering on target.
// 3. User can update the device targets (target days wet, target days dry, wet threshold?, dry threshold?).
// 4. User can choose to set or update hyperparameters for the ML model.
// 5. User can idle the device where an animation plays and the lcd goes to sleep.


RitaUi::RitaUi() {

}

void RitaUi::get_screen_state(std::string &lin_1, std::string &lin_2) {
  lin_1 = active_lin_1;
  lin_2 = active_lin_2;
}

// void RitaUi::menu_view() {

// }

// whatever updates the ui state should use a mutex resource

// The queuing of processes, especially ui changes, should be done with a semaphore.
// The semaphore is designed to have queues'


// BUTTOM IMPLEMENTATION MUST USE INTERRUPTS


