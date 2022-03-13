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


PID.drive_dis(100, 7)
PID.right_turn(52)
PID.drive_dis(100, 72)
PID.right_turn(33)
PID.drive_time(80, 5)
PID.drive_dis(60, 20)
PID.right_turn(15)
PID.drive_dis(70, 30)
PID.drive_dis(-50,10)
PID.left_turn(35)
PID.drive_dis(-60, 20)
motor.time_move("D", 2, -70)
PID.drive_dis(90, 20)
PID.drive_time(100,2)
motor.time_move("A", 2, -100)