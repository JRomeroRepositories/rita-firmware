
# Add the paths to the modules
import sys
sys.path.append('/os')
sys.path.append('/io_driver_modules')
sys.path.append('/ai_modules')

import machine
import time
from io_driver_modules.rita_io import WaterSensorDriver

# # Initialize the LED pin
# led = machine.Pin(3, machine.Pin.OUT)

# # Turn on the LED
# led.value(1)
# time.sleep(3)
# led.value(0)


print("LED on pin GP2 (GPIO4) is turned ON.")

val = 0
adc2 = machine.ADC(2)

while True:
    print("Reading sensor value")
    sensor = WaterSensorDriver(adc2)
    val = sensor.read_sensor()
    print("Sensor value: ", val)
