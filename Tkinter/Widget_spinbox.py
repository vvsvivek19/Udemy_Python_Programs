from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

#handler function
def myhandler():
    var.set(spb1.get())
    # spb1.selection('range',1,3)

shopping = ['Amazon','Flipkart','Myntra','eBay','Snapdeal','Meesho'] 

#Remember: Spinbox doesn't allow any insertion, so whatever values are there in the list will be the elements in Spinbox. You cannot add new elements like you can in Listbox

#Entry
var = StringVar()
en1 = Entry(win,textvariable=var)
en1.pack()

#Spinbox
# spb1 = Spinbox(win,from_=0.0,to=1.0,increment=0.01)
spb1 = Spinbox(win,values=shopping,state="readonly",wrap=True)
spb1.pack()

#Button
btn1 = Button(win,text='SELECT SITE',command=myhandler)
btn1.pack()

win.mainloop()