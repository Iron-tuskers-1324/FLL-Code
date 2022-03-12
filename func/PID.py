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


def drive_dis(speed,Distance,target=0):
    
    speed = -2.5*speed                                  # מכפיל את המהירות לקבלת מהירות עדכנית
    Distance = 30*Distance                              # מכפיל את המרחק לקבלת מרחק אמיתי
    gyro.reset_angle(0)                                 # מאפס ג'ירו
    robot.reset()                                       # מאפס את המרחק של הרובוט
    kp = 5                                              # P מגדיר מקדם
    ki = 0.0003                                         # I מגדיר מקדם
    kd = 1                                              # D מגדיר מקדם
    kt = 1                                              # מגדיר מקדם כללי
    I = 0                                               # מאפס משתנים
    output = 0                                          # מאפס משתנים
    error = 0                                           # מאפס משתנים
    p = 0                                               # מאפס משתנים
    realdistance = abs(int(robot.distance()))           # מקבל את המרחק האמיתי של הרובוט
    while Distance >= realdistance:                     # כל עוד המרחק גדול מהמרחק של הרובוט
        p = target-gyro.angle()                         # P חישוב
        I = I+p                                         # I חישוב
        D = error-p                                     # D חישוב
        error = p                                       # מגדיר שגיאה
        output = (kp*p+ki*I+kd*D)*kt                    # מחשב חישוב כללי
        left_motor.run(speed+output)                    # מניע את המנוע
        right_motor.run(speed-output)                   # מניע את המנוע
        realdistance = abs(int(robot.distance()))       # מקבל מחדש את המרחק של הרובוט
        time.sleep(0.01)                                # מחכה רגע
    robot.stop()                                        # עוצר


def drive_time(speed,Time, target=0):

    speed = -2.5*speed                                  # מכפיל את המהירות לקבלת מהירות עדכנית
    gyro.reset_angle(0)                                 # מאפס ג'ירו
    kp = 5                                              # P מגדיר מקדם
    ki = 0.0003                                         # 
    kd = 1                                              # 
    kt = 1                                              # 
    I = 0                                               # 
    output = 0                                          # 
    error = 0                                           # 
    p = 0                                               # 
    T1 = time.time()                                    # 
    T2 = time.time()                                    # 
    while T2 - T1 <= Time:
        p = target-gyro.angle()
        I = I+p
        D = error-p
        error = p
        output = (kp*p+ki*I+kd*D)*kt
        left_motor.run(speed+output)
        right_motor.run(speed-output)
        time.sleep(0.01)
        T2 = time.time()

def right_turn(angle):
    angle = -1*angle
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
        while angle < int(gyro.angle()):
            p = angle-gyro.angle()
            I = I+p
            D = error-p
            error = p
            output = (kp*p+ki*I+kd*D)*kt
            while count2 <= 2 and angle != int(gyro.angle()):
                left_motor.run(output*2)
                right_motor.run(output*-2)
                count2 += 1
            
        #robot.stop()
        left_motor.brake()
        right_motor.brake()
        #wait(10)
        count += 1
        
def left_turn(angle):

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
        while angle > int(gyro.angle()):
            p = angle-gyro.angle()
            I = I+p
            D = error-p
            error = p
            output = (kp*p+ki*I+kd*D)*kt
            while count2 <= 2 and angle != int(gyro.angle()):
                left_motor.run(output*2)
                right_motor.run(output*-2)
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



