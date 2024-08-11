from tkinter import *
from tkinter.font import *

win = Tk()
win.geometry('600x400+460+150')
win.title('My First App')

counter = 0

def myhandler():
    global counter
    counter += 1
    lb1['text'] = str(counter)

fnt = Font(family='Sans',size=30)

lb1 = Label(win,text='',font=fnt)
lb1.pack()

bt1 = Button(win,text='CLICK TO COUNT',command=myhandler,font=fnt)
bt1.pack()


win.mainloop()