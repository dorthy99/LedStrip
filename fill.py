import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range (500):
        for i in range(19,-1,-1):
                pixels[i] = (0,0,255)
                time.sleep(.13)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
        for i in range(19,0,-1):
                pixels[i] = (0,0,255)
                time.sleep(.13)
                pixels[i] = (0,0,0)
        pixels[i] = (0,0,255)
