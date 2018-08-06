from adafruit_circuitplayground.express import cpx
import time
import simpleio
pink = (40, 0, 30)
turquoise = (34, 125, 108)
yellow = (40, 20, 0)
off = (0, 0, 0) 
while True:
    if cpx.button_a:
        cpx.pixels.fill(yellow)
    if cpx.button_b:
         cpx.play_file("coin.wav")
    