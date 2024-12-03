## A time and counter classes to handle the time and counter values for the Rita_OS.py
import time


class clock:
    def __init__(self):
        self.start_time = time.time()
        self.current_time = time.time()
        self.time_elapsed = 0

    ## Update Time
    ## Updates the current time and time elapsed since the start of the clock
    def update_time(self):
        self.current_time = time.time()
        self.time_elapsed = self.current_time - self.start_time

    def reset_time(self):
        self.start_time = time.time()
        self.current_time = time.time()
        self.time_elapsed = 0
    
    def get_time(self):
        return self.time_elapsed
    
    def get_current_time(self):
        return self.current_time
    
    def get_start_time(self):
        return self.start_time
    
    def destroy(self):
        del self

