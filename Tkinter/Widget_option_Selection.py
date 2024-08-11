from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

e1 = Entry(win, selectforeground='yellow',selectbackground='black',selectborderwidth=10)
e1.pack()

l1 = Listbox(win,selectforeground='yellow',selectbackground='black')
l1.insert(0,'AAAA')
l1.insert(1,'BBBB')
l1.insert(2,'CCCC')
l1.insert(4,'DDDD')
l1.pack()

win.mainloop()
