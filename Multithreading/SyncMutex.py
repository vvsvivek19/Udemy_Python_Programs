from threading import *
from time import *

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        sleep(0.7)
    l.release()
l = Lock()
t1 = Thread(target=display, args=('HELLO WORLD',))
t2 = Thread(target=display, args = (' You are welcome',))

t1.start()
t2.start()

t1.join()
t2.join()