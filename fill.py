import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

t = .02
s = 1
for i in range (1):
        for i in range(19,-1,1):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,0,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,1,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,2,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,3,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,4,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,5,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,6,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,7,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,8,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,9,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,10,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,11,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,12,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,13,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,14,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,15,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,16,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,17,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,18,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)
        pixels[i] = (255,50,0)
        for i in range(19,19,s):
                pixels[i] = (255,50,0)
                time.sleep(.03)
                pixels[i] = (0,0,0)

        for i in range(20):
                pixels[i] = (0,0,0)
        time.sleep(.3)
        for i in range(20):
                pixels[i] = (255,50,0)
