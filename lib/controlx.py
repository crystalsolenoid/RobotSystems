import logging
from logdecorator import log_on_start, log_on_end, log_on_error
import atexit

import platform
if platform.machine() == 'armv7l':
    from pin import Pin
    from adc import ADC
    from filedb import fileDB
    config_location = '/home/qntn/.picar_config'
else:
    print('''This computer does not seem to have an arm processor and therefore is not a PiCar-X. Shadowi
ng hardware calls with substitute functions.''')
    from sim_pin import Pin
    from sim_adc import ADC
    from sim_filedb import fileDB
    config_location = '/home/qkonyn/.picar_config'

logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%HL%ML%S")

logging.getLogger().setLevel(logging.DEBUG)

class Controlx():
    def __init__(self, scaling=10):
        self.scale = scaling
    
    def control(self, px, position):
        steer = position * self.scale
        px.set_dir_servo_angle(steer)
        return steer
