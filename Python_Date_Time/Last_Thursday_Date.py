import datetime

weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
day = input('Enter the day you want to know the date of from last week: ')
day = day.lower()


def prev_day(day):
    today = datetime.date.today()
    t_wd = today.weekday()
    dw = weekday.index(day)
    diff = dw - t_wd
    if diff < 0:
        new_date = today + datetime.timedelta(diff)
    else:
        new_date = today - datetime.timedelta(7 - diff)
    return new_date


print('Today:', datetime.date.today())
print('Previous:',prev_day(day))
