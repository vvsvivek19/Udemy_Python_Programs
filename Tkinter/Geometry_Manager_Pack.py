from tkinter import *

win = Tk()

win.title('My First Application')

win.geometry('600x400+460+150')

l1 = Label(win,text='Label 1',bg='red',fg='yellow',font='Sans')
l1.pack(side = LEFT,fill=Y,padx=2,pady=2,ipadx=15,ipady=15)

l2 = Label(win,text='Label 2',bg='red',fg='yellow',font='Sans')
l2.pack(side= TOP,fill=X,padx=2,pady=2,ipadx=5,ipady=5)


l3 = Label(win,text='Label 3',bg='red',fg='yellow',font='Sans')
l3.pack(side=LEFT, fill=X, expand=1, padx=2,pady=2,ipadx=5,ipady=5)

l4 = Label(win,text='Label 4',bg='red',fg='yellow',font='Sans')
l4.pack(side=LEFT,fill=X,expand=1,padx=2,pady=2,ipadx=5,ipady=5)

win.mainloop()

