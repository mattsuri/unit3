#Matthew Suriawinata
#3/1/18
#dotDemo.py - how to use loops with graphics

from ggame import *

RADIUS = 10

red = Color("0xFF000", 1)


dot = CircleAsset(RADIUS, LineStyle(1, red), red)

for i in range(12 * 2*RADIUS+10): #place row of dots
    for j in range(12):
        Sprite(dot, (10 + i*(2*RADIUS+10) ,10+(2*RADIUS+10)*j))
    

App().run()





