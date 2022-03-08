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


def drive(speed,Distance):
    
    
    speed = -2.5*speed
    Distance = 30*Distance
    gyro.reset_angle(0)
    robot.reset()

    kp = 5
    ki = 0.0003
    kd = 1
    kt = 1
    I = 0
    output = 0
    error = 0
    p = 0
    realdistance = abs(int(robot.distance()))
    while Distance >= realdistance:
        ####print(realdistance)
        p = 0-gyro.angle()
        I = I+p
        D = error-p
        error = p
        output = (kp*p+ki*I+kd*D)*kt
        #robot.drive(speed, output*kt)
        #Dprint()

        left_motor.run(speed+output)
        right_motor.run(speed-output)
        realdistance = abs(int(robot.distance()))
        time.sleep(0.01)
    robot.stop()


def turn(angle):

    kp = 0.7
    ki = 0
    kd = 0.1
    kt = 5
    p = 0
    I = 0
    D = 0
    gyro.reset_angle(0)
    count2 = 0
    error = 0
    count = 0
    while count != 2:
        while angle != int(gyro.angle()):
            p = angle-gyro.angle()
            I = I+p
            D = error-p
            error = p
            output = (kp*p+ki*I+kd*D)*kt
            while count2 <= output and angle != int(gyro.angle()):
                left_motor.run(output*5)
                right_motor.run(output*-5)
                count2 += 1
            
        #robot.stop()
        left_motor.brake()
        right_motor.brake()
        #wait(10)
        count += 1



def follow_line(speed, Distance, sensor = "right"):
    robot.reset()
    s = sensor.lower()
    # This program requires LEGO EV3 MicroPython v2.0 or higher.
    # Click "Open user guide" on the EV3 extension tab for more information.
    if s == "right":
        sensor = ColorSensor(Port.S4)
    elif s == "left":
        sensor = ColorSensor(Port.S1)
    else:
        print("sensor invalid")
        quit()

    Distance = Distance*26
    B = 5
    W = 55
    T = 30

    DRIVE_SPEED = -2*speed

    P = 0
    I = 0
    D = 0

    error = 0

    kp = 0.56
    ki = 0.9
    kd = 1
    Bget = 30 
    realdistance = abs(int(robot.distance()))
    while Distance >= realdistance:
        # Calculate the deviation from the threshold.
        Rget = sensor.reflection()
        P = (Rget-T)*kp
        I = (P+I)*ki
        D = (P-error)*kd
        error = P
        correction = P+I+D
        #robot.drive(DRIVE_SPEED, -1*correction)
        left_motor.run(DRIVE_SPEED-correction)
        right_motor.run(DRIVE_SPEED+correction)
        realdistance = abs(int(robot.distance()))
    time.sleep(1)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)



