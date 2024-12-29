import utime
import machine
from machine import I2C
from io_driver_modules.lcd_api import LcdApi
from io_driver_modules.pico_i2c_lcd import I2cLcd
import uasyncio

 

## rita_io.py Overview
## The rita_io.py module contains the following classes:
## - ManageIO 
## - ButtonDriver 
## - WaterSensorDriver
## - PumpMotorDriver
## - LcdDriver
## - LedDriver


##  ManageIO initializes all of the seperate io driver classes and stores them as attributes of the class
class ManageIO:
    """
    A class that handles the IO of the rita device. That is, the class manages
    the device's inputs (buttons and water sensor) and outputs (motor, LEDs, and LCD).
    """

    def __init__(self, button1_pin, button2_pin, water_sensor_pin, lcd_addr, lcd_rows, lcd_cols, LED1_pin, LED2_pin, motor_pin):
        """
        Initializes the rita_io class with the following parameters:
        button1_pin: The pin number of button1 (select button)
        button2_pin: The pin number of button2 (Increment button)
        water_sensor_pin: The pin number of the water sensor
        lcd_addr: The I2C address of the LCD
        lcd_rows: The number of rows of the LCD (this case 2)
        lcd_cols: The number of columns of the LCD (this case 16)
        LED1_pin: The pin number of LED1
        LED2_pin: The pin number of LED2
        motor_pin: The pin number of the motor
        """

        ## Initialize the IO pins
        self.button1_pin = button1_pin
        self.button2_pin = button2_pin
        self.water_sensor_pin = water_sensor_pin
        self.lcd_addr = lcd_addr
        self.lcd_rows = lcd_rows
        self.lcd_cols = lcd_cols
        self.LED1_pin = LED1_pin
        self.LED2_pin = LED2_pin
        self.motor_pin = motor_pin



    ## manage_io_run is a method that runs the IO manager in an async loop of 2 seconds
    async def manage_io_initialize(self):
        self.lcd = LcdDriver(self.lcd_addr, self.lcd_rows, self.lcd_cols)
        self.led1 = LedDriver(self.LED1_pin)
        self.led2 = LedDriver(self.LED2_pin)
        self.button1 = ButtonDriver(self.button1_pin)
        self.button2 = ButtonDriver(self.button2_pin)
        self.water_sensor = WaterSensorDriver(self.water_sensor_pin)
        self.motor = PumpMotorDriver(self.motor_pin)

        await uasyncio.gather(
            self.lcd.lcd_inititalize(),
            self.led1.led_initialize(),
            self.led2.led_initialize(),
        )



## -----------------------------------------------------------------------------------------------
        
##  Button Driver class - a signal is only sent when the button is released. 
class ButtonDriver:
    def __init__(self, pin):
        ## Initialize the button pins
        self.button_pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)

        ## Initialize the button state variables
        self.button_prev_state = None

    ## button is normalized to 1 when pressed and 0 when unpressed
    def _normalize_button(self, pin):
        Bval = pin.value()
        return not Bval
    
    ## handle_button is a method that checks the state of the button and returns 1 when the button is released
    async def _handle_button(self):
        button_state = self._normalize_button(self.button_pin)

        ## Initialize the button state variables if they are None
        if (self.button_prev_state == None):
            self.button_prev_state = button_state

        ## Check if the button state has changed, then only return on the release of the button.
        if (button_state != self.button_prev_state):
            if ((self.button_prev_state == 1) and (button_state == 0)):
                self.button_prev_state = button_state
                return 1
            else:
                self.button_prev_state = button_state
        return 0
    
    ## button_run is a method that runs the button handler in an async loop
    async def button_run(self):
        while True:
            response = self._handle_button()
            await uasyncio.sleep(0.1) # Prevent tight looping, yield to other tasks
            return response

## -----------------------------------------------------------------------------------------------

## Water Sensor Driver Class
## The water sensor driver class is used to read the water sensor value (asynchronously)
## The water sensor value is normalized to between 1 and 100
## The water sensor value is averaged over 10 readings
## The water sensor pin is wired to pin 34 (ADC2)
class WaterSensorDriver:
    ## Normalization constants to between 1 and 100
    TARGET_MIN = 1
    TARGET_MAX = 100

    ## Raw ADC constants
    RAW_MIN = 0
    RAW_MAX = 65535


    def __init__(self, pin):
        self.SENSOR_PIN = machine.Pin(pin, machine.Pin.IN) ## Water Sensor Pin is Pin 34 or (ADC2)
        
        self.sensor_running = False
        self.moving_average_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ## Function to normalize ADC value
    def _normalize_adc_value(self, raw_value):
        return self.TARGET_MIN + (raw_value / self.RAW_MAX) * 99

    def read_moisture_sensor(self):
        raw_val = machine.ADC(self.SENSOR_PIN).read_u16()
        normalized_val = int(self._normalize_adc_value(raw_val)) # Normalize the raw value to between 1 and 100

        ## First reading, moving average list is empty
        if sum(self.moving_average_list) == 0:
            self.moving_average_list = [normalized_val] * 10
        else:
            self.moving_average_list.pop(0) # Remove the first element
            self.moving_average_list.append(normalized_val) # Append the new value to the end of the list

        ## Return the average of the moving average list
        return sum(self.moving_average_list) / 10
    
    ## Function to read the sensor value asynchronously
    async def m_sensor_run(self):
        self.sensor_running = True
        while (self.sensor_running):
            moisture_val = self.read_moisture_sensor() # Already normalized and averaged
            await uasyncio.sleep(0.1)
            return moisture_val
        
## -----------------------------------------------------------------------------------------------

## Water Pump Motor Driver Class
## The motor driver class is used to control the water pump motor
## In Rita V1, motor pin is wired to 15
class PumpMotorDriver:
    def __init__(self, pin):
        self.MOTOR_PIN = machine.Pin(pin, machine.Pin.OUT, machine.Pin.PULL_DOWN)

    def motor_on(self):
        self.MOTOR_PIN.value(1)
    
    def motor_off(self):
        self.MOTOR_PIN.value(0)

    def motor_toggle(self):
        if (self.MOTOR_PIN.value() == 1):
            self.MOTOR_PIN.value(0)
        else:
            self.MOTOR_PIN.value(1)
        
    async def motor_run_duration(self, t): ## Stays on for t seconds
        self.MOTOR_PIN.value(1)
        await uasyncio.sleep(t)
        self.MOTOR_PIN.value(0)

## -----------------------------------------------------------------------------------------------

## LCD Driver Class
## LCD Driver class - objective is to set up functions that facilitate menu functionality.
##  Below are some considerations for implimentation:
##      - Idle display screen functionality
##      - Backlight timeout (possibly to be part of the menu classes)
##      - Logo and/or custom character functionality (for some style)
class LcdDriver:
    def __init__(self, addr, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
        self.lcd = I2cLcd(self.i2c, addr, num_rows, num_cols)

    ## lcd_initialize is a method that initializes the LCD asynchonously
    async def lcd_inititalize(self):
        await self.lcd_bl_wake(2)
        self.lcd.clear()
        self.lcd.move_to(0, 0) # column, row
        self.lcd.putstr("Rita")
        ## TODO: Impliment a logo or custom character
        self.lcd.move_to(0, 1)  # column, row
        self.lcd.putstr("Initializing...")
        await uasyncio.sleep(2)
        self.lcd.clear()
        self.lcd.hide_cursor()


    ## --- Async methods ---

    ## lcd_bl_wake is a method that wakes the backlight for a given time (t)
    async def lcd_bl_wake(self, t):
        self.lcd_backlight_on()
        await uasyncio.sleep(t)
        self.lcd_backlight_off()


    ## list_view_run is a method that runs the list view in an async loop
    ## TODO: Impliment list_view_run method so that incrementing the selected item index is possible
    # async def list_view_run(self, list_items, selected_item_index):
    #     self.lcd.clear()
    #     print("at function call selected item index: ", selected_item_index)
    #     while True:
    #         self.list_view(list_items, selected_item_index)
    #         print("selected item index check: ", selected_item_index)
    #         await uasyncio.sleep(1)


    ## lcd_stat_view is a method that displays statistics on the LCD
    ## The statistics are displayed in the following format:
    ##      - Line 1: "Stat_Name1:Stat_Value1||Stat_Name2:Stat_Value2"
    ##      - Line 2: "Stat_Name3:Stat_Value3||Stat_Name4:Stat_Value4"
    ## Where stat name is less than 3 characters and stat value is less than 3 characters
    ## Assumes 2x16 LCD
    ## TODO: Test lcd_stat_view method
    async def lcd_stat_view_run(self, stat_dict_list):
        stat_dict_list_strings = []
        assert len(stat_dict_list) == 4, "Stat dict list must have 4 dictionaries"
        for stat_name, stat in stat_dict_list:
            assert stat_name <= 3, "Stat name must be less than 3 characters"
            assert type(stat) == float or type(stat) == int, "Stat value must be a float or an integer"
            ## Convert the stat value to a string of length 3
            stat_str = str(stat)
            if len(stat_str) == 2:
                stat_str = "0" + stat_str
            elif len(stat_str) == 1:
                stat_str = "00" + stat_str
            elif len(stat_str) > 3:
                stat_str = stat_str[:3]
            ## Append the stat name and string converted value to the list
            stat_dict_list_strings.append({stat_name : stat_str}) 

        self.lcd.clear()
        while True:
            self._lcd_display(  stat_dict_list_strings[0].keys()[0] + ":" + stat_dict_list_strings[0].values()[0] + "||" + stat_dict_list_strings[1].keys()[0] + ":" + stat_dict_list_strings[1].values()[0],
                                stat_dict_list_strings[2].keys()[0] + ":" + stat_dict_list_strings[2].values()[0] + "||" + stat_dict_list_strings[3].keys()[0] + ":" + stat_dict_list_strings[3].values()[0])
            await uasyncio.sleep(0.5)


    ## --- Sync methods ---

    ## lcd_display is a method that displays two strings on the LCD
    ## The strings are displayed on two seperate lines
    ## Max length for the strings is num_cols
    def _lcd_display(self, line1, line2):
        assert len(line1) <= self.num_cols, "Line 1 is too long"
        assert len(line2) <= self.num_cols, "Line 2 is too long"
        self.lcd.move_to(0, 0)
        self.lcd.putstr(line1)
        self.lcd.move_to(0, 1)
        self.lcd.putstr(line2)

    ## list_view() displays a list of strings, with the selected item in the top row and next item in the bottom row
    ## At the end of the list, the selected item (last item) is displayed in the top row and the first item is displayed in the bottom row
    def list_view(self, list_items, selected_item_index):
        assert selected_item_index < len(list_items), "Selected item index is out of range"
        if selected_item_index == len(list_items) - 1:
            self._lcd_display(list_items[selected_item_index], list_items[0])
            self.lcd.move_to(15, 0)
            self.lcd.putstr("<")
        else:
            self._lcd_display(list_items[selected_item_index], list_items[selected_item_index + 1])
            self.lcd.move_to(15, 0)
            self.lcd.putstr("<")

    ## lcd_clear is a method that clears the LCD display
    def lcd_clear(self):
        self.lcd.clear()

    ## lcd_backlight_on is a method that turns the LCD backlight on
    def lcd_backlight_on(self):
        self.lcd.backlight_on()
    
    ## lcd_backlight_off is a method that turns the LCD backlight off
    def lcd_backlight_off(self):
        self.lcd.backlight_off()



## -----------------------------------------------------------------------------------------------

## LED Driver Class
##  States of the LED:
##      - off (self.led_state = 0)
##      - steady signal (self.led_state = 1)
##      - fast blink (self.led_state = 2)
##      - Slow blink  (self.led_state = 3)
## NOTE: In Rita V1, Blue is wired to pin 8 (GPIO2) and Red is wired to pin 9 (GPIO3)
## Blue and Red LEDs must be initialized seperately as seperate objects
class LedDriver:
    def __init__(self, led_pin):
        self.led_state = 0 # 0 is off, 1 is on, 2 is blinking (fast), 3 is blinking (slow)
        self.led_running = False
        self.led = machine.Pin(led_pin, machine.Pin.OUT)

    ## led_initialize is a method that initializes the LED asynchronously
    ## The LED is turned on for 2 seconds and then turned off
    async def led_initialize(self):
        self.led.value(1)
        await uasyncio.sleep(2)
        self.led.value(0)


    ## led_run is a method that runs the LED in the current state
    async def led_run(self):
        self.led_running = True
        while self.led_running:
            if self.led_state == 1:
                self.led.value(1)  # LED steady ON
                await uasyncio.sleep(0.1)  # Prevent tight looping, yield to other tasks
            elif self.led_state == 0:
                self.led.value(0)  # LED steady OFF
                await uasyncio.sleep(0.1)  # Prevent tight looping, yield to other tasks
            elif self.led_state == 2:
                await self._blink_led(0.5)  # Fast blink
            elif self.led_state == 3:
                await self._blink_led(1.25)  # Slow blink


    ## led_update_state is a method that updates the state of the LED
    ## The state can be 0 (off), 1 (on), 2 (fast blink), or 3 (slow blink)
    def led_update_state(self, state):
        self.led_state = state

    ## led_stop is a method that stops the LED from running completely
    ## Only call this method when the LED is no longer needed (ie. when the device is shutting down)
    def led_stop(self):
        self.led_running = False
        self.led_state = 0
        self.led.value(0)
    
    ## _blink_led is a private method that blinks the LED with the given interval (seconds)
    ## This method is called by the led_run method
    async def _blink_led(self, time_interval):
        """Blink the LED with the given interval (seconds)."""
        self.led.value(1)  # LED ON
        await uasyncio.sleep(time_interval)
        self.led.value(0)  # LED OFF
        await uasyncio.sleep(time_interval)
    
    ## _led_toggle is a private method that toggles the LED state
    def _led_toggle(self):
        if (self.led.value() == 1): ## Note: it checks the actual state of the LED pin, not the stored state
            self.led.value(0)
        else:
            self.led.value(1)

## -----------------------------------------------------------------------------------------------


