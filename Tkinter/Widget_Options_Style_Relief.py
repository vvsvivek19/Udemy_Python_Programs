from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

def color_change(e):
    if int(e.type)==4:
        b1['activebackground'] = 'red'    
        b1['activeforeground'] = 'yellow'
        # b1['activeborderwidth'] = 3
    

b1 = Button(win,text='Button 1',bd='2m',bg='purple',fg='yellow',anchor=S,relief=RAISED,overrelief=RIDGE)
b1.pack()
b1.bind('<ButtonPress>',color_change)


win.mainloop()
