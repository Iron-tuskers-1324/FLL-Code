#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.ev3devices import InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math
import time
import func.PID as PID
import func.motor as motor

PID.drive_dis(120, 42)              # נוסע קדימה כדי להגיע לקו 
PID.follow_line(55, 36)             # עוקב אחרי הקו עד שהוא מגיע למשימה
PID.left_turn(4)
PID.drive_dis(160, 80)              # מתיישר על הקיר ועושה את המשימה
PID.drive_dis(-80, 18)              # מתנתק מהעגלה
PID.drive_dis(100, 15)              # מתיישר על העגלה
motor.time_move("D", 1.3, -60)      # מוריד את הדלת של המטוס עם הזרוע
motor.time_move("A", 1, -200)       # מוריד מיישר לחבילה
PID.drive_dis(-80, 30)              # נוסע חצי דרך חזרה לבסיס
motor.time_move("D", 1, 100)        # מרים את הזרוע האחורית
PID.drive_dis(-120, 35)             # מגיע עד לבסיס


