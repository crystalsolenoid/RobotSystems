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

class Interpretx():
    def __init__(self, sensitivity=150, polarity=1):
        self.sens = sensitivity
        self.pol = polarity

    def __call__(self, sensors):
        return self.process(sensors)
    
    def process(self, sensors):
        s0, s1, s2 = sensors
        # find gradient
        # and if polarity is negative, invert image
        # scale by sensitivity
        d1 = (s1 - s0) * self.pol / self.sens
        d2 = (s2 - s1) * self.pol / self.sens
        # determine if there is an edge
        print(d1, d2)
        if abs(d1) > 1 and abs(d2) > 1:
            return 0
        elif abs(d1) > 1:
            if d1 > 1: # +, 0
                return 0.5
            else: # -, 0
                return -1
        elif abs(d2) > 1:
            if d2 > 1: # 0, +
                return 1
            else: # 0, -
                return -0.5
        else:
            return 0

class EmergencyStop():
    def __init__(self, cutoff=50):
        self.cutoff = cutoff

    def __call__(self, ultrasonic):
        return self.process(ultrasonic)

    def process(self, ultrasonic):
        # return True if there's something too close
        return ultrasonic < self.cutoff

