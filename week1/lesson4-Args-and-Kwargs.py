# Задача 1 Напишите функцию `max_value`, которая принимает произвольное число аргументов
# и возвращает максимальное значение среди них.
# Пример использования:
# print(max_value(1, 2, 3, 4, 5))
# Вывод:5
# Первое решение:
def max_value_standard(*nums):
    maxx = max(nums)
    print("Max: ", maxx)


max_value_standard(0, -19, 3, 5, 66)
max_value_standard(23, 223, 453)


# Второе решение:
def max_value_manual(*nums):
    n_max = 0
    for n in nums:
        if n >= n_max:
            n_max = n
    return n_max


result = max_value_manual(1, 23, 4, 5, -12)
print(result)


# Задача 2 Напишите функцию `merge_lists`, которая принимает произвольное число списков в виде
# аргументов *args и возвращает новый список, содержащий все элементы этих списков.
# Пример использования:
# print(merge_lists([1, 2, 3], [4, 5], [6, 7, 8, 9]))
# Вывод:
m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [11, 21, 35, 24, 53, 64, 73, 82, 95]


def merge_lists(*args):
    c = []
    for el in args:
        c = c + el
    return c


result = merge_lists(f, m)
print(result)


# Задача 3 Напишите функцию `print_user_data`, которая принимает произвольное число именованных
# аргументов **kwargs,представляющих информацию о пользователе (имя, возраст, город и т.д.), и
# выводит эту информацию в отформатированном виде.
# Пример использования:
# print_user_data(name="John", age=30, city="New York", occupation="Programmer")
# Вывод:
# Name: John
# Age: 30
# City: New York
# Occupation: Programmer

def print_user_data(**some_information):
    data = {}
    for i, l in some_information.items():
        print(f"{i}: {l}")
        data.update({i: l})
    # print(data)


print_user_data(name="John", age=30, city="New York", occupation="Programmer")
