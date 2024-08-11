from tkinter import *
import ttkbootstrap as tb

win = Tk()

win = tb.Window(themename='cyborg')

win.title('My First Application')

win.geometry('600x400+460+150')

l1 = tb.Button(win,text='Button 1')
l2 = tb.Button(win,text='Button 2')
l3 = tb.Button(win,text='Button 3')
l4 = tb.Button(win,text='Button 4')
l5 = tb.Button(win,text='Button 5')
l6 = tb.Button(win,text='Button 6')
l7 = tb.Button(win,text='Button 7')
l8 = tb.Button(win,text='Button 8')
l9 = tb.Button(win,text='Button 9')

l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=0,column=1,padx=5,pady=5)
l3.grid(row=0,column=2,padx=5,pady=5)

l4.grid(row=1,column=0,padx=5,pady=5)
l5.grid(row=1,column=1,padx=5,pady=5)
l6.grid(row=1,column=2,padx=5,pady=5)

l7.grid(row=2,column=0,padx=5,pady=5)
l8.grid(row=2,column=1,padx=5,pady=5)
l9.grid(row=2,column=2,padx=5,pady=5)

win.mainloop()
