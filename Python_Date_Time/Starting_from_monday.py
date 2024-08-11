import datetime
year = int(input("Please Enter a year: "))
count = 0
for i in range(1,13):
    dat = datetime.date(year,i,1)
    if dat.weekday() == 0:
        count += 1
        print(i)
print("Number of Months in year {} starting with Monday are {}".format(year,count))
