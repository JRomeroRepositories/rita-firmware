## Rita_OS.py
## The menu and main program for Rita OS
import utime
import Button_Handler_JR as bh
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


button1_pin = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
button2_pin = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)

# LCD Addressing
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

#Test function for verifying basic functionality
print("Running test_main")
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.backlight_on()
#lcd.blink_cursor_on()
