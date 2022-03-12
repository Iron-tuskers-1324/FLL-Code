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
    ki = 0.0003                                         # I מגדיר מקדם
    kd = 1                                              # D מגדיר מקדם
    kt = 1                                              # מגדיר מקדם כללי
    I = 0                                               # מאפס משתנים
    output = 0                                          # מאפס משתנים
    error = 0                                           # מאפס משתנים
    p = 0                                               # מאפס משתנים
    T1 = time.time()                                    # מגדיר זמן התחלה
    T2 = time.time()                                    # מגדיר זמן עדכני
    while T2 - T1 <= Time:                              # כל עוד מספר השניות קטן מהזמן
        p = target-gyro.angle()                         # P חישוב
        I = I+p                                         # I חישוב
        D = error-p                                     # D חישוב
        error = p                                       # מגדיר שגיאה
        output = (kp*p+ki*I+kd*D)*kt                    # מחשב חישוב כללי
        left_motor.run(speed+output)                    # מניע את המנוע
        right_motor.run(speed-output)                   # מניע את המנוע
        time.sleep(0.01)                                # מחכה רגע
        T2 = time.time()                                # מגדיר זמן עדכני עדכני

def right_turn(angle):
    
    angle = -1*angle                                    # 
    kp = 0.7                                            # 
    ki = 0                                              # 
    kd = 0.1                                            # 
    kt = 5                                              # 
    p = 0                                               # 
    I = 0                                               # 
    D = 0                                               # 
    gyro.reset_angle(0)                                 # 
    count2 = 0                                          # 
    error = 0                                           # 
    count = 0                                           # 
    while count != 2:                                   # 
        while angle < int(gyro.angle()):                # 
            p = angle-gyro.angle()                      # 
            I = I+p                                     # 
            D = error-p                                 # 
            error = p                                   # 
            output = (kp*p+ki*I+kd*D)*kt                # 
            while count2<=2 and angle!=gyro.angle():    # 
                left_motor.run(output*2)                # 
                right_motor.run(output*-2)              # 
                count2 += 1                             # 
        left_motor.brake()                              # 
        right_motor.brake()                             # 
        count += 1                                      # 
        
def left_turn(angle):

    kp = 0.7                                            #
    ki = 0                                              #
    kd = 0.1                                            #
    kt = 5                                              #
    p = 0                                               #
    I = 0                                               #
    D = 0                                               #
    gyro.reset_angle(0)                                 #
    count2 = 0                                          #
    error = 0                                           #
    count = 0                                           #
    while count != 2:                                   #
        while angle > int(gyro.angle()):                #
            p = angle-gyro.angle()                      #
            I = I+p                                     #
            D = error-p                                 #
            error = p                                   #
            output = (kp*p+ki*I+kd*D)*kt                #
            while count2<=2 and angle != gyro.angle():  #
                left_motor.run(output*2)                #
                right_motor.run(output*-2)              #
                count2 += 1                             #
            
        #robot.stop()
        left_motor.brake()
        right_motor.brake()
        #wait(10)
        count += 1
        



def follow_line(speed, Distance, sensor = "right"):
    robot.reset()                                       # מאפס מרחק רובוט
    s = sensor.lower()                                  # הגדרת חיישן אור
    if s == "right":                                    # הגדרת חיישן אור
        sensor = ColorSensor(Port.S4)                   # ...
    elif s == "left":                                   # ...
        sensor = ColorSensor(Port.S1)                   # ...
    else:                                               # ...
        print("sensor invalid")                         # ...
        quit()                                          # הגדרת חיישן אור
    Distance = Distance*26                              # הכפלת מרחק לקבל מרחק אמיתי
    B = 5                                               # הגדרת צבע שחור
    W = 55                                              # הגדרת צבע לבן
    T = 30                                              # הגדרת צבע אפור

    DRIVE_SPEED = -2*speed                              # הצבת המהירות כפול 2

    P = 0                                               # איפוס שגיאה
    I = 0                                               # איפוס אינטגרל
    D = 0                                               # איפוס נגזרת
 
    error = 0                                           # איפוס משתנים

    kp = 0.56                                           # מקדם השגיאה
    ki = 0.9                                            # מקדם אינטדקל
    kd = 1                                              # הצבת מקדם נגזרת
    Bget = 30                                           # הצבת Bget
    realdistance = abs(int(robot.distance()))
    while Distance >= realdistance:                     # לולאת השגיאה
        # Calculate the deviation from the threshold.
        Rget = sensor.reflection()
        P = (Rget-T)*kp                                 # חישוב השגיאה לפי בהירות
        I = (P+I)*ki                                    # חישוב האינטגרל
        D = (P-error)*kd                                # חישוב נגזרת
        error = P                                       # הצבת השגיאה לשגיאה קודמת
        correction = P+I+D #סכום השגיאה
        #robot.drive(DRIVE_SPEED, -1*correction)
        left_motor.run(DRIVE_SPEED-correction) # הנעת מנוע שמאלי במתיקון השגיאה
        right_motor.run(DRIVE_SPEED+correction) # הנעת מנוע ימיני בתיקון השגיאה
        realdistance = abs(int(robot.distance())) # הצבה בערך מוחלט
    time.sleep(1) # הרובוט מחכה שניה
    left_motor.reset_angle(0) # איפוס מנוע שמאלי
    right_motor.reset_angle(0) # איפוס מנוע ימיני



