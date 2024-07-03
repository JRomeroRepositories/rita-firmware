## A Library that handles two on-board LEDs

from machine import Pin
import utime




## LED Handler Class
class LEDHandler:
    def __init__(self, red_pin, blue_pin):
        self.red_led = Pin(red_pin, Pin.OUT, Pin.PULL_DOWN)
        self.blue_led = Pin(blue_pin, Pin.OUT, Pin.PULL_DOWN)
        
    def red_led_on(self):
        self.red_led.value(1)
        
    def red_led_off(self):
        self.red_led.value(0)
        
    def blue_led_on(self):
        self.blue_led.value(1)
        
    def blue_led_off(self):
        self.blue_led.value(0)
        
    def red_led_toggle(self):
        if (self.red_led.value() == 1):
            self.red_led.value(0)
        else:
            self.red_led.value(1)
    
    def blue_led_toggle(self):
        if (self.blue_led.value() == 1):
            self.blue_led.value(0)
        else:
            self.blue_led.value(1)
    
    def both_leds_on(self):
        self.red_led.value(1)
        self.blue_led.value(1)
        
    def both_leds_off(self):
        self.red_led.value(0)
        self.blue_led.value(0)
        
    def both_leds_toggle(self):
        if (self.red_led.value() == 1):
            self.red_led.value(0)
        else:
            self.red_led.value(1)
        if (self.blue_led.value() == 1):
            self.blue_led.value(0)
        else:
            self.blue_led.value(1)
            
    def red_led_blink(self, t): ## Stays on for t seconds
        self.red_led.value(1)
        utime.sleep(t)
        self.red_led.value(0)
        
    def blue_led_blink(self, t):
        self.blue_led.value(1)
        utime.sleep(t)
        self.blue_led.value(0)
        
