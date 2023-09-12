# HOME ASSIGNMENT LISTS
# 1) Создать список своих любимых песен. Отсортировать список в алфавитном порядке и вывести его.
list_my_favorite = [" A Wind of Change", "Zaz", "Dust in the wind", "I miss you", "Sunny", "Total eclipse of the heart",
                    "Forever young"]
list_my_favorite.sort(reverse=False)
print(list_my_favorite)

# 2)Создать список из десяти элементов.
# Заполнить его случайными числами. Вывести этот список. Вывести наименьший элемент списка.

import random

arrey = []
for i in range(10):
    arrey.append(random.randint(7, 67))
print(arrey)
print(min(arrey))
n = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for i in range(len(n)):
    for j in range(len(n[i])):
        if j > i:
            n[i][j] = "#"
        elif j < i:
            n[i][j] = "*"
        else:
            n[i][j] = 0
for i in n:
    print(i)

# ЗАДАЧА 3)Заполнить массив из 5 элементов случайными числами в интервале [-100,100].
# Найти сумму всех отрицательных элементов массива.
# Если отрицательных элементов в массиве нет, вывести сообщение «отрицательных элементов нет».
mas = []
for i in range(5):
    mas.append(random.randint(-100, 100))
print(mas)
result = 0
for i in mas:
    if i < 0:
        result += i
if result == 0:
    print("Отрицательных элементов нет")
else:
    print(result)

# 4)Заполнить массив из 10 элементов случайными числами в интервале [-100,100]
# и переставить элементы так, чтобы все положительные элементы стояли в начала массива,
# а все отрицательные и нули – в конце. Пример: исходный массив: 20 -90 15 -34 10 0; результат: 20 15 10 0 -34 -90 .

import random

mas = []
for i in range(10):
    mas.append(random.randint(-100, 100))
result = sorted(mas, reverse=True)
print(result)
