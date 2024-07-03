from machine import Pin
import utime

pump = Pin(17, Pin.OUT)

pump.high()

##while True:
##    led.on()
##    print("led is on")
##    time.sleep(1)
##    led.off()
##    print("led is off")
##    time.sleep(1)