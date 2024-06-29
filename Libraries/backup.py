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







## OLD non-Class version of button handler for reference

# from machine import Pin
# import utime

# ## This script can handle all setups for harware buttons including always on butons
# ## Please note that the handler function must know HOW the button pin was initialized

# ## Goal here will be to get the buttons script to handle any hardware set up and provide
# ## Multple output variations like pressed, held for 2 seconds, held for 5


# ## button norm -> helper function to normalize the button to be 1 when pressed and 0 when unpressed.
# ## Int, Char, Char -> Bool
# def bttn_norm(Bpin, InOrOut, UpOrDown):
#     Bval = Bpin.value()
#     if (UpOrDown == 'U'): # In this configuration Bpin is 0 when button pressed
#         Bval = not Bval # Thus it's inverted
#     return Bval
    

# BTTN_PREV_STATE = 0


# ## Button Handler -> function that handles the button actions
# ## Bpin, InOrOut, UpOrDown
# ## Int, Char, Char -> Char
# def bttn_handle(Bpin, InOrOut, UpOrDown):
#     Bstate = bttn_norm(Bpin, InOrOut, UpOrDown)
#     global BTTN_PREV_STATE
#     global PRESS_T_ELAPSED
#     global PRESS_START_TIME
#     if (Bstate == True) and (BTTN_PREV_STATE == False): #Pressed, If input is HIGH and different from before
#         PRESS_START_TIME = utime.ticks_ms()  #Update previous state variable
#         BTTN_PREV_STATE = True
#         #put your code or call your code to execute here for 'on-press' action
#     elif (Bstate == True) and (BTTN_PREV_STATE == True):
#         current_time = utime.ticks_ms()
#         PRESS_T_ELAPSED = current_time - PRESS_START_TIME
#         if (PRESS_T_ELAPSED > 2000):
#             if (PRESS_START_TIME != 0):
#                 PRESS_START_TIME = 0
#                 return 2
#     elif (Bstate == False) and (BTTN_PREV_STATE == True): #Released, If input is LOW and different from before
#         BTTN_PREV_STATE = False   
#         if (PRESS_START_TIME != 0):
#             return 1
#         else:
#             return 0
        


# #button1_pin = Pin(6, Pin.IN, Pin.PULL_UP)

# ## Testing Loop

# # print("Ready, Set, Go!")
# # while True:  #run an endless loop - Typical main loop
# #     bstate = bttn_handle(button1_pin, 'I', 'U')
# #     if (bstate == 2):
# #         print("hard press")
# #     elif (bstate == 1):
# #         print("quick pressed")
# #     utime.sleep(.01) #slow down the loop to mimic other processing activities

import utime
from machine import Pin
from machine import I2C
from machine import ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import Libraries.button_handler as button_handler


# Define Motor Relay
motor_pin = Pin(22, Pin.OUT)

# Define LED pins
red_led_pin = Pin(3, Pin.OUT, Pin.PULL_DOWN)
blue_led_pin = Pin(2, Pin.OUT, Pin.PULL_DOWN)

# Define button pins 
# button_handler6 = Button_Handler_JR.ButtonHandler(6)
# button_handler7 = Button_Handler_JR.ButtonHandler(7)
button1_pin = Pin(6, Pin.IN, Pin.PULL_UP)
button2_pin = Pin(7, Pin.IN, Pin.PULL_UP)

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
    red_led_pin.value(0)
    blue_led_pin.value(0)
    motor_state(0)


    # while True:
    #     red_led_pin.value(1)
    #     blue_led_pin.value(0)
    #     motor_state(0)
    #     utime.sleep(1)
    #     red_led_pin.value(0)
    #     blue_led_pin.value(1)
    #     motor_state(1)
    #     utime.sleep(1)



    # #Test function for verifying basic functionality
    # print("Running test_main")
    # i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    # lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    # lcd.clear()
    # time = utime.localtime()
    # lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(
    #     year=time[0], month=time[1], day=time[2],
    #     HH=time[3], MM=time[4], SS=time[5]))
    # utime.sleep(3)
    # lcd.clear()
    # while True:
    # # Read button states
    #     button1_state = button_handler6.handle_button()
    #     button2_state = button_handler7.handle_button()

    #     value = adc.read_u16()  # Read 16-bit unsigned integer value

    # ## Print out information about the state of the device
    #     print("B1 ==", button1_state)
    #     print("B2 ==", button2_state)
    #     print("LED red", red_led_pin.value())
    #     print("LED blue", blue_led_pin.value())
    #     print("Analog value:", value)

    # # Check button states and update LEDs and Motor state accordingly
    #     if button1_state == 0 and button2_state == 1:  # Button 1 pressed
    #         red_led_pin.value(1)  # Red LED on, others off
    #     elif button1_state == 1 and button2_state == 0:  # Button 2 pressed
    #         blue_led_pin.value(1)  # Blue LED on, others off
    #     elif button1_state == 1 and button2_state == 1:
    #         print("Filling display")
    #         lcd.clear()
    #         string = ""
    #         for x in range(32, 32+I2C_NUM_ROWS*I2C_NUM_COLS):
    #             string += chr(x)
    #             lcd.putstr(string)
    #         red_led_pin.value(1)
    #         blue_led_pin.value(1)
    #         motor_state(1)     # Motor On
    #     else:
    #         red_led_pin.value(0)
    #         blue_led_pin.value(0)  # All LEDs off
    #         motor_state(0)     # Motor Off
        
    #     utime.sleep_ms(500)        


#if __name__ == "__main__":
#test_main()



