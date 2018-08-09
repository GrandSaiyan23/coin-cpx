from adafruit_circuitplayground.express import cpx
import time
import simpleio
yellow = (40, 20, 0) 
while True:
    if cpx.button_a:
        cpx.pixels.fill(yellow)
    if cpx.button_b:
         cpx.play_file("coin.wav"
