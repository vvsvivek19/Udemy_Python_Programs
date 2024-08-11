from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

var = IntVar(value=20)

# s1 = Scale(win, from_ = 0, to=100,variable=var)
# s1.pack()

sb1 = Scrollbar(win,orient=VERTICAL)
t1 = Text(win)

t1.config(yscrollcommand=sb1.set) #connecting scroll bar with text widget
sb1.config(command=t1.yview) #configuring the vertical scroll command in scroll bar

sb1.pack(side=RIGHT,fill=Y)
t1.pack(side=LEFT,fill=Y)

win.mainloop()