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

PID.drive_dis(120, 42)
PID.follow_line(60, 39)
PID.left_turn(10)
PID.drive_dis(150, 60)
PID.drive_dis(-80, 18)
PID.drive_dis(100, 15)
motor.time_move("D", 1.3, -60)
motor.time_move("A", 1, -200)
PID.drive_dis(-80, 30)
motor.time_move("D", 1, 100)
PID.drive_dis(-120, 35)


