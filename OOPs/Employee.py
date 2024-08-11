class Employee:
    employee_count = 101
    def __init__(self,name,salary,designation):
        self.name = name
        self.salary = salary
        self.empid = 'e' + str(Employee.employee_count)
        self.designation = designation
        Employee.employee_count += 1
    def show_employee_details(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Employee ID:",self.empid)
        print("Designation:",self.designation)
    @classmethod
    def total_employees(cls):
        total = cls.employee_count - 101
        print("Total Employees in company: ", total)

E1 = Employee('Vivek',40000,'Associate Software Engineer')
E2 = Employee('Rakesh',90000, 'Lead Software Engineer')
E3 = Employee('Ananya',60000,'Project Manager')
E1.show_employee_details()
print('')
E2.show_employee_details()
print('')
E3.show_employee_details()
print('')
E3.total_employees()


