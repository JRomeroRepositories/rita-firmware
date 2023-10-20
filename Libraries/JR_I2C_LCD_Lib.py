
def display_scroll(string, row_no):
    speed_Adjust = 300;   # Speed of moving Text
    rest_Time = 400;      # Resting time of Text animation at the edges of display
    text_Len = len(string)              ## Variable to save text length
    while True:
        j = 0
        # Write the indicated string to the LCD at the current cursor
        # position and advances the cursor position appropriately.
        lcd.move_to((row_no - 1), 0)
        for char in string: ## IN THIS AREA WORKING ON SCROLLABLE TEXT****
            lcd.putchar(char)
            j = j + 1
            print(j)
            if (i == 16):
                lcd.move_to((row_no - 1), 0)
                j = 0
        utime.sleep_ms(speed_Adjust)
    utime.sleep_ms(rest_Time)
    lcd.clear()


## lcd_menu_display(string1, string2) -> lcd output
## Assess the length of the strings to be displayed in the 16x2 lcd, and 
##  displays them scrolling or non-scrolling appropriately.
def lcd_menu_display(Row1, Row2):
    if (len(Row1) > 16 and len(Row2) > 16)
        display_scroll(Row1, 1)
        display_scroll(Row2, 2)
    elif (len(Row1) <= 16 and len(Row2) > 16)
        lcd.move_to(0, 0)
        lcd.putstr(Row1)
        display_scroll(Row2, 2)
    elif (len(Row1) > 16 and len(Row2) <= 16)
        display_scroll(Row1, 1)
        lcd.move_to(2, 0)
        lcd.putstr(Row2)
    else (len(Row1) <= 16 and len(Row2) <= 16)
        lcd.move_to(0, 0)
        lcd.putstr(Row1)
        lcd.move_to(2, 0)
        lcd.putstr(Row2)



display_scroll("Show me the money baby", 1)