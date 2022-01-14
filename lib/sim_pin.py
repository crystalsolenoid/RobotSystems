# from .basic import _Basic_class
#import RPi.GPIO as GPIO

class Pin(object):
    PULL_NONE = None

    def __init__(self, *value):
        super().__init__()

    def check_board_type(self):
        pass

    def init(self, mode, pull=PULL_NONE):
        self._pull = pull
        self._mode = mode
        pass

    def dict(self, *_dict):
        return { "BOARD_TYPE": 12, }

    def __call__(self, value):
        return 0

    def value(self, *value):
        return 0

    def on(self):
        return 0

    def off(self):
        return 0

    def high(self):
        return True
#        return self.on()

    def low(self):
        return True
#        return self.off()

    def mode(self, *value):
        return self._mode

    def pull(self, *value):
        return self._pull

    def irq(self, handler=None, trigger=None, bouncetime=200):
        pass

    def name(self):
        return "GPIO%s"%"pin_name"

    def names(self):
#        return [self.name, self._board_name]
        return ["self.name", "self._board_name"]

    class cpu(object):
        GPIO17 = 17
        GPIO18 = 18
        GPIO27 = 27
        GPIO22 = 22
        GPIO23 = 23
        GPIO24 = 24
        GPIO25 = 25
        GPIO26 = 26
        GPIO4  = 4
        GPIO5  = 5
        GPIO6  = 6
        GPIO12 = 12
        GPIO13 = 13
        GPIO19 = 19
        GPIO16 = 16
        GPIO26 = 26
        GPIO20 = 20
        GPIO21 = 21

        def __init__(self):
            pass


if __name__ == "__main__":
    import time
    mcu_reset = Pin("MCURST")
    mcu_reset.off()
    time.sleep(0.001)
    mcu_reset.on() 
    time.sleep(0.01) 
