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


motor.time_move("A", 3, 55)
PID.drive_dis(100, 100)
PID.drive_dis(50, 48,-5)
PID.drive_time(120, 1.7)
PID.drive_dis(-60, 4)
PID.drive_time(150, 0.7)
PID.drive_dis(-60, 4)
motor.time_move("D", 5, 120)
PID.drive_time(-120, 8)
PID.drive_dis(60, 7)
PID.right_turn(40)

