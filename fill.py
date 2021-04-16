import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range (500):
        for i in range(19,-1,-1):
                pixels[i] = (0,0,255)
                time.sleep(.05)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
        for i in range(19,0,-1):
                pixels[i] = (0,0,255)
                time.sleep(.05)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
        for i in range(19,1,-1):
                pixels[i] = (0,0,255)
                time.sleep(.05)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
        for i in range(19,2,-1):
                pixels[i] = (0,0,255)
                time.sleep(.05)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
        for i in range(19,3,-1):
                pixels[i] = (0,0,255)
                time.sleep(.05)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
        for i in range(19,4,-1):
                pixels[i] = (0,0,255)
                time.sleep(.05)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
        for i in range(19,5,-1):
                pixels[i] = (0,0,255)
                time.sleep(.05)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
