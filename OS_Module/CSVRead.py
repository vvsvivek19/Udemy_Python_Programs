import csv

f = open('employees.csv')
csv_reader = csv.reader(f)

next(csv_reader)

emp_id =[]
first_name = []
last_name = []
salaries = []

for col in csv_reader:
    emp_id.append(int(col[0]))
    first_name.append(col[1])
    last_name.append(col[2])
    salaries.append(int(col[7]))


# Find the index of the employee with the minimum salary and maximum salary
min_salary_index = salaries.index(min(salaries))
max_salary_index = salaries.index(max(salaries))

# Print the details of the employee with the minimum salary
print("Details of employee with minimum salary")
print('------------------------------------------')
print('Minimum Salary:', min(salaries))
print('Emp_ID:', emp_id[min_salary_index])
print('First Name:', first_name[min_salary_index])
print('Last_Name:', last_name[min_salary_index])


print('')
print("Details of employee with maximum salary")
print('------------------------------------------')
print('Maximum Salary:', max(salaries))
print('Emp_ID:', emp_id[max_salary_index])
print('First Name:', first_name[max_salary_index])
print('Last_Name:', last_name[max_salary_index])

f.close()