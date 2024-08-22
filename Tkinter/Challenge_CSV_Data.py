from tkinter import *
import csv

win = Tk()
win.title('CSV Data')
win.geometry('600x400+460+150')

# opening csv file and creating a Dictionary Reader object
f = open(r'D:\Dev Role Prep\Tutorial Practice Codes\Udemy_Python_Programs\Tkinter\employees.csv')

rdr = csv.DictReader(f)

# Handler function for option menu
def select_option(selected):
    if selected == options[0]:
        list_var.set(empid)
    elif selected == options[1]:
        list_var.set(name)
    elif selected == options[2]:
        list_var.set(salary)


# Options for option menu
options = ['EmpID','Name','Salary']
var_opt = StringVar()
var_opt.set(options[0])
opt = OptionMenu(win,var_opt,*options,command=select_option)
opt.pack()

# Creating lists to store EmpID, Name, Salary
empid = []
name = []
salary = []
for row in rdr:
    empid.append(row['EMPLOYEE_ID'])
    name.append(row['FIRST_NAME'])
    salary.append(row['SALARY'])


# Creating a Listbox
list_var = Variable(value=empid)
list1 = Listbox(win,selectmode=SINGLE,listvariable=list_var,width=30)
list1.pack()

win.mainloop()