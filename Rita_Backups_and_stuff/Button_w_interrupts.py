from machine import Pin, Timer

BUTTON1_PIN = 6
BUTTON2_PIN = 7
PRESS_THRESHOLD = 2000  # Press duration threshold in milliseconds

button1 = Pin(BUTTON1_PIN, Pin.IN)
button2 = Pin(BUTTON2_PIN, Pin.IN)

button1_state = 0  # Initial state for Button 1 (no press)
button2_state = 0  # Initial state for Button 2 (no press)

button1_timer = Timer()
button2_timer = Timer()

def handle_button1_press(pin):
    global button1_state
    button1_state = 0  # Button 1 is being pressed
    button1_timer.init(mode=Timer.ONE_SHOT, period=PRESS_THRESHOLD, callback=handle_button1_release)

def handle_button2_press(pin):
    global button2_state
    button2_state = 0  # Button 2 is being pressed
    button2_timer.init(mode=Timer.ONE_SHOT, period=PRESS_THRESHOLD, callback=handle_button2_release)

def handle_button1_release(timer):
    global button1_state
    if button1_state == 0:
        button1_state = 1  # Button 1 quick press
    button1_timer.deinit()

def handle_button2_release(timer):
    global button2_state
    if button2_state == 0:
        button2_state = 1  # Button 2 quick press
    button2_timer.deinit()

button1.irq(trigger=Pin.IRQ_FALLING, handler=handle_button1_press)
button2.irq(trigger=Pin.IRQ_FALLING, handler=handle_button2_press)

def read_button_states():
    global button1_state, button2_state
    return [button1_state, button2_state]

while True:
    button_states = read_button_states()  # Read button states
    print(button_states)  # Print button states
