from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')
win.state('zoomed')

def my_handler():
    try:
        # print(lst_var.get())
        selected_items = [ lst1.get(i) for i in lst1.curselection()]
        # print(selected_items)
        if selected_items:
            ent_var.set(','.join(selected_items))
        else:
            ent_var.set('No Selection')
    except Exception as e:
        ent_var.set(f'Error {e}')


def my_inserter():
    try:
        lst1.insert(int(ent_var2.get())-1,ent_var3.get())
    except Exception as e:
        ent_var.set(f'Error {e}')


ent_var = StringVar()
ent1 = Entry(win, width=50,textvariable=ent_var)
ent1.pack(pady=10)

lbl1 = Label(win,text='Select your favorite programming languages')
lbl1.pack()

lst_var = StringVar()
lst1 = Listbox(win,selectmode=MULTIPLE,listvariable=lst_var)
languages = [ 'Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'C Language',
    'PHP', 'C#', 'R', 'Swift', 'Android', 'VB', 'PERL', 'Kotlin',
    'Go', 'Scala']
for index,language in enumerate(languages):
    lst1.insert(index,language)
lst1.pack(pady=10)

btn1 = Button(win,text='SELECT',command=my_handler)
btn1.pack(pady=10)

lbl2 = Label(win, text='Want to enter a item?')
lbl2.pack(pady=10)


lbl_index = Label(win,text='Enter the position')
lbl_index.pack()
ent_var2 = StringVar()
ent2 = Entry(win, width=30,textvariable=ent_var2)
ent2.pack(pady=10)


lbl_language = Label(win,text='Enter the Language')
lbl_language.pack()
ent_var3 = StringVar()
ent3 = Entry(win, width=30,textvariable=ent_var3)
ent3.pack(pady=10)

btn2 = Button(win,text='INSERT',command=my_inserter)
btn2.pack(pady=10)

win.mainloop()