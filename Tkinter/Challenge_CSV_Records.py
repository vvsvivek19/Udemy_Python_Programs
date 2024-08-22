from tkinter import *
import csv

#handler function for Option Menu
def fetch_data(selected):
    i = employee_id.index(var_opt_menu.get())
    var_empid.set(data[i][0])
    var_name.set(data[i][1])
    var_phone.set(data[i][4])
    var_salary.set(data[i][7])

# Button Functionality
def update_data():
    i = employee_id.index(var_opt_menu.get())
    data[i][0] = var_empid.get()
    data[i][1] = var_name.get()
    data[i][4] = var_phone.get()
    data[i][7] = var_salary.get()

def save_data():
    file_csv.close()
    write_csv = open(r'D:\Dev Role Prep\Tutorial Practice Codes\Udemy_Python_Programs\Tkinter\employees.csv','w',newline='')
    wrtr = csv.writer(write_csv)
    wrtr.writerow(headings)
    wrtr.writerows(data)
    write_csv.close()
    win.quit()

win = Tk()
win.title('CSV Data')
win.geometry('+460+150')

# Creating a option menu filled with employee names
employee_list_label = Label(win,text='Employee List')
employee_list_label.grid(row=0,column=0,columnspan=2)

# opening csv file and creating a Dictionary Reader object
file_csv = open(r'D:\Dev Role Prep\Tutorial Practice Codes\Udemy_Python_Programs\Tkinter\employees.csv')
reader = csv.reader(file_csv)
headings = next(reader)
data = [row for row in reader]

employee_id = []
for row in data:
    employee_id.append(row[0])

var_opt_menu = StringVar(value=employee_id[0])
opt_menu = OptionMenu(win,var_opt_menu,*employee_id,command=fetch_data)
opt_menu.grid(row=0,column=2, columnspan=2)

# Creating a simple form
empid_label = Label(win,text='Employee ID')
empid_label.grid(row=1,column=0)
var_empid = StringVar()
empid_entry = Entry(win,textvariable=var_empid)
empid_entry.grid(row=1,column=1)

name_label = Label(win,text='Name')
name_label.grid(row=1,column=2)
var_name = StringVar()
name_entry = Entry(win,textvariable=var_name)
name_entry.grid(row=1,column=3)

salary_label = Label(win,text='Salary')
salary_label.grid(row=2,column=0)
var_salary = StringVar()
salary_entry = Entry(win,textvariable=var_salary)
salary_entry.grid(row=2,column=1)

phone_label = Label(win,text='Phone')
phone_label.grid(row=2,column=2)
var_phone = StringVar()
phone_entry = Entry(win,textvariable=var_phone)
phone_entry.grid(row=2,column=3)

# Buttons
update_button = Button(win,text='UPDATE',command=update_data)
update_button.grid(row=3,column=0,columnspan=2)

savexit_button = Button(win,text='SAVE & EXIT',command=save_data)
savexit_button.grid(row=3,column=2,columnspan=2)

win.mainloop()

