#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.ev3devices import InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

def time_move(m, Time, speed):
    speed = speed * 10
    m = m.upper()
    D = {"A": Port.A, "B": Port.B, "C": Port.C, "D": Port.D}
    motor = Motor(D[m])
    motor.run(speed)
    time.sleep(Time)
    motor.hold()

def angle_move(m, angle, speed):
    speed = speed * 10
    m = m.upper()
    D = {"A": Port.A, "B": Port.B, "C": Port.C, "D": Port.D}
    motor = Motor(D[m])
    motor.run_angle(speed, angle)
    motor.hold()
