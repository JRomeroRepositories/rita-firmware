
# Add the paths to the modules
import sys
sys.path.append('/os')
sys.path.append('/io_driver_modules')
sys.path.append('/ai_modules')

import machine
import time
import io_driver_modules.rita_io as io



class RitaTest:

    def __init__(self):
        print("RitaTest initialized")
        self.buttons = io.ButtonDriver(6, 7)
        self.blue_led = io.LedDriver(2) ## Blue LED is wired to pin 8
        self.red_led = io.LedDriver(3) ## Red LED is wired to pin 9
        # self.water_sensor = io.WaterSensorDriver(28)

    def test_io(self):



        ## Main testing loop. While active, allows for testing of the IO drivers on hardware.
        while True:
            ## TODO: Write io testing functionality
            



# ## Test the Water Sensor Driver
# val = 0
# adc2 = 28

# while True:
#     print("Reading sensor value")
#     sensor = WaterSensorDriver(adc2)
#     val = sensor.read_sensor()
#     print("Sensor value: ", val)
#     time.sleep(1)

## Run the test
test_instance = RitaTest()
test_instance.test_io()