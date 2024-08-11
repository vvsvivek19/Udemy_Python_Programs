date = input("Please enter the date in dd/mm/yyyy format: ")
split_date = date.split('/')
print("Date is:",split_date[0])
month_num = int(split_date[1])
if month_num == 1:
    print("It is January")
elif month_num == 2:
    print("It is February")
elif month_num == 3:
    print("It is March")
elif month_num == 4:
    print("It is April")
elif month_num == 5:
    print("It is May")
elif month_num == 6:
    print("It is June")
elif month_num == 7:
    print("It is July")
elif month_num == 8:
    print("It is August")
elif month_num == 9:
    print("It is September")
elif month_num == 10:
    print("It is October")
elif month_num == 11:
    print("It is November")
elif month_num == 12:
    print("It is December")
else:
    print("Invalid month number")
print("Year is:",split_date[2])
