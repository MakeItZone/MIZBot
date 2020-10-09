# Basic script that will drive two DC motors connected to an L293D or similar driver board.
# Accelerates motors one way, and then the other. 
# Neopixel indicates throttle- green for positive and blue for negative.
# Uses pins 0-3.

import board
import neopixel
import time
from adafruit_motor import motor
import pulseio
import math

pixel=neopixel.NeoPixel(board.NEOPIXEL,1)

motA1 = pulseio.PWMOut(board.IO0, duty_cycle=0, frequency=50)
motA2 = pulseio.PWMOut(board.IO1, duty_cycle=0, frequency=50)
motB1 = pulseio.PWMOut(board.IO2, duty_cycle=0, frequency=50)
motB2 = pulseio.PWMOut(board.IO3, duty_cycle=0, frequency=50)

motorA = motor.DCMotor(motA1, motA2)
motorB = motor.DCMotor(motB1, motB2)

throttle_range = 0.9
throttle_step = 0.1

def range_f(start, stop, increment):
    x= start
    if start <= stop:
        while x <= stop:
            yield x
            x += increment
    else:
        while x >= stop:
            yield x
            x += increment


def do_it(throttle):
    print(throttle)
    green = 0
    if throttle > 0:
        green = 255*throttle/throttle_range
    blue = 0
    if throttle <0:
        blue = 255*(-throttle/throttle_range)
    pixel[0]=(0, green, blue)
    motorA.throttle=throttle
    motorB.throttle=throttle

while True:
    for throttle in range_f(-throttle_range, throttle_range, throttle_step):
        do_it(throttle)
        time.sleep(0.5)
    print("****************")
    for throttle in range_f(throttle_range, -throttle_range, -throttle_step):
        do_it(throttle)
        time.sleep(0.5)


