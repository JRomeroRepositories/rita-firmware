## Rita_OS.py
## The OS for the Rita Project

import machine
import utime



import button_handler as bh
import LED_handler as lh
import LCD_handler as lcdh
import motor_handler as mh
import Rita_time as rt


from collections import namedtuple



 ## Menu System
Menu = namedtuple('Menu', ['str_lst', 'val_lst'])

main_menu = Menu(["START MODEL", "STOP MODEL", "SET MDL PRMTRS", "MDL STAT MNU  ->", "PLNT STAT MNU ->", "SLEEP DEVICE"], [0, 0, 0, 0, 0, 0])

model_state_menu = Menu(["NXT WTR DURATION", "LST WTR DURATION", "LST SOIL WET DUR", "TRGT SOIL WET DUR", "T SINCE LAST WTR", "BCK TO MM"], [0, 0, 0, 0, 0, 0])
plant_state_menu = Menu(["MSTR LEVEL", "MDL ACCURACY"], [0, 0])
set_model_parameters = Menu(["SOIL MSTR THRSHLD", "TRGT DAYS WET", "TRGT DAYS DRY"], [0, 0, 0]) # Goes into edit mode where the user can change the values


class Rita_OS:

    # State Variables
    menu_counter = 0
    current_menu = main_menu
    top_row = ""
    bottom_row = ""

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
        # Initialize io handlers
        self.buttons = bh.ButtonHandler(6, 7)
        self.leds = lh.LEDHandler(3, 2)
        self.lcd = lcdh.lcd_handler()
        self.motor = mh.MotorHandler(22)


        ## LCD State
        self.previous_menu = main_menu
        self.current_menu = main_menu
        self.line1 = ""
        self.line2 = ""
        self.line1_prev = ""
        self.line2_prev = ""
        self.lcd_states = [[self.line1, self.line2], [self.line1_prev, self.line2_prev]]

        ## Button states
        self.button_state = 0
        self.prev_button_state = 0

        self.menu_display(self.current_menu)
        self.menu_counter = 0

        ## Main Loop
        while True:
            self.prev_button_state = self.button_state
            self.buttonstate = self.buttons.handle_button()

            if self.prev_button_state == self.prev_button_state:
                if self.buttonstate == 1:
                    ## Select Action
                    self.menu_action(self.current_menu.str_lst[self.menu_counter], self.current_menu.val_lst[self.menu_counter])
                elif self.buttonstate == 2:
                    ## Increment Action
                    self.menu_scroll(self.current_menu)
                elif self.buttonstate == 3:
                    ## confirm change action
                    pass
            
            ## Checks if the system state has changed. If so, it updates the display
            if ((self.line1 != self.line1_prev) or (self.line2 != self.line2_prev)):
                self.menu_display(self.current_menu)

            utime.sleep(.01)



    def menu_display(self, menu):
        top_idx = self.menu_counter
        if self.menu_counter == len(menu.str_lst) - 1: # If the bottom index is the last item in the list, the top index is the first item
            bottom_idx = 0
        else:
            bottom_idx = self.menu_counter + 1


        ## Update LCD state variables
        self.line1_prev = self.line1
        self.line2_prev = self.line2
        top_str = menu.str_lst[top_idx]
        bottom_str = menu.str_lst[bottom_idx]
        self.line1 = top_str
        self.line2 = bottom_str

        if len(top_str) > 16:
            top_str = top_str[:16]
        if len(bottom_str) > 16:
            bottom_str = bottom_str[:16]

        self.lcd.lcd_menu_display(top_str, bottom_str)

    ## Menu Scroll
    def menu_scroll(self, menu):
        self.menu_counter += 1
        if self.menu_counter == len(menu.str_lst):
            self.menu_counter = 0
        self.menu_display(self.current_menu)


    ## Menu Actions
    def menu_action(self, menu_item_name, menu_item_val):
        ## Main Menu Actions
        if menu_item_name == "START MODEL":
            print(menu_item_val)
        elif menu_item_name == "STOP MODEL":
            print(menu_item_val)
        elif menu_item_name == "SET MDL PRMTRS":
            self.current_menu = set_model_parameters
            self.menu_counter = 0
            self.menu_display(self.current_menu)
        elif menu_item_name == "MDL STATE MNU ->":
            self.current_menu = model_state_menu
            self.menu_counter = 0
            self.menu_display(self.current_menu)
        elif menu_item_name == "PLNT STATE MNU ->":
            self.current_menu = plant_state_menu
            self.menu_counter = 0
            self.menu_display(self.current_menu)
        elif menu_item_name == "SLEEP DEVICE":
            self.lcd.backlight_off()
        else:
            pass

        ## Model State Menu Actions
        if menu_item_name == "NXT WTR DURATION":
            pass
        elif menu_item_name == "LST WTR DURATION":
            pass
        elif menu_item_name == "LST SOIL WET DUR":
            pass
        elif menu_item_name == "TRGT SOIL WET DUR":
            pass
        elif menu_item_name == "T SINCE LAST WTR":
            pass
        elif menu_item_name == "BCK TO MM":
            self.current_menu = main_menu
            self.menu_counter = 0
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
    
        
