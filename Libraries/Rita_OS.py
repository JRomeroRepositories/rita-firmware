## Rita_OS.py
## The OS for the Rita Project

import machine
import utime



# import Libraries.button_handler as bh
# import Libraries.LED_handler as lh
# import Libraries.LCD_handler as lcdh
# import Libraries.motor_handler as mh

from Libraries import button_handler as bh
from Libraries import LED_handler as lh
from Libraries import LCD_handler as lcdh
from Libraries import motor_handler as mh


from collections import namedtuple



 ## Menu System
Menu = namedtuple('Menu', ['str_lst', 'val_lst'])

main_menu = Menu(["Start Model", "Stop Model", "Set Model Parameters", "Model State Menu", "Plant State Menu", "Sleep Device"], [0, 0, 0, 0])

model_state_menu = Menu(["Nxt Watering Duration", "Lst Watering Duration", "Lst Soil Wet Duration", "Trgt Soil Wet Duration", "Time Since Lst Water"], [0, 0, 0, 0, 0])
plant_state_menu = Menu(["Moisure Level", "Time_Since_Last_Water", "Lst_Watering_Duration"], [0, 0, 0])
set_model_parameters = Menu(["Soil Moisture Threshold", "Target Days Wet", "Target Days Dry"], [0, 0, 0]) # Goes into edit mode where the user can change the values


class Rita_OS:

    # State Variables
    menu_counter = 0
    current_menu = main_menu

    next_watering_duration = 0
    last_watering_duration = 0
    last_soil_wet_duration = 0

    time_elapsed_since_last_water = 0
    time_elapsed_since_soil_moist = 0

    ## Input Values
    soil_moisture_threshold = 0
    target_days_wet = 0
    target_days_dry = 0

    

    ## Model State Menu
    def __init__(self):
        self.buttons = bh.ButtonHandler(6, 7)
        self.leds = lh.LEDHandler(3, 2)
        self.lcd = lcdh.lcd_handler()
        self.motor = mh.MotorHandler(22)

        self.menu_display(self.current_menu)
        self.menu_counter = 0

        ## Main Loop
        while True:
            buttonstate = self.buttons.handle_button()
            if buttonstate == 1:
                ## Select Action
                self.menu_action(self.current_menu.str_lst[self.menu_counter])
                
                pass
            elif buttonstate == 2:
                ## Increment Action
                self.menu_scroll(self.current_menu)
            elif buttonstate == 3:
                ## confirm change action
                pass
            
            self.menu_display(self.current_menu)
            utime.sleep(.01)



    def menu_display(self, menu):
        self.lcd.lcd_menu_display(menu.str_lst[self.menu_counter], menu.str_lst[self.menu_counter + 1])

    ## Menu Scroll
    def menu_scroll(self, menu):
        if self.menu_counter == len(menu.str_lst) - 1:
            self.menu_counter = 0
        else:
            self.menu_counter += 1

        self.menu_display(menu)

    ## Menu Actions
    def menu_action(self, menu_item_name):

        ## Main Menu Actions
        if menu_item_name == "Start Model":
            pass
        elif menu_item_name == "Stop Model":
            pass
        elif menu_item_name == "Set Model Parameters":
            self.menu = set_model_parameters
            self.menu_counter = 0
        elif menu_item_name == "Model State Menu":
            self.menu = model_state_menu
            self.menu_counter = 0
        elif menu_item_name == "Plant State Menu":
            self.menu = plant_state_menu
            self.menu_counter = 0
        elif menu_item_name == "Sleep Device":
            self.lcd.backlight_off()
        else:
            pass

        ## Model State Menu Actions
        if menu_item_name == "Nxt Watering Duration":
            pass
        elif menu_item_name == "Lst Watering Duration":
            pass
        elif menu_item_name == "Lst Soil Wet Duration":
            pass
        elif menu_item_name == "Trgt Soil Wet Duration":
            pass
        elif menu_item_name == "Time Since Lst Water":
            pass
        else:
            pass

        ## Plant State Menu Actions
        if menu_item_name == "Moisure Level":
            pass
        elif menu_item_name == "Time_Since_Last_Water":
            pass
        elif menu_item_name == "Lst_Watering_Duration":
            pass
        else:
            pass

    
        


    # def get_button_state(self):
    #     val = bh.ButtonHandler.handle_button(self.buttons)
    #     return val
    
    # def set_led_state(self, red_state, blue_state):
    #     if red_state:
    #         lh.LEDHandler.red_led_on(self.leds)
    #     if blue_state:
    #         lh.LEDHandler.blue_led_on(self.leds)

    # def water_plant(self, duration):
    #     mh.MotorHandler.motor_duration(self.motor, duration)
    
    # def lcd_display(self, row1, row2):
    #     lcdh.lcd_handler.lcd_menu_display(self.lcd, row1, row2)

Rita = Rita_OS()
    
        
