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
while True:
    ALL = ev3.buttons.pressed()
    if Button.CENTER in ALL:
        if not(A):
            A = True
            clear()
            Sprint('["A"] --> UP & DOWN')
            Sprint('["D"] --> LEFT & RIGHT')
            time.sleep(0.2)
        else:
            A = False
            clear()
            Sprint('["B"] --> UP & DOWN')
            Sprint('["C"] --> LEFT & RIGHT')
            time.sleep(0.2)
    
    if A:
        if Button.UP in ALL:
            motorA.run(1000)
            time.sleep(0.2)
        
        elif Button.DOWN in ALL:
            motorA.run(-1000)
            time.sleep(0.2)

        else:
            motorA.stop()
        
        if Button.LEFT in ALL:
            motorD.run(1000)
            time.sleep(0.2)

        elif Button.RIGHT in ALL:
            motorD.run(-1000)
            time.sleep(0.2)
        
        else:
            motorD.stop()
         
    else:
        if Button.UP in ALL:
            motorB.run(1000)
            time.sleep(0.2)
        
        elif Button.DOWN in ALL:
            motorB.run(-1000)
            time.sleep(0.2)
        
        else:
            motorB.stop()
        
        if Button.LEFT in ALL:
            motorC.run(1000)
            time.sleep(0.2)

        elif Button.RIGHT in ALL:
            motorC.run(-1000)
            time.sleep(0.2)
         
        else:
            motorC.stop()
        
