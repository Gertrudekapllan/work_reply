# Задача 1 Напишите функцию с именем add_excitement, которая берет список строк и добавляет
# восклицательный знак (!) в конец каждой строки в списке. Программа должна изменить исходный список
# и ничего не возвращать.2. (а)(b) Напишите ту же функцию, за исключением того, что она не должна
# изменять исходный список и вместо этого должна возвращать новый список.

weather_conditions = ["sunny", "cloudy", "rainy", "windy", "stormy", "snowy", "foggy", "hot", "cold", "hail"]


def add_excitement(list, changeable=True):
    if changeable:
        i = 0
        while i < len(list):
            list[i] = list[i] + "!"
            i += 1
        return list
    else:
        list_new = []
        i = 0
        while i < len(list):
            list_new.append(list[i] + "!")
            i += 1
        return list_new


result = add_excitement(weather_conditions, False)
print(result)
print(weather_conditions)

# Задача 2 Напишите функцию match, которая принимает две строки в качестве аргументов и возвращает количество
# совпадений между строками. Совпадение — это когда две строки имеют один и тот же символ с одним и тем же
# индексом. Например, «python» и «path» совпадают в первом, третьем и четвертом символах, поэтому функция должна
# вернуть 3.

a = "abcdeaa"
b = "abcdf"


def match(a, b):
    count = 0
    if len(a) > len(b):

        for i, l in enumerate(b):
            if a[i] == b[i]:
                count += 1
    else:
        for i, l in enumerate(a):
            if a[i] == b[i]:
                count += 1
    return count


result = match(a, b)
print(result)

# Задача 3 Напомним, что если s является строкой, то s.find('a') найдет расположение первого символа a в s.
# Проблема в том, что он не находит местоположение каждого a. Напишите функцию findall, которая по заданной
# строке и одному символу возвращает список, содержащий все местоположения этого символа в строке.
# Он должен возвращать пустой список, если в строке нет вхождений символа.

s = "qwertyqwertyqwerty"


def find_all(srtr, char):
    index_list = []
    for index, letter in enumerate(srtr):
        if letter == char:
            index_list.append(index)
    return index_list


result = find_all(s, "r")
print(result)
