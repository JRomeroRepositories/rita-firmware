## A Class that handles all input and output for the Rita project

import Libraries.button_handler as bh
import Libraries.LED_handler as lh
import Libraries.LCD_handler as lcdh
import Libraries.motor_handler as mh
import machine

# # Pin Definitions
# button1_pin = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
# button2_pin = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
# red_led_pin = machine.Pin(3, machine.Pin.OUT, machine.Pin.PULL_DOWN)
# blue_led_pin = machine.Pin(2, machine.Pin.OUT, machine.Pin.PULL_DOWN)
# motor_pin = machine.Pin(22, machine.Pin.OUT, machine.Pin.PULL_DOWN)

# # LCD Addressing
# I2C_ADDR     = 0x27
# I2C_NUM_ROWS = 2
# I2C_NUM_COLS = 16

class Rita_IO:
    def __init__(self):
        self.buttons = bh.ButtonHandler(6, 7)
        self.leds = lh.LEDHandler(3, 2)
        self.lcd = lcdh.lcd_handler()
        self.motor = mh.MotorHandler(22)

    def get_button_state(self):
        val = bh.ButtonHandler.handle_button(self.buttons)
        return val
    
    def set_led_state(self, red_state, blue_state):
        if red_state:
            lh.LEDHandler.red_led_on(self.leds)
        if blue_state:
            lh.LEDHandler.blue_led_on(self.leds)

    def water_plant(self, duration):
        mh.MotorHandler.motor_duration(self.motor, duration)
    
    def lcd_display(self, row1, row2):
        lcdh.lcd_handler.lcd_menu_display(self.lcd, row1, row2)
    
    