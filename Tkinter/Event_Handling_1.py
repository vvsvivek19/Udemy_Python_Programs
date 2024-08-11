from tkinter import *

win = Tk()
win.title('Clicking Mouse')
win.geometry('600x400+450+150')


def hello(event):
    print('Single Click, Button-1')


def Quit(event):
    print('Double click. so lets stop!')


b = Button(win, text='Mouse Clicks', bg='black', fg='yellow')
b.place(relx=0.40, rely=0.40, relheight='0.10', relwidth='0.20')
b.bind('<Button-1>', hello)
b.bind('<Double-1>', Quit)

win.mainloop()
