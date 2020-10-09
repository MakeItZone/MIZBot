# reference: https://circuitpython.readthedocs.io/en/2.x/shared-bindings/neopixel_write/__init__.html

# This requires no external libraries
# Creates a pretty sequence, but the loops etc make it not a first script.

import board
import neopixel_write
import digitalio
import time

pin = digitalio.DigitalInOut(board.NEOPIXEL)
pin.direction = digitalio.Direction.OUTPUT
pixel = bytearray([0, 0, 0]) # GRB
dir = 1 
start = 0
end = 64
factors = [1.0, 0.5, 0]

while True:
    for r in range(start, end, dir):
        for c in range(3):
            pixel[c] = int(r * factors[c])
        #print(pixel)
        neopixel_write.neopixel_write(pin, pixel)
        time.sleep(0.1)
    dir = dir * -1
    temp = start
    start = end
    end = temp
    if dir>0: 
        factors = factors[1:] + factors[:1]