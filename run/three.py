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


PID.drive_dis(70, 10)
PID.right_turn(54)
PID.drive_dis(70, 60)
PID.right_turn(25)
PID.drive_time(57, 5)
PID.drive_dis(60, 15)
PID.right_turn(-15)
PID.drive_dis(70, 20)
PID.drive_dis(50,10)
PID.left_turn(35)
PID.drive_dis(-60, 20)
motor.time_move("D", 2, -70)
PID.drive_dis(90, 6)
PID.left_motor(15)
PID.drive_time(100,2)
motor.time_move("A", 2, -100)