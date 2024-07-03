## Button_state
from machine import Pin, Timer
import utime

BUTTON1_PIN = 6
# BUTTON2_PIN = 7
PRESS_THRESHOLD = 2000  # Press duration threshold in milliseconds

button1 = Pin(BUTTON1_PIN, Pin.IN, Pin.PULL_UP)
# button2 = Pin(BUTTON2_PIN, Pin.IN, Pin.PULL_UP)

button1_timer = Timer()  # Timer for measuring Button 1 press duration
# button2_timer = Timer()  # Timer for measuring Button 2 press duration

button1_state = 0  # Initial state for Button 1 (no press)
# button2_state = 0  # Initial state for Button 2 (no press)

def handle_button1_press(button1_timer):
    global button1_state
    button1_state = 2  # Button 1 press duration exceeded threshold

# def handle_button2_press(timer):
#     global button2_state
#     button2_state = 2  # Button 2 press duration exceeded threshold

def handle_button1_release(button1_timer):
    global button1_state
    button1_state = 1  # Button 1 quick press

    button1_timer.deinit()  # Stop the timer

# def handle_button2_release(timer):
#     global button2_state
#     button2_state = 1  # Button 2 quick press
# 
#     button2_timer.deinit()  # Stop the timer

def read_button_states():
    global button1_state #, button2_state

    # Check Button 1 state
    if button1.value() == 0 and button1_state == 0:
        # Button 1 is pressed and was not previously pressed
        button1_timer.init(mode=Timer.ONE_SHOT, period=PRESS_THRESHOLD, callback=handle_button1_press)
        button1_state = 0  # Button 1 is being pressed
    elif button1.value() == 1 and button1_state == 2:
        # Button 1 is released after long press duration
        button1_state = 0  # Button 1 is not pressed
        button1_timer.deinit()  # Stop the timer
    elif button1.value() == 1 and button1_state == 0:
        # Button 1 is released before long press duration
        handle_button1_release(None)

#     # Check Button 2 state
#     if button2.value() == 0 and button2_state == 0:
#         # Button 2 is pressed and was not previously pressed
#         button2_timer.init(mode=Timer.ONE_SHOT, period=PRESS_THRESHOLD, callback=handle_button2_press)
#         button2_state = 0  # Button 2 is being pressed
#     elif button2.value() == 1 and button2_state == 2:
#         # Button 2 is released after long press duration
#         button2_state = 0  # Button 2 is not pressed
#         button2_timer.deinit()  # Stop the timer
#     elif button2.value() == 1 and button2_state == 0:
#         # Button 2 is released before long press duration
#         handle_button2_release(None)

    return [button1_state] #, button2_state]

while True:
    button_states = read_button_states()  # Read button states
    print(button_states)  # Print button states
    utime.sleep(1)

