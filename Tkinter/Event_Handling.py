from tkinter import *

win = Tk()
win.title('Handling Events')
win.geometry('600x400+450+150')


def fun(msg):
    print(msg)


b1 = Button(win, text='My Button', command=lambda: fun('Button 1 is clicked'))
b1.pack()

b2 = Button(win, text='My Button', command=lambda: fun('Button 2 is clicked'))
b2.pack()

win.mainloop()
