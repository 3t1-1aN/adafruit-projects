import time
import board
import neopixel
import random
color_value = (0,0,0)


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    for i in range(10):
        pixels[i]=color_value
        time.sleep(0.001)
        pixels.fill((0, 0, 0))
    color_value = (random.randint(0, 255), random.randint(0,255), random.randint(0,255))
