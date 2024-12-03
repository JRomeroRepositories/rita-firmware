# boot.py -- run on boot-up

# Add the paths to the modules
import sys
sys.path.append('/os')
sys.path.append('/io_driver_modules')
sys.path.append('/ai_modules')

from os.rita_core_os import CoreOS

OS = CoreOS()