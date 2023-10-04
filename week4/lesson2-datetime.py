# 1:Попросите пользователя ввести год, а затем используйте модуль datetime,
# чтобы проверить, является ли этот год високосным, и выведите результат.
# Високосным годом является тот год, который нацело делится на 4,
# кроме столетий (исключением являются столетия делящиеся на 400).


import calendar
from datetime import timedelta, datetime


def leap_year():
    year = int(input('Введите год: '))

    if calendar.isleap(year):
        print('Год високосный.')
    else:
        print('Год не високосный.')
    return year


result = leap_year()
print(result)


# 2:Попросите пользователя ввести две даты (начальную и конечную), а затем используйте модуль
# datetime для подсчета количества рабочих дней между этими датами, исключая выходные дни.
def count_working_days(start_date, end_date):
    delta = timedelta(days=1)
    count = 0
    while start_date <= end_date:
        if "Sun" != start_date.strftime("%a") != "Sat":
            count += 1
        start_date += delta
    return count


def input_and_format():
    start_date = input("please input start date in format dd/mm/yy:")
    end_date = input("please input finish date in format dd/mm/yy:")
    start_date = datetime.strptime(start_date, '%d/%m/%y')
    end_date = datetime.strptime(end_date, '%d/%m/%y')
    print(count_working_days(start_date, end_date))


input_and_format()
