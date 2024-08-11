class English:
    def greeting(self):
        print("Hello!🙂🙂")

class French:
    def greeting(self):
        print("Bonjour!🙂🙂")

def greet(language):
    language.greeting()

E = English()
F = French()

greet(E)
greet(F)