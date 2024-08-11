import datetime
str_date = input("Please Enter the date in DD-MM-YYYY Format: ")
d,m,y = str_date.split('-')
dt = datetime.date(int(y),int(m),int(d))
print(dt)