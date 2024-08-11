from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

def myHandler():
    if var1.get() == 1:   #this var.get() is new, I didn't knew about it
        lb1['text'] = cb1['text']  
    else:
        lb1['text'] = ''
    if var2.get() == 1:
        lb1['text'] += cb2['text'] #concatenation
    else:
        lb1['text'] += ''
    if var3.get() == 1:
        lb1['text'] += cb3['text']
    else:
        lb1['text'] += ''
        
def buthandler():
    cb1.invoke()

lb1 = Label(win,text='')
lb1.pack()

var1 = IntVar() #value of this variable is 1 if Checkbutton is checked and 0 is if it is unchecked
cb1 = Checkbutton(win,text='Java',command=myHandler,variable=var1)
cb1.pack()

var2 = IntVar()
cb2 = Checkbutton(win,text='Python',command=myHandler,variable=var2)
cb2.pack()

var3 = IntVar()
cb3 = Checkbutton(win,text='C++',command=myHandler,variable=var3)
cb3.pack()

# but1 = Button(win,text='CLICK ME',command=buthandler)
# but1.pack()


win.mainloop()