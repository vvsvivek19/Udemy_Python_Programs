from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

t1 = Text(win,insertbackground='red',insertwidth=7,insertontime=10,insertofftime=50,cursor='spider')
t1.pack()

win.mainloop()