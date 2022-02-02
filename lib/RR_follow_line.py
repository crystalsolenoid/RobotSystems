import rossros as rr

import picarx_improved as picarx
import interpretx
import sensorx
import controlx

px = picarx.Picarx()
sx = sensorx.Sensorx()
ux = sensorx.UltraSonic()
ix = interpretx.Interpretx()
ex = interpretx.EmergencyStop()
cx = controlx.Controlx(px)
fx = controlx.Forward(px)

bGround= rr.Bus([0,0,0],"Ground Sensor")
bLine= rr.Bus(0,"Line Position")
bUltra = rr.Bus(0,"Ultrasonic Sensor")
bTooClose = rr.Bus(True, "Too Close")

pGroundSensor = rr.Producer(sx, bGround, 0.1, name="Ground Sensor")
pUltraSensor = rr.Producer(ux, bUltra, 0.1, name="Ultrasonic Sensor")
cpInterpreter = rr.ConsumerProducer(ix, bGround, bLine, 0.3, name="Interpret Line")
cpEmergencyStop = rr.ConsumerProducer(ex, bUltra, bTooClose, 0.1, name="Interpret Ultra")
cController = rr.Consumer(cx, bLine, 0.5, name="Steering")
cForward = rr.Consumer(fx, bTooClose, 0.5, name="Forward")
pTimer = rr.Timer(rr.default_termination_bus)

rr.runConcurrently([pGroundSensor, pUltraSensor,
                    cpInterpreter, cpEmergencyStop,
                    cController, cForward,
                    pTimer])


