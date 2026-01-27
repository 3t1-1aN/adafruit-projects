import time
import board
import neopixel
import random
color_value = (0,0,0)


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    pixels[random.randint(0, 9)]=color_value
    time.sleep(0.05)
    pixels.fill((0, 0, 0))
    color_value = (random.randint(0, 255), random.randint(0,255), random.randint(0,255))

