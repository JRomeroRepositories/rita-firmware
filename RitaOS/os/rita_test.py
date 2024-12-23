
# Add the paths to the modules
import sys
sys.path.append('/os')
sys.path.append('/io_driver_modules')
sys.path.append('/ai_modules')

# import time
import uasyncio
import io_driver_modules.rita_io as io
import time



class RitaTest:

    def __init__(self):
        print("RitaTest initialized")
        # self.button1 = io.ButtonDriver(6) ## Select Button
        # self.button2 = io.ButtonDriver(7) ## Increment Button
        self.blue_led = io.LedDriver(2) ## Blue LED is wired to pin 8
        self.red_led = io.LedDriver(3) ## Red LED is wired to pin 9
        print(self.blue_led)
        print(self.red_led)
        # self.water_sensor = io.WaterSensorDriver(28)

    ## test_leds_rotation rotates the LED states between the two LEDs every 10 seconds
    async def test_leds_rotation(self):
        while True:
            for i in range(0, 4):
                self.blue_led.led_update_state(i)
                print("Blue LED State: ", i)
                await uasyncio.sleep(5)
            
            await uasyncio.sleep(1)

            for i in range(0, 4):
                self.red_led.led_update_state(i)
                print("Red LED State: ", i)
                await uasyncio.sleep(5)

    ## test_io is a method that tests the IO of the Rita device
    async def test_io(self):
        await uasyncio.gather(
            self.test_leds_rotation(),
            self.red_led.led_run(),
            self.blue_led.led_run(),
            )

        

# ## Test the Water Sensor Driver
# val = 0
# adc2 = 28

# while True:
#     print("Reading sensor value")
#     sensor = WaterSensorDriver(adc2)
#     val = sensor.read_sensor()
#     print("Sensor value: ", val)
#     time.sleep(1)



# Run the test
test_instance = RitaTest()
print("Running test")
uasyncio.run(test_instance.test_io())