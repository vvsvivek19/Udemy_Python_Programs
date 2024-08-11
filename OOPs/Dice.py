from random import *

class Dice:
    def  __init__(self,side=None):
        self.side = side
    def roll_dice(self):
        side_num = randint(1,self.side)
        print(side_num)

goti = Dice(6)
goti.roll_dice()
goti.roll_dice()
