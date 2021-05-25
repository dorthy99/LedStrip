import board
import neopixel
import time
n = 20
pixels = neopixel.NeoPixel(board.D18, n)


def fillup(dt):
    for i in range(n):
        pixels[i] = (255,0,255)
        time.sleep(dt)
def clear():
    for i in range(n):
        pixels[i] = (0,0,0)
def xtwo(dt):
    for x in range(n):
        r = 5*x**2
        if r < 0:
            r = 0
        if r > 255:
            r = 255
        pixels[x] = (r,25,215)
        time.sleep(.01)
def left(dt):
    for i in range (10):
        b = 5*i**2
        if b < 0:
            b = 0
        if b > 255:
            b = 255
        pixels[i] = (0,b,50)
        time.sleep(.01)

for i in range (20,10,-1):
    r = 5*i**2
    if r < 0:
        r = 0
    if r > 255:
        r = 255
    pixels[i] = (r,0,50)
    time.sleep(.01)

fillup(.01)
clear()
fillup(.01)
clear()
xtwo(.05)
clear()
left(1)
