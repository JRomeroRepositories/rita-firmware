#include <LiquidCrystal_PCF8574.h>
#include <string>

class LcdDriver {
  public:
    LcdDriver();
    void lcd_run(std::string lin_1, std::string lin_2);
    
  

  private:
    LiquidCrystal_PCF8574 lcd;
    std::string prev_lcd_state[2] = {"LINE_ONE_PLACHOL", "LINE_TWO_PLACHOL"};
};