from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

can1 = Canvas(win,bg='yellow',width=600, height=400)
can1.pack()

can1.create_arc(100,100,200,200,fill='red',width=3,style=ARC)




win.mainloop()