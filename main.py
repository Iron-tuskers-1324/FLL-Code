#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.ev3devices import InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math, time
import func.motor as motor

ev3 = EV3Brick()
A = False
D = {"A": Port.A, "B": Port.B, "C": Port.C, "D": Port.D}
Sprint = ev3.screen.print
clear = ev3.screen.clear
#motor = Motor(D[m])
#motor.run(speed)
clear()
motorA = Motor(D["A"])
motorB = Motor(D["B"])
motorC = Motor(D["C"])
motorD = Motor(D["D"])
i = 0
while True:
    ALL = ev3.buttons.pressed()
    if i == 0 or A:
        clear()
        Sprint('[UP]    => RUN-1')
        Sprint('[RIGHT] => RUN-2')
        Sprint('[LEFT]  => RUN-3')
        time.sleep(0.2)        
    i += 1
    if Button.UP in ALL:
        import run.one
        clear()
        Sprint("RUN-1 completed!")
        A = False
        time.sleep(0.2)
    
    elif Button.RIGHT in ALL:
        import run.two
        clear()
        Sprint("RUN-2 completed!")
        A = False
        time.sleep(0.2)

    elif Button.LEFT in ALL:
        import run.three
        clear()
        Sprint("RUN-3 completed!")
        A = False
        time.sleep(0.2)

    if Button.CENTER in ALL:
        A = True
        
         
    