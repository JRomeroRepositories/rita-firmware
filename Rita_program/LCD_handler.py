## A class that handles diplay output to the LCD screen

from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


import utime

class lcd_handler:
    def __init__(self):
        # LCD Addressing
        I2C_ADDR     = 0x27
        I2C_NUM_ROWS = 2
        I2C_NUM_COLS = 16
        

        i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
        self.lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
        
        self.lcd.backlight_on()
        self.lcd_menu_display("Initializing", "Rita OS...")
        utime.sleep(2)
        self.lcd.clear()
        
    def lcd_menu_display(self, row1, row2):
        self.lcd.clear()
        self.lcd.move_to(0,0)
        self.lcd.putstr(row1)
        self.lcd.move_to(0,1)
        self.lcd.putstr(row2)
        
    def lcd_clear(self):
        self.lcd.clear()

    def lcd_toggle_backlight(self):
        if self.lcd.backlight:
            self.lcd.backlight_off()
        else:
            self.lcd.backlight_on()
    
    def backlight_on(self):
        self.lcd.backlight_on()

    def backlight_off(self):
        self.lcd.backlight_off()



    
        
