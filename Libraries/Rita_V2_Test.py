import utime
from machine import Pin
from machine import I2C
from machine import ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import Button_Handler_JR


# Define Motor Relay
motor_pin = Pin(22, Pin.OUT)

# Define LED pins
red_led_pin = Pin(2, Pin.OUT, Pin.PULL_DOWN)
blue_led_pin = Pin(3, Pin.OUT, Pin.PULL_DOWN)

# Define button pins 
button_handler6 = Button_Handler_JR.ButtonHandler(6)
button_handler7 = Button_Handler_JR.ButtonHandler(7)
# button1_pin = Pin(6, Pin.IN, Pin.PULL_UP)
# button2_pin = Pin(7, Pin.IN, Pin.PULL_UP)

# Configure ADC pin
adc = ADC(2)  # Use ADC2 (pin 34)
#adc.atten(machine.ADC.ATTN_11DB)  # Set attenuation to 11dB (0-3.3V range)

# Function to Turn on Relay
def motor_state(state):
    motor_pin.value(state)

# Set device state to null
red_led_pin.value(0)
blue_led_pin.value(0)
motor_state(0)

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

def test_main():
    #Test function for verifying basic functionality
    print("Running test_main")
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    lcd.clear()
    time = utime.localtime()
    lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(
        year=time[0], month=time[1], day=time[2],
        HH=time[3], MM=time[4], SS=time[5]))
    utime.sleep(3)
    lcd.clear()
    while True:
    # Read button states
        button1_state = button_handler6.handle_button()
        button2_state = button_handler7.handle_button()

        value = adc.read_u16()  # Read 16-bit unsigned integer value

    ## Print out information about the state of the device
        print("B1 ==", button1_state)
        print("B2 ==", button2_state)
        print("LED red", red_led_pin.value())
        print("LED blue", blue_led_pin.value())
        print("Analog value:", value)

    # Check button states and update LEDs and Motor state accordingly
        if button1_state == 0 and button2_state == 1:  # Button 1 pressed
            red_led_pin.value(1)  # Red LED on, others off
        elif button1_state == 1 and button2_state == 0:  # Button 2 pressed
            blue_led_pin.value(1)  # Blue LED on, others off
        elif button1_state == 1 and button2_state == 1:
            print("Filling display")
            lcd.clear()
            string = ""
            for x in range(32, 32+I2C_NUM_ROWS*I2C_NUM_COLS):
                string += chr(x)
                lcd.putstr(string)
            red_led_pin.value(1)
            blue_led_pin.value(1)
            motor_state(1)     # Motor On
        else:
            red_led_pin.value(0)
            blue_led_pin.value(0)  # All LEDs off
            motor_state(0)     # Motor Off
        
        utime.sleep_ms(500)        


#if __name__ == "__main__":
test_main()


