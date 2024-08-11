students = dict()
flag = 0
while flag != 1:
    name = input("Please Enter the name of student: ")
    if name not in students:
        roll_no = int(input("Please Enter the roll Number"))
        Student_name = name
        Dept_name = input("Please Enter the Dept Name")
        students[name] = {'RollNo': None, 'Name':name, 'roll_no':roll_no}
    prompt = input("Do you wanna enter more details - Yes/No: ")
    if prompt == 'Yes' or prompt == 'yes':
        flag = 0
    else:
        flag = 1
print(students)
