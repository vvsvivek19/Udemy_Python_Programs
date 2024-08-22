from tkinter import *

win = Tk()
win.title('CSV Data')
win.geometry('600x400+460+150')

f1 = LabelFrame(win,text='Frame 1',width=300,height=400,bg='red')
f1.pack(side=LEFT)
f2 = LabelFrame(win,text='Frame 2',width=300,height=400,bg='blue')
f2.pack(side=RIGHT)

b1 = Button(f1,text='Button 1')
b2 = Button(f1,text='Button 2')
b3 = Button(f1,text='Button 3')
b4 = Button(f1,text='Button 4')

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)



win.mainloop()