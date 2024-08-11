import datetime as dt

year = input('Please Enter the date in DD-MM-YYYY: ')
d, m, y = year.split('-')
current_date = dt.date(int(y),int(m),int(d))
start_date = dt.date(int(y),1,1)
total_days = current_date - start_date
print('Total days:',total_days.days+1)