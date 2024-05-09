from lcd_api import LcdApi as lcd
import machine



class menu_lcd(lcd):
    def __init__(self, i2c, addr, num_lines, num_columns):
        super().__init__(i2c, addr, num_lines, num_columns)
        self._menu = []
        self._current_menu = 0
        self._current_option = 0
        self._menu_changed = False
        self._option_changed = False
        self._menu_length = 0
        self._option_length = 0