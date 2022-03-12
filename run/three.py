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


PID.drive_dis(100, 5)
PID.right_turn(50)
PID.drive_dis(80, 69)
PID.right_turn(30)
PID.drive_dis(70, 50)
PID.drive_time(70, 2)
PID.left_turn(30)
PID.drive(70, 20)
PID.right_turn(30)
PID.drive_time(70, 2)
