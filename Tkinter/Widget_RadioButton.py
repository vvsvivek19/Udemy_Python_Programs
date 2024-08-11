from tkinter import *

win = Tk()
win.geometry('600x400+460+150')
win.title('My First App')

def myhandler():
    lb1['text'] = var.get()

lb1 = Label(win,text='')
lb1.pack()

#to bring all radiobuttons under one group we need a single variable, not multiple vairables like checkbuttons
#All radio Buttons need distinct Value in value option

var = StringVar()
rb1 = Radiobutton(win,text='Java',variable=var,value='Java',command=myhandler)
rb1.pack()
rb2 = Radiobutton(win,text='Python',variable=var,value='Python',command=myhandler)
rb2.pack()
rb3 = Radiobutton(win,text='C++',variable=var,value='C++',command=myhandler)
rb3.pack()


win.mainloop()