class Robot:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('Hi I am {}, I am a simple Robot with no function!'.format(self.name))
class PoliceRobot(Robot):
    def say_hi(self):
        print('Hi I am {}, I am here to help, Please be calm.'.format(self.name))

r = Robot('Max')
r.say_hi()

pr = PoliceRobot('RoboCop')
pr.say_hi()

