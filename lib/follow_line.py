import time

import picarx_improved as picarx
import interpretx
import sensorx
import controlx

def update_steering(ix, sx, cx):
    data = sx.get_adc_value()
    position = ix.process(data)
    print(data, position)
    angle = cx.control(position)
    return angle

if __name__ == "__main__":
    px = picarx.Picarx()
    ix = interpretx.Interpretx()
    sx = sensorx.Sensorx()
    cx = controlx.Controlx(px)
    while True:
        angle = update_steering(ix, sx, cx)
        px.drive_distance(0.3, angle, 25)
