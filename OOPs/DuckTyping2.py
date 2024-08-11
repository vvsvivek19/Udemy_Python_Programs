class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self):
        print(self.name,'Says Meow Meow')

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self):
        print(self.name,'Says Bow Bow')

def my_pet(pet):
    pet.sound()

c = cat('Garfield',2)
d = dog('Blacky',3)

my_pet(d)
my_pet(c)