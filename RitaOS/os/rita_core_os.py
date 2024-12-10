# import rita_menu_os

# from ai_modules.Rita_AI import RitaAI ## NOTE may wanna be more specific to leave out certain classes.

## Temporarily module importing that will eventually be moved to boot.py
# Add the paths to the modules
import sys
sys.path.append('/os')
sys.path.append('/io_driver_modules')
sys.path.append('/ai_modules')

import time
import _thread
from io_driver_modules.rita_io import LedDriver

class CoreOS:
    def __init__(self):
        print("CoreOS initialized")

        # self.buttons = ButtonDriver(6, 7)
        self.blue_led = LedDriver(2) ## Blue LED is wired to pin 8
        self.red_led = LedDriver(3) ## Red LED is wired to pin 9
        # self.MENU = rita_menu_os.MenuOS()
        # self.IO = ManageIO()
        # self.AI = RitaAI()


    ## run contains the operating loop
    ## TODO: impliment mainloop as the operating system is built
    def run(self):
        print("CoreOS running")

        ## Test the LED driver 
        ## TODO: thread implementation is no good, requires async methods solution
        print("Testing Blue LED")
        _thread.start_new_thread(self.blue_led.led_run, ())
        self.blue_led.led_run() ## State starts at 0, so the LED should be off
        time.sleep(3)
        self.blue_led.led_update_state(1) ## State is now 1, so the LED should be on
        print("led state: ", self.blue_led.led_state)
        time.sleep(3)
        self.blue_led.led_update_state(2) ## State is now 2, so the LED should be blinking fast
        print("led state: ", self.blue_led.led_state)
        time.sleep(3)
        self.blue_led.led_update_state(3) ## State is now 3, so the LED should be blinking slow
        print("led state: ", self.blue_led.led_state)
        time.sleep(3)
        self.blue_led.led_stop()
        
        # print("Testing Red LED")
        # self.red_led.led_run()
        # time.sleep(3)
        # self.red_led.led_update_state(1)
        # time.sleep(3)
        # self.red_led.led_update_state(2)
        # time.sleep(3)
        # self.red_led.led_update_state(3)
        # time.sleep(3)
        # self.red_led.led_stop()

        # while True:
        #     response = self.buttons.handle_button()
        #     time.sleep(0.1)
        #     print(response)

OPERATION = CoreOS()
OPERATION.run()





