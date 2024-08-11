#hours = [int(x) for x in input("Please enter the daily hours separated by space").split()]
hours = []
print("Please first enter all the working hours for each day!")
for x in range(5):
    hours.append(int(input("Enter hours: ")))
Total_hours = 0
Hourly_wage = int(input("Please Enter Hourly wage: "))
for x in range(len(hours)):
    Total_hours = Total_hours + hours[x]
Weekly_salary = Total_hours * Hourly_wage
print("Weekly Salary:", Weekly_salary)
