from threading import *
from time import *

# def display():
#     for i in range(65, 91):
#         print(chr(i))
#         sleep(0.7)

class Alphabets(Thread):
    def run(self):
        for i in range(65, 91):
            print(chr(i))
            sleep(0.7)
# t = Thread(target=display,name='Aplhabets')
t = Alphabets()
t.start()
for i in range(65,91):
    print(i)
    sleep(0.7)
t.join()