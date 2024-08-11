from threading import *
from time import *

class MyData:
    def __init__(self):
        self.data = 0
        self.cv = Condition()

    def put(self, d):
        self.cv.acquire()
        self.cv.wait(timeout=0)
        self.data = d
        self.cv.notify()
        self.cv.release()
        sleep(1)

    def get(self):
        self.cv.acquire() #sending request that it wants to lock 
        self.cv.wait(timeout=0)
        x = self.data
        self.cv.notify()
        self.cv.release()
        sleep(1)
        return x

def producer(data):
    i = 1
    while True:
        data.put(i)
        print('Producer has produced the value:',i)
        sleep(1)
        i +=1

def consumer(data):
    while True:
        x = data.get()
        sleep(1)
        print('Consumer gets the value:',x)

data = MyData()

t1 = Thread(target=lambda:producer(data))
t2 = Thread(target=lambda:consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()