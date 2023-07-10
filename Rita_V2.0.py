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

b1_state = 0
b2_state = 0

# Menu Strings
menu = ["Display Water Statisics",
        "Diplay Last Water",
        "Water 500ml Now",
        "Water 1000ml Now"]

# Menu Indexing
i = 0
j = 1

def menu_inc(n, l):
    assert(n < l)
    if ((n + 1) == l):
        return 0
    else:
        n = n + 1
        return n

def menu_dec(n, l):
    assert(n < l)
    if (n == 0):
        return (l - 1)
    else:
        n = n - 1
        return n
    
ROW_1_DISPLAY = menu[i]
ROW_1_DISPLAY = menu[j]
display = [menu[i], menu[j]]




# while True:
#     b1_state = bh.bttn_handle(button1_pin, 'I', 'U')
#     b2_state = bh.bttn_handle(button2_pin, 'I', 'U')
#     prev_display = display
#     if (b1_state == 1):
#         i = menu_inc(i, len(menu))
#         j = menu_inc(j, len(menu))
#         print("Menu incremented")
#         display = [menu[i], menu[j]]
#     if (b2_state == 1):
#          print("selected")
#          display = ["HOLD A TO CONFIRM",
#                     "Press B to cancel"]
#     print(b1_state, " , ", b2_state)

#     #LCD Display code
#     if (prev_display != display):
#         lcd_menu_display(display[0], display[1])