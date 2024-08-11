import datetime as dt

yr = int(input("Please Enter the year you want to see all Sunday's of: "))
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def all_sunday(year):
    first_date = dt.date(year, 1, 1)
    first_date_weekday = first_date.weekday()
    first_sunday_diff = 6 - first_date_weekday
    first_sunday_date = first_date + dt.timedelta(first_sunday_diff)
    print(first_sunday_date)
    next_sunday_date = first_sunday_date + dt.timedelta(7)
    while next_sunday_date.year == year:
        print(next_sunday_date)
        next_sunday_date = next_sunday_date + dt.timedelta(7)


all_sunday(yr)
