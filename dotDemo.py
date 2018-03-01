#Matthew Suriawinata
#3/1/18
#dotDemo.py - how to use loops with graphics

from ggame import *

red = Color("0xFF000", 1)


dot = CircleAsset(25, LineStyle(1, red), red)

for i in range(12): #place row of dots
    for j in range(12):
        Sprite(dot, (10 + i*75 ,10+60*j))
    

App().run()





