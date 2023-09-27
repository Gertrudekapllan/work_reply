# Попросите пользователя ввести имя файла, а затем попытайтесь открыть этот файл для чтения.
# Обработайте исключение, которое может возникнуть, если файл не существует.:
# Создайте программу, которая запрашивает у пользователя число и пытается
# найти квадратный корень этого числа. Обработайте исключение, которое может возникнуть,
# если пользователь вводит отрицательное число.
from math import sqrt

# 1
name_file = str(input("Input file's name:"))
try:
    f = open(name_file, "r")
    print(f.read())
except IOError:  # some other IOError
    print("no file by that name")
# 2
simple_number = int(input("Input number:"))
try:
    print(sqrt(simple_number))
except:
    print("Does not")
