import datetime

date_of_birth = input('Please Enter the DOB in DD-MM-YYYY format: ')
d, m, y = date_of_birth.split('-')

DOB = datetime.datetime(int(y), int(m), int(d))
DOB_year = DOB.year
DOB_month = DOB.month
DOB_day = DOB.day

Current_Date = datetime.datetime.today()
Today_year = Current_Date.year
Today_month = Current_Date.month
Today_day = Current_Date.day

age = 0

if Today_month < DOB_month:
    age = Today_year - DOB_year - 1
elif Today_month == DOB_month:
    if Today_day < DOB_day:
        age = Today_year - DOB_year - 1
    else:
        age = Today_year - DOB_year
else:
    age = Today_year - DOB_year

print("Age is years", age)
