from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title('Event Binding')
win.geometry('600x400+450+150')


def fun(event):
    showinfo('My Box', 'Event is generated!')


e1 = Entry(win, bg='black', fg='yellow')
e1.place(x=200, y=100, width=200, height=50)

e2 = Entry(win, bg='black', fg='yellow')
e2.place(x=200, y=160, width=200, height=50)

e3 = Entry(win, bg='black', fg='yellow')
e3.place(x=200, y=220, width=200, height=50)

# e.bind('<Shift - Button-1>', fun) #instance level binding

# win.bind_class('Entry','<Button-1>',fun) #Class level binding

win.bind_all('<Button-1>', fun)  #Application Level Binding

win.mainloop()
