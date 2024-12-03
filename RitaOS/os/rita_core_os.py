import rita_menu_os
from io_driver_modules.rita_io import ManageIO
from ai_modules.Rita_AI import RitaAI ## NOTE may wanna be more specific to leave out certain classes.


class CoreOS:
    def __init__(self):
        print("CoreOS initialized")
        self.MENU = rita_menu_os.MenuOS()
        self.IO = ManageIO()
        self.AI = RitaAI()




