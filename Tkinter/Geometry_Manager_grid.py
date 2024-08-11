from tkinter import *

win = Tk()

win.title('My First Application')

win.geometry('600x400+460+150')

l1 = Button(win, text='Button 1', bg='lightblue', fg='blue')
l2 = Button(win, text='Button 2', bg='lightblue', fg='blue')
l3 = Button(win, text='Button 3', bg='lightblue', fg='blue')
l4 = Button(win, text='Button 4', bg='lightblue', fg='blue')
l5 = Button(win, text='Button 5', bg='lightblue', fg='blue')
l6 = Button(win, text='Button 6', bg='lightblue', fg='blue')
l7 = Button(win, text='Button 7', bg='lightblue', fg='blue')
l8 = Button(win, text='Button 8', bg='lightblue', fg='blue')
l9 = Button(win, text='Button 9', bg='lightblue', fg='blue')

l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=0, column=1, padx=5, pady=5)
l3.grid(row=0, column=2, padx=5, pady=5)

l4.grid(row=1, column=0, padx=5, pady=5)
l5.grid(row=1, column=1, padx=5, pady=5)
l6.grid(row=1, column=2, padx=5, pady=5)

l7.grid(row=2, column=0, padx=5, pady=5)
l8.grid(row=2, column=1, padx=5, pady=5)
l9.grid(row=2, column=2, padx=5, pady=5)

win.mainloop()
