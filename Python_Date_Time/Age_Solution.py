import datetime
from datetime import date


def age(dob):
    today = date.today()
    years = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.year):  # Comparing two tuples
        years -= 1
    return years


print("Age: ", age(date(1998, 2, 19)))
