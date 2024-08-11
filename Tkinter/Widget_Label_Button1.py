from tkinter import *
from tkinter.font import *

win = Tk()
win.geometry('600x400+460+150')
win.title('My First App')

def myhandler():
   var.set(var.get()+1)

fnt = Font(family='Sans',size=30)

var = IntVar(value=0)
lb1 = Label(win,text='',font=fnt,textvariable=var)
lb1.pack()

bt1 = Button(win,text='CLICK TO COUNT',command=myhandler,font=fnt)
bt1.pack()


win.mainloop()