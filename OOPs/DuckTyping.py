def Driver(car):
    car.drive()

class Creta:
    def drive(self):
        print('Creta in driving')

class Mercedes:
    def drive(self):
        print('Mercedes is driving')

def PetLover(pet):
    pet.talk()
    pet.walk()

class Duck:
    def talk(self):
        print('Ducking is Talking')
    def walk(self):
        print('Duck in walking')\

class Dog:
    def talk(self):
        print('Dog is Talking')
    def walk(self):
        print('Dog in walking')

p = Dog()
PetLover(p)