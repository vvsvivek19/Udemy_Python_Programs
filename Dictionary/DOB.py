birthdays = {
    'Sachin': '03/14/2003',
    'Carl': '01/17/2001',
    'Khan': '12/10/2006',
    'Donald': '06/14/2010',
    'Rohan': '01/6/2005'}
name = input("Please enter a name: ")
DOB = birthdays.get(name, 'Not present')
if DOB == 'Not present':
    print("Birthday not found")
else:
    print('Birthday is', DOB)
