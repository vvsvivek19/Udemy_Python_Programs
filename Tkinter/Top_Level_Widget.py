from tkinter import *
from tkinter import messagebox

class MyTop(Toplevel):
    def childhandler(self):
        messagebox.showinfo('Message','Child window message',parent=self)

    def __init__(self):
        Toplevel.__init__(self)
        bt1 = Button(self,text='Button 1',command=self.childhandler)
        bt1.pack()


def myhandler():
    tp1 = MyTop()
    tp1.geometry('300x300+600+250')
    tp1.title('Child Window')
    tp1.mainloop()

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

btn1 = Button(win,text='Click Me', command=myhandler)
btn1.pack()

win.mainloop()