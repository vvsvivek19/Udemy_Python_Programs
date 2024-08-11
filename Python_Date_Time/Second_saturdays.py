import calendar
import datetime

year = int(input("Please Enter the year: "))
for month in range(1,13):
    current_month = calendar.monthcalendar(year,month)
    if current_month[0][5] == 0:
        print('Second Saturday for month',month,'is',datetime.date(year,month,current_month[2][5]))
    else:
        print('Second Saturday for month', month, 'is', datetime.date(year, month, current_month[1][5]))


