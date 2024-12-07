# import rita_menu_os

# from ai_modules.Rita_AI import RitaAI ## NOTE may wanna be more specific to leave out certain classes.

## Temporarily module importing that will eventually be moved to boot.py
# Add the paths to the modules
import sys
sys.path.append('/os')
sys.path.append('/io_driver_modules')
sys.path.append('/ai_modules')

import time
from io_driver_modules.rita_io import ButtonDriver

class CoreOS:
    def __init__(self):
        print("CoreOS initialized")
        self.buttons = ButtonDriver(6, 7)
        # self.MENU = rita_menu_os.MenuOS()
        # self.IO = ManageIO()
        # self.AI = RitaAI()


    ## run contains the operating loop
    ## TODO: impliment mainloop as the operating system is built
    def run(self):
        print("CoreOS running")
        while True:
            response = self.buttons.handle_button()
            time.sleep(0.1)
            print(response)

OPERATION = CoreOS()
OPERATION.run()





