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
    def __init__(self, px, scaling=10):
        self.px = px
        self.scale = scaling

    def __call__(self, position):
        self.control(position)
    
    @log_on_start(logging.DEBUG, "Steering...")
    def control(self, position):
        steer = position * self.scale
        self.px.set_dir_servo_angle(steer)
        return steer

class Forward():
    def __init__(self, px, speed=30):
        self.px = px
        self.speed = speed

    def __call__(self, too_close):
        return self.control(too_close)

    def control(self, too_close):
        if too_close:
            self.px.stop()
        else:
            self.px.forward(self.speed)
