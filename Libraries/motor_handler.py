## A class to control the state of the motor

from machine import Pin
import utime

class MotorHandler:
    def __init__(self, motor_pin):
        self.motor = Pin(motor_pin, Pin.OUT, Pin.PULL_DOWN)
        
    def motor_on(self):
        self.motor.value(1)
        
    def motor_off(self):
        self.motor.value(0)
        
    def motor_toggle(self):
        if (self.motor.value() == 1):
            self.motor.value(0)
        else:
            self.motor.value(1)
    
    def motor_duration(self, t): ## Stays on for t seconds
        self.motor.value(1)
        utime.sleep(t)
        self.motor.value(0)