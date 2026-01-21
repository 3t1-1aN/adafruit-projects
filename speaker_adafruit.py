import time
from adafruit_circuitplayground.bluefruit import cpb
notes = [262, 294, 330, 349, 392, 440, 494, 523]  # C D E F G A B (oct 4)
color = (255, 255, 255)

def animation():
    cpb.pixels[0] = color
    cpb.pixels[9] = color
    time.sleep(0.1)
    cpb.pixels[1] = color
    cpb.pixels[8] = color
    time.sleep(0.1)
    cpb.pixels[2] = color
    cpb.pixels[7] = color
    time.sleep(0.1)
    cpb.pixels[3] = color
    cpb.pixels[6] = color
    time.sleep(0.1)
    cpb.pixels[4] = color
    cpb.pixels[5] = color
    time.sleep(0.1)
    cpb.pixels.fill([0, 0, 0])
    
while True:
    if cpb.touch_A1:
        cpb.start_tone(notes[0])
        animation()
    elif cpb.touch_A2:
        cpb.start_tone(notes[1])
        animation()
    elif cpb.touch_A3:
        cpb.start_tone(notes[2])
        animation()
    elif cpb.touch_A4:
        cpb.start_tone(notes[3])
        animation()
    elif cpb.touch_A5:
        cpb.start_tone(notes[4])
        animation()
    elif cpb.touch_A6:
        cpb.start_tone(notes[5])
        animation()
    elif cpb.button_a:
        cpb.start_tone(notes[6])
        animation()
    elif cpb.button_b:
        cpb.start_tone(notes[7])
        animation()
    else:
        cpb.stop_tone()

