import time
import board
import neopixel
import random #allows for randomization
color_value = (0,0,0) #set the default color value

#initialize all the neopixels to the variable "pixels" for easy access
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    pixels[random.randint(0, 9)]=color_value #gets a random neopixel and assigns the color value
    time.sleep(0.05)
    pixels.fill((0, 0, 0)) #technically, turns all the neopixels off by turning them black
    color_value = (random.randint(0, 255), random.randint(0,255), random.randint(0,255)) #randomize the next color in the range of 0-255

