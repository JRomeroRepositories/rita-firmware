
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



## Test the Water Sensor Driver
val = 0
adc2 = 28

while True:
    print("Reading sensor value")
    sensor = WaterSensorDriver(adc2)
    val = sensor.read_sensor()
    print("Sensor value: ", val)
    time.sleep(1)

## Run the test
test_instance = RitaTest()
test_instance.test_io()