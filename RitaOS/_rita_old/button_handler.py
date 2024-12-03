from machine import Pin
import utime

## Button Handler Class

## The key to the button handler class is to have the output register only on button release. This
## makes it easy to handle multiple button presses and hold times. 
class ButtonHandler:
    def __init__(self, pin_1, pin_2):
        self.button_pin_1 = Pin(pin_1, Pin.IN, Pin.PULL_UP)
        self.button_pin_2 = Pin(pin_2, Pin.IN, Pin.PULL_UP)


    def _normalize_button(self, pin):
        Bval = pin.value()
        return not Bval
    

    ## Button Handler -> function that handles the button actions
    ## Button presses are normalized to 1 when pressed and 0 when unpressed
    def handle_button(self):
        Bstate_1 = self._normalize_button(self.button_pin_1)
        Bstate_2 = self._normalize_button(self.button_pin_2)

        if ((Bstate_1 == True) and (Bstate_2 == True)):
            return 3 ## Both buttons pressed
        elif (Bstate_1 == True):
            return 1 ## Select Action
        elif (Bstate_2 == True):
            return 2 ## Increment Action
        else:
            return 0 ## No action
    
        


# ## Testing Loop
# buttons = ButtonHandler(6, 7)
# print("Ready, Set, Go!")
# while True:
#     response = buttons.handle_button()
#     print(response)

