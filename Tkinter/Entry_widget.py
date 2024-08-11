from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

def validate_handler(txt):
    if txt.isdigit(): #this will allow only digits to enter
        return True
    else:
        return False

validate_register = (win.register(validate_handler),'%S')

# ent1_var = StringVar(value='Welcome!')
ent1_var = StringVar()
ent1 = Entry(win,textvariable=ent1_var,validate='key',validatecommand=validate_register)
ent1.pack()
ent1.focus()
# ent1.icursor(8)
# ent1.select_to(9)

'''
Beyond this there are insert and delete methods also. Insert takes a index value and the content that you want to insert. Where as delete takes starting and ending index to delete the data present in Entry widget.

You can also use the option show to mask the data in entry. For example use show = *, with this data in entry field will be masked with *. 
'''

win.mainloop()