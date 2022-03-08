from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.ev3devices import InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import func.PID as PID
import func.motor as motor


motor.time_move("A", 2, -20)
PID.drive(100, 70)
PID.drive(50, 50)
PID.drive(70, 80)
motor.time_move("D", 5, 120)
PID.drive(-70, 200)
