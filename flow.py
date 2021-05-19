import board
import neopixel
import time
n = 20
pixels = neopixel.NeoPixel(board.D18, n)


def fillup(dt):
    for i in range(n):
        pixels[i] = (255,255,0)
        time.sleep(dt)
def clear():
    for i in range(n):
        pixels[i] = (0,0,0)
def xtwo():
    for x in range(n):
        r = 2+x**2
        if r < 0:
            r = 0
        if r > 255:
            r = 255
        pixels[x] = (r,0,0)
        time.sleep(.01)

fillup(.01)
clear()
fillup(.01)
clear()
xtwo()
