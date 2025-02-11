#include <Arduino.h>


class ButtonDriver {
public:
  int PIN;
  ButtonDriver(int pin);
  static void ISR_function(); // confirm there should be 

private:
  static ButtonDriver* instance;

  // Private method that handles the interrupt in a class.
  static void handleInterrupt() {
    if (instance) {
    instance->ISR_function();
    }
  }
};

ButtonDriver* ButtonDriver::instance = nullptr;