from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title('Event Binding')
win.geometry('600x400+450+150')

# b1 = Entry(win, highlightbackground='red',highlightthickness=2,highlightcolor='yellow')
# b1 = Button(win,text='Button 1',state=ACTIVE,activebackground='red',activeforeground='yellow')
b1 = Listbox(win,activestyle=DOTBOX)
b1.insert(0,'a')
b1.insert(1,'b')
b1.insert(2,'c')
b1.insert(3,'d')
b1.pack()
b2 = Button(win,text='Button 2',takefocus=0)
b2.pack()
c1 = Checkbutton(win,text='Check Button 1',indicatoron=True) #indicator on removes the check marks and makes it a pushbutton
c1.pack()

win.mainloop()