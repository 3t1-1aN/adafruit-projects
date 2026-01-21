import time
from adafruit_circuitplayground import cp

THRESHOLD_UP = 5
THRESHOLD_RIGHT = -5
THRESHOLD_LEFT = -5
COLOR_VALUE = (255, 155, 0)

def right_animation():
    #cp.pixels.brightness = 0.3
    cp.pixels[0] = COLOR_VALUE
    cp.pixels[9] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[1] = COLOR_VALUE
    cp.pixels[8] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[2] = COLOR_VALUE
    cp.pixels[7] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[3] = COLOR_VALUE
    cp.pixels[6] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[4] = COLOR_VALUE
    cp.pixels[5] = COLOR_VALUE

def left_animation():
    #cp.pixels.brightness = 0.3
    cp.pixels[7] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[8] = COLOR_VALUE
    cp.pixels[6] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[9] = COLOR_VALUE
    cp.pixels[5] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[0] = COLOR_VALUE
    cp.pixels[4] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[1] = COLOR_VALUE
    cp.pixels[3] = COLOR_VALUE
    time.sleep(0.1)
    cp.pixels[2] = COLOR_VALUE

def main():
    while True:
        x, y, z = cp.acceleration
        #print(f"{x},{y},{z}")
        if z >= THRESHOLD_UP:
            print("HAND DOWN")
            time.sleep(0.1)
        else:
            if x < THRESHOLD_RIGHT:
                print("RIGHT")
                time.sleep(0.5)
                #while x < THRESHOLD_RIGHT:
                right_animation()
                time.sleep(0.1)
                cp.pixels.fill((0, 0, 0))
                time.sleep(0.1)
            elif y < THRESHOLD_LEFT:
                print("LEFT")
                time.sleep(0.5)
                left_animation()
                time.sleep(0.1)
                cp.pixels.fill((0, 0, 0))
                time.sleep(0.1)

main()
