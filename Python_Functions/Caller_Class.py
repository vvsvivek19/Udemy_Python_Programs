class Dept:
    def __init__(self):
        self.depts = {'hr': 'Human Resources',
                      'acc': 'Accounts and Finance Department',
                      'sd': 'Sales and Distribution',
                      'mft': 'Manufacturing Department'}

    def __call__(self, dept):
        return self.depts[dept]

d = Dept()
s = d('hr')
print(s)