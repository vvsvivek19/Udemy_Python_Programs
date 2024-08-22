import csv
import pprint

# Open the CSV file for reading
f = open(r'D:\Dev Role Prep\Tutorial Practice Codes\Udemy_Python_Programs\OS_Module\Employees1.csv')

# Create a CSV DictReader object to read the file as a dictionary
rdr = csv.DictReader(f)

# Create a dictionary where the key is the employee's name and the value is the entire row for that employee
emp_dict = {row['Name']: row for row in rdr}

# Use pprint to print the dictionary in a formatted way
pprint.pprint(emp_dict)

# Print the details of the employee named 'Harry'
print('Harry =', emp_dict['Harry'])

# Close the file
f.close()
