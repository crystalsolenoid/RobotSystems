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

class Sensorx():
    def __init__(self):
        self.S0 = ADC('A0')
        self.S1 = ADC('A1')
        self.S2 = ADC('A2')

    def get_adc_value(self):
        adc_value_list = []
        adc_value_list.append(self.S0.read())
        adc_value_list.append(self.S1.read())
        adc_value_list.append(self.S2.read())
        return adc_value_list

    @log_on_end(logging.DEBUG, "Distance measured: {result!r}cm")
    def Get_distance(self):
        timeout=0.01
        trig = Pin('D8')
        echo = Pin('D9')

        trig.low()
        time.sleep(0.01)
        trig.high()
        time.sleep(0.000015)
        trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while echo.value()==0:
            pulse_start = time.time()
            if pulse_start - timeout_start > timeout:
                return -1
        while echo.value()==1:
            pulse_end = time.time()
            if pulse_end - timeout_start > timeout:
                return -2
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

