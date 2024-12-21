
# Add the paths to the modules
import sys
sys.path.append('/os')
sys.path.append('/io_driver_modules')
sys.path.append('/ai_modules')

import time
import uasyncio
import io_driver_modules.rita_io as io



class RitaTest:

    def __init__(self):
        print("RitaTest initialized")
        self.button1 = io.ButtonDriver(6) ## Select Button
        self.button2 = io.ButtonDriver(7) ## Increment Button
        self.blue_led = io.LedDriver(2) ## Blue LED is wired to pin 8
        self.red_led = io.LedDriver(3) ## Red LED is wired to pin 9
        # self.water_sensor = io.WaterSensorDriver(28)

    async def test_io(self):



        ## Main testing loop. While active, allows for testing of the IO drivers on hardware.
        while True:
            print("This is an iteration of the main loop")
            await uasyncio.sleep(1)

            result = await uasyncio.gather(
                self.button1.button_run(),
                self.button2.button_run(),
                self.blue_led.led_run(),
                self.red_led.led_run()
                )

            print("Button 1: ", result[0])
            print("Button 2: ", result[1])
            print("Blue LED: ", result[2])
            print("Red LED: ", result[3])


            



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
uasyncio.run(test_instance.test_io())