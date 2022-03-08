#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.ev3devices import InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math
import time
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
middle_motorA = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter = 290, axle_track = 120)
robot.settings(straight_speed = 200, straight_acceleration = 100, turn_rate = 100)
gyro = GyroSensor(Port.S2)



def time_move(m, Time, speed):
    speed = speed * 10
    m = m.upper()
    D = {"A": Port.A, "B": Port.B, "C": Port.C, "D": Port.D}
    motor = Motor(D[m])
    motor.run(speed)
    time.sleep(Time)
    motor.hold()

def angle_move(m, angle, speed):
    speed = speed * 10
    m = m.upper()
    D = {"A": Port.A, "B": Port.B, "C": Port.C, "D": Port.D}
    motor = Motor(D[m])
    motor.run_angle(speed, angle)
    motor.hold()



def on_line():
    Black = 6
    White = 50
    speed = -40
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    robot = DriveBase(left_motor, right_motor, wheel_diameter = 290, axle_track = 120)
    Lsensor = ColorSensor(Port.S1)
    Rsensor = ColorSensor(Port.S4)
    while Rsensor.reflection() >=  Black:
        left_motor.run(speed*2)
        right_motor.run(speed*2)
        
    while Lsensor.reflection() <=  White:
        left_motor.run(speed*2)
        right_motor.run(speed*-1.5)
    
    #while Rsensor.reflection() > =  Black:
    #    left_motor.run(speed*0.5)
    #   right_motor.run(speed*-1)
    
    for i in range(3):
        C = 0
        while C<10000:
            if Lsensor.reflection() >= White:
                left_motor.run(speed)
            if Rsensor.reflection() >= White:
                right_motor.run(speed)
            C += 1
        #####print(C)
        C = 0
        while C<10000:
            if Lsensor.reflection() <= Black:
                left_motor.run(-1*speed)
            if Rsensor.reflection() <= Black:
                right_motor.run(-1*speed)
            C += 1
            