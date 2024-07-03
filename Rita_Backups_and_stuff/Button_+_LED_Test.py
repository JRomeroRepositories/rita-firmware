from machine import Pin

# Define LED pins
red_led_pin = Pin(2, Pin.OUT)
green_led_pin = Pin(3, Pin.OUT)
blue_led_pin = Pin(4, Pin.OUT)

# Define button pins 
button1_pin = Pin(6, Pin.IN, Pin.PULL_UP)
button2_pin = Pin(7, Pin.IN, Pin.PULL_UP)

# Function to update LED states
def update_leds(red, green, blue):
    red_led_pin.value(red)
    green_led_pin.value(green)
    blue_led_pin.value(blue)

# Main loop
while True:
    # Read button states
    button1_state = button1_pin.value()
    button2_state = button2_pin.value()


    ## Note in this example the button is pressed when button#_state is 0

    # Check button states and update LEDs accordingly
    if button1_state == 0 and button2_state == 1:  # Button 1 pressed
        update_leds(1, 0, 0)  # Red LED on, others off
    elif button1_state == 1 and button2_state == 0:  # Button 2 pressed
        update_leds(0, 1, 0)  # Green LED on, others off
    elif button1_state == 0 and button2_state == 0:  # Both buttons pressed
        update_leds(0, 0, 1)  # Blue LED on, others off
    else:
        update_leds(0, 0, 0)  # All LEDs off
        
        