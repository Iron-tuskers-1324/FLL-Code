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
PID.drive_dis(50, 48,-5)            # מאט על מנת לבצע משימה
PID.drive_time(120, 1.7)            # נוסע עד שהוא מתיישר על המשימה 
PID.drive_dis(-60, 4)               # נוסע אחורה בשביל תנופה
PID.drive_time(150, 0.7)            # נוסע משיא המהירות כדי להיתקע במשימה
PID.drive_dis(-60, 4)               # נוסע אחורה בשביל מרווח
motor.time_move("D", 5, 120)        # מרים את הזרוע עם המכולות
PID.drive_time(-120, 8)             # נוסע אחורה ומתיישר על הקיר
PID.drive_dis(60, 7)                # מקבל מרווח מהקיר
PID.right_turn(40)                  # מסתובב כדי להיכנס בבסיס

