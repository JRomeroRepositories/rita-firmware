import utime
import machine
from machine import I2C
from io_driver_modules.lcd_api import LcdApi
from io_driver_modules.pico_i2c_lcd import I2cLcd

## io manager class

## button driver
## water sensor driver
## lcd driver
## LED driver
## motor/pump driver



class ManageIO:
    """
    A class that handles the IO of the rita device. That is, the class manages
    the device's inputs (buttons and water sensor) and outputs (motor, LEDs, and LCD).
    """
    # ## NOTE the io manager initializes all of the seperate io driver classes and stores them as attributes of the class
    # def __init__(self, button1_pin, button2_pin, water_sensor_pin, lcd_addr, lcd_rows, lcd_cols, LED1_pin, LED2_pin):
    #     """
    #     Initializes the rita_io class with the following parameters:
    #     button1_pin: The pin number of button1 (select button)
    #     button2_pin: The pin number of button2 (Increment button)
    #     water_sensor_pin: The pin number of the water sensor
    #     lcd_addr: The I2C address of the LCD
    #     lcd_rows: The number of rows of the LCD (this case 2)
    #     lcd_cols: The number of columns of the LCD (this case 16)
    #     LED1_pin: The pin number of LED1
    #     LED2_pin: The pin number of LED2
    #     """
    #     self.button1 = machine.Pin(button1_pin, machine.Pin.IN, machine.Pin.PULL_UP) ## Select Button
    #     self.button2 = machine.Pin(button2_pin, machine.Pin.IN, machine.Pin.PULL_UP) ## Increment Button
    #     self.water_sensor = machine.Pin(water_sensor_pin, machine.Pin.IN, machine.Pin.PULL_DOWN) 
    #     self.i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    #     self.lcd = I2cLcd(self.i2c, lcd_addr, lcd_rows, lcd_cols)
    #     self.LED1 = machine.Pin(LED1_pin, machine.Pin.OUT)
    #     self.LED2 = machine.Pin(LED2_pin, machine.Pin.OUT)

    # def button_check(self):
    #     """
    #     Checks the state of the buttons. Returns 1 if button1 is pressed, 2 if button2 is pressed, 3 if both are pressed, and 0 if none are pressed.
    #     """
    #     Bstate_1 = not self.button1.value()
    #     Bstate_2 = not self.button2.value()
    #     if ((Bstate_1 == True) and (Bstate_2 == True)):
    #         return 3 ## Both buttons pressed
    #     elif (Bstate_1 == True):
    #         return 1 ## Select Action
    #     elif (Bstate_2 == True):
    #         return 2 ## Increment Action
    #     else:
    #         return 0 ## No action
        
        
## Button Driver Class
# TODO: Complete the button driver class so that a signal is only sent when the button is released, ie information 
#    is only sent when the button is released. This will allow for the handling of multiple button presses and hold times.   
class ButtonDriver:
    def __init__(self, pin_1, pin_2):
        ## Initialize the button pins
        self.button_pin_1 = machine.Pin(pin_1, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button_pin_2 = machine.Pin(pin_2, machine.Pin.IN, machine.Pin.PULL_UP)

        ## Initialize the button state variables
        self.button_1_prev_state = None
        self.button_2_prev_state = None

    ## button is normalized to 1 when pressed and 0 when unpressed
    def _normalize_button(self, pin):
        Bval = pin.value()
        return not Bval
    
    def handle_button(self):
        button_1_state = self._normalize_button(self.button_pin_1)
        button_2_state = self._normalize_button(self.button_pin_2)

        ## Initialize the button state variables if they are None
        if (self.button_1_prev_state == None):
            self.button_1_prev_state = button_1_state
        if (self.button_2_prev_state == None):
            self.button_2_prev_state = button_2_state

        ## Check if the button state has changed, then only return on the release of the button
        ## Button 1
        if (button_1_state != self.button_1_prev_state):
            if ((self.button_1_prev_state == 1) and (button_1_state == 0)):
                self.button_1_prev_state = button_1_state
                return 1
            else:
                self.button_1_prev_state = button_1_state
        ## Button 2
        if (button_2_state != self.button_2_prev_state):
            if ((self.button_2_prev_state == 1) and (button_2_state == 0)):
                self.button_2_prev_state = button_2_state
                return 2
            else:
                self.button_2_prev_state = button_2_state
        ## If no button is pressed, return 0
        return 0



        # if ((Bstate_1 == True) and (Bstate_2 == True)):
        #     return 3 ## Both buttons pressed
        # elif (Bstate_1 == True):
        #     return 1 ## Select Action
        # elif (Bstate_2 == True):
        #     return 2 ## Increment Action
        # else:
        #     return 0 ## No action


## Water Sensor Driver Class
## TODO: Impliment
class WaterSensorDriver:
    def __init__(self, pin):
        self.SENSOR_PIN = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN)


## Water Pump Motor Driver Class
## TODO: Impliment motor driver class
## NOTE: In Rita V1, motor pin is wired to 15
class PumpMotorDriver:
    def __init__(self, pin):
        self.MOTOR_PIN = machine.Pin(pin, machine.Pin.OUT)

    def motor_on(self):
        self.MOTOR_PIN.value(1)
    
    def motor_off(self):
        self.MOTOR_PIN.value(0)

    def motor_toggle(self):
        if (self.MOTOR_PIN.value() == 1):
            self.MOTOR_PIN.value(0)
        else:
            self.MOTOR_PIN.value(1)
        
    def motor_duration(self, t): ## Stays on for t seconds
        self.MOTOR_PIN.value(1)
        utime.sleep(t)
        self.MOTOR_PIN.value(0)


## LCD Driver Class
## TODO: Impliment LCD Driver class - objective is to set up functions that facilitate menu functionality.
##  Below are some considerations for implimentation:
##      - text too long for a single line
##      - Idle display screen functionality
##      - Backlight timeout (possibly to be part of the menu classes)
##      - Logo and/or custom character functionality (for some style)
class LcdDriver:
    def __init__(self, addr, num_rows, num_cols):
        pass


## LED Driver Class
##  Considerations:
##      - steady signal
##      - fast blink TODO
##      - Slow blink (for error indication) TODO

## NOTE: In Rita V1, LED1 is wired to pin 8 and LED2 is wired to pin 9
class LedDriver:
    def __init__(self, red_pin, blue_pin):
        self.red_led = machine.Pin(red_pin, machine.Pin.OUT, machine.Pin.PULL_DOWN)
        self.blue_led = machine.Pin(blue_pin, machine.Pin.OUT, machine.Pin.PULL_DOWN)
        
    def red_led_on(self):
        self.red_led.value(1)
        
    def red_led_off(self):
        self.red_led.value(0)
        
    def blue_led_on(self):
        self.blue_led.value(1)
        
    def blue_led_off(self):
        self.blue_led.value(0)
        
    def red_led_toggle(self):
        if (self.red_led.value() == 1):
            self.red_led.value(0)
        else:
            self.red_led.value(1)
    
    def blue_led_toggle(self):
        if (self.blue_led.value() == 1):
            self.blue_led.value(0)
        else:
            self.blue_led.value(1)
        
    def both_leds_off(self):
        self.red_led.value(0)
        self.blue_led.value(0)
            
    def red_led_timed(self, t): ## Stays on for t seconds
        self.red_led.value(1)
        utime.sleep(t)
        self.red_led.value(0)
        
    def blue_led_timed(self, t):
        self.blue_led.value(1)
        utime.sleep(t)
        self.blue_led.value(0)
        

