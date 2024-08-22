from tkinter import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

# Define the function that updates the listbox based on the selected option
def selected_option(selected):
    if selected == options[0]:
        list_var.set(languages)
    elif selected == options[1]:
        list_var.set(databases)
    elif selected == options[2]:
        list_var.set(clouds)

# def selected_option():
#     if var_opt.get() == options[0]:
#         list_var = Variable(value=languages)
#         list1.delete(0,END)
#         list1['listvariable'] = list_var
#     elif var_opt.get() == options[1]:
#         list_var = Variable(value=databases)
#         list1.delete(0,END)
#         list1['listvariable'] = list_var       
#     elif var_opt.get() == options[2]:
#         list_var = Variable(value=clouds)
#         list1.delete(0,END)
#         list1['listvariable'] = list_var       

# Options for the dropdown menu
options = ['Languages','Databases','Clouds']
var_opt = StringVar()
var_opt.set(options[0])
opt =  OptionMenu(win, var_opt,*options,command=selected_option)
opt.pack(pady=10)

# Lists corresponding to each option
languages = ['C++','c','Java','Python','JavaScript','Go Lang']
databases = ['MySQL','SQL Server','Postgres','Oracle']
clouds = ['AWS Cloud','Microsoft Azure','Google Cloud','Salesforce']

# Variable to control the content of the listbox
list_var = Variable(value=languages)
list1 = Listbox(win,selectmode=SINGLE,listvariable=list_var,width=30)
list1.pack(pady=10)

win.mainloop()