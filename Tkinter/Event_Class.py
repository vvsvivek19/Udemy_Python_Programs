from tkinter import *
from tkinter.messagebox import *

def my_handler(e):
    print(e)
    # print(e.state)
    # print(e.x_root,e.y_root)

win = Tk()
win.title('Event Binding')
win.geometry('600x400+450+150')

ent = Entry(win,bg='black',fg='yellow')
ent.place(relx=0.35,rely=0.40,relwidth=0.30,relheight=0.10)
ent.bind('<KeyPress>',my_handler)
win.mainloop()
