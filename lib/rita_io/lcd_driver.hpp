#include <LiquidCrystal_PCF8574.h>

class LcdDriver {
  public:
  LiquidCrystal_PCF8574 lcd;
  LcdDriver(int sda_pin, int scl_pin);

  private:
    const int SDA_PIN;
    const int SCL_PIN;

};