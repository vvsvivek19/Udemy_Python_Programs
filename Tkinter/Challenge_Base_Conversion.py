from tkinter import *

win = Tk()
win.title('Base Conversion')
win.geometry('+460+150')

def update_label():
    try:
        if radio_var.get() == 0:
            main_label['text'] = str(value)
        elif radio_var.get() == 1:
            main_label['text'] = str(bin(value))
        elif radio_var.get() == 2:
            main_label['text'] = str(oct(value))
        elif radio_var.get() == 3:
            main_label['text'] = str(hex(value))
    except Exception as e:
        print(f'Cannot Perform Acction due some error: {e}')
         

value = 25
main_label = Label(win,text=str(value),font=('Times New Roman',30,'bold'))
main_label.grid(row=0,column=0,columnspan=4)

radio_var = IntVar(value=0)
decimal_rb = Radiobutton(win, text='Decimal',variable=radio_var,value=0,command=update_label)
decimal_rb.grid(row=1,column=0)
binary_rb = Radiobutton(win, text='Binary',variable=radio_var,value=1,command=update_label)
binary_rb.grid(row=1,column=1)
octal_rb = Radiobutton(win, text='Octal',variable=radio_var,value=2,command=update_label)
octal_rb.grid(row=1,column=2)
hexa_decimal_rb = Radiobutton(win, text='Hexa Decimal',variable=radio_var,value=3,command=update_label)
hexa_decimal_rb.grid(row=1,column=3)

win.mainloop()