import utime
from machine import Pin
from machine import I2C
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

# Configure ADC pin
adc = machine.ADC(2)  # Use ADC2 (pin 34)
adc.atten(machine.ADC.ATTN_11DB)  # Set attenuation to 11dB (0-3.3V range)

# Function to Turn on Relay
def motor_state(state):
    motor_pin.value(state)

# Set device state to null
red_led_pin.value(0)
blue_led_pin.value(0)
motor_state(0)

# Main loop
while True:
    # Read button states
    button1_state = button1_pin.value()
    button2_state = button2_pin.value()
    value = adc.read_u16()  # Read 16-bit unsigned integer value

    ## Print out information about the state of the device
    print("B1 ==", button1_state)
    print("B2 ==", button2_state)
    print("LED red", red_led_pin.value())
    print("LED blue", blue_led_pin.value()
    print("Analog value:", value)

    # Check button states and update LEDs and Motor state accordingly
    if button1_state == 0 and button2_state == 1:  # Button 1 pressed
        red_led_pin.value(1)  # Red LED on, others off
    elif button1_state == 1 and button2_state == 0:  # Button 2 pressed
        blue_led_pin.value(1)  # Blue LED on, others off
    elif button1_state == 1 and button2_state == 1:
        #update_leds(1, 1)   # Both Blue and Red lights on
        red_led_pin.value(1)
        blue_led_pin.value(1)
        motor_state(1)     # Motor On
    else:
        red_led_pin.value(0)
        blue_led_pin.value(0)  # All LEDs off
        motor_state(0)     # Motor Off
    utime.sleep_ms(500)        


