from machine import Pin
import utime

class ButtonHandler:
    def __init__(self, pin_num):
        self.button_pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        self.BTTN_PREV_STATE = 0
        self.PRESS_START_TIME = 0
        self.PRESS_T_ELAPSED = 0
        self.PRESS_UP_DOWN = 'U'

    def normalize_button(self):
        Bval = self.button_pin.value()
        if self.PRESS_UP_DOWN == 'U':
            Bval = not Bval
        return Bval

    def handle_button(self):
        Bstate = self.normalize_button()
        if Bstate and not self.BTTN_PREV_STATE:
            self.PRESS_START_TIME = utime.ticks_ms()
            self.BTTN_PREV_STATE = True
        elif Bstate and self.BTTN_PREV_STATE:
            current_time = utime.ticks_ms()
            self.PRESS_T_ELAPSED = current_time - self.PRESS_START_TIME
            if self.PRESS_T_ELAPSED > 2000:
                if self.PRESS_START_TIME != 0:
                    self.PRESS_START_TIME = 0
                    return 2
        elif not Bstate and self.BTTN_PREV_STATE:
            self.BTTN_PREV_STATE = False
            if self.PRESS_START_TIME != 0:
                return 1
            else:
                return 0

# Usage example:
# button_handler = ButtonHandler(6)  # Create an instance with the button pin number
# print("Ready, Set, Go!")
# while True:
#     bstate = button_handler.handle_button()
#     if bstate == 2:
#         print("hard press")
#     elif bstate == 1:
#         print("quick pressed")
#     utime.sleep(.01)









## OLD non-Class version for reference

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

