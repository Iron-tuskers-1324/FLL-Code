#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.ev3devices import InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import func.PID as PID
import func.motor as motor


motor.time_move("A", 3, 55)         # מוריד את הזרוע
PID.drive_dis(100, 100)             # נוסע קדימה לעבר המשימה במהירות
PID.drive_dis(50, 30,-7)            # מאט על מנת לבצע משימה
PID.drive_time(100, 3)            # נוסע עד שהוא מתיישר על המשימה 
PID.drive_dis(-50, 5)               # נוסע אחורה בשביל תנופה
PID.drive_time(150, 0.7)            # נוסע משיא המהירות כדי להיתקע במשימה
PID.drive_dis(-60, 4)               # נוסע אחורה בשביל מרווח
PID.drive_dis(50, 0.2)
motor.time_move("D", 8, 120)        # מרים את הזרוע עם המכולות
PID.drive_dis(-50, 15)
PID.left_turn(7)
PID.drive_dis(-80, 20)
PID.right_turn(7)
PID.drive_time(-120, 8)             # נוסע אחורה ומתיישר על הקיר
PID.drive_dis(60, 5)                # מקבל מרווח מהקיר
PID.right_turn(40)                  # מסתובב כדי להיכנס בבסיס

