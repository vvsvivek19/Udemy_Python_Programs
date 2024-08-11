from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

b1 = Button(win,text='Button 1',bg='black',fg='yellow')
b2 = Button(win,text='Button 2',bg='lightblue',fg='blue')
b3 = Button(win,text='Button 3',bg='lightblue',fg='blue')

b1.place(relx=0.45,rely=0.45,relheight=0.1,relwidth=0.2)
# b2.place(x=250,y=200,width=150,height=100)
# b3.place(x=400,y=300,width=150,height=100)

win.mainloop()

