from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

img = PhotoImage(file='D:\\Dev Role Prep\\Tutorial Practice Codes\\Udemy-Python\\Tkinter\\dragon-ball-super-saiyan.gif')
lb1 = Label(win,text='Super Saiyan 1',image=img)
lb1.pack()



win.mainloop()