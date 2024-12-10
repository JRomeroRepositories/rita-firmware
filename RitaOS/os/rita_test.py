import machine
import time

# Initialize the LED pin
led = machine.Pin(3, machine.Pin.OUT)

# Turn on the LED
led.value(1)
time.sleep(3)
led.value(0)


print("LED on pin GP2 (GPIO4) is turned ON.")
