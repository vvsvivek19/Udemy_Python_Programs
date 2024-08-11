class iPhone6:
    def home(self):
        print("Home button is pressed!")

class iphone10(iPhone6):
    def home(self): #method overriding
        print('Swipe up the nav bar to go home!')
        super().home() #super should be used inside the class defintion of child class


i6 = iPhone6()
i6.home()

i10 = iphone10()
i10.home()