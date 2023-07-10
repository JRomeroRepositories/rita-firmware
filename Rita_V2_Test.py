import utime
from machine import Pin
from machine import I2C
#import Button_Handler_JR as bh
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


# Define Motor Relay
motor_pin = Pin(22, Pin.OUT)

# Define LED pins
red_led_pin = Pin(2, Pin.OUT, Pin.PULL_DOWN)
blue_led_pin = Pin(3, Pin.OUT, Pin.PULL_DOWN)

# Define button pins 
button1_pin = Pin(6, Pin.IN, Pin.PULL_UP)
button2_pin = Pin(7, Pin.IN, Pin.PULL_UP)

# Function to update LED states
def update_leds(red, blue):
    red_led_pin.value(red)
    blue_led_pin.value(blue)

# Function to Turn on Relay
def motor_state(state):
    motor_pin.value(state)

# Set device state to null
update_leds(0, 0)
motor_state(0)

# Main loop
while True:
    # Read button states
    button1_state = button1_pin.value()
    button2_state = button2_pin.value()
    print("B1 ==", button1_state)
    print("B2 ==", button2_state)
    print("LED red", red_led_pin.value())
    print("LED blue", blue_led_pin.value())

    # Note in this example the button is pressed when button#_state is 0
    # Check button states and update LEDs accordingly
    if button1_state == 0 and button2_state == 1:  # Button 1 pressed
        update_leds(0, 1)  # Red LED on, others off
    elif button1_state == 1 and button2_state == 0:  # Button 2 pressed
        update_leds(1, 0)  # Blue LED on, others off
    elif button1_state == 1 and button2_state == 1:
        #update_leds(1, 1)   # Both Blue and Red lights on
        motor_state(1)     # Motor On
    else:
        update_leds(0, 0)  # All LEDs off
        motor_state(0)     # Motor Off
        continue
    utime.sleep_ms(500)        


