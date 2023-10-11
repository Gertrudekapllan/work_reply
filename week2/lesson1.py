# # 1:
# # Вычислить мощность электрического чайника.
# # Формула: P = T * A,
# # power -мощность, tension - напряжение, amperage - сила тока.
# # tension и amperage даны в качестве атрибутов функции
def kettle_power(tension, amperage):
    power = tension * amperage
    return power


# Пример использования функции для чайника с напряжением(tension) 220 В и силой тока(amparage) 10 А
tension_kettle = int(input("Введите напряжение:"))  # вольты #220
amperage_kettle = int(input("Введите силу тока:"))  # амперы #10
result = kettle_power(tension_kettle, amperage_kettle)
print("Мощность чайника:", result, "ватт")
#
#
# # Второй вариант проще:
# def get_power(U, I):
#     P = U * I
#     return P
#
#
# print(get_power(220, 10))
# import math
#
#
# # 2:
# # Вычислить объем цилиндра.
# # Формула объема цилиндра V = π * r^2 * h
# # Высота и радиус даны в качестве атрибутов функции, π = 3.14.
# def get_volume(r, h):
#     s = math.pi * (r ** 2)
#     v = s * h
#     print(s, h)
#     return v
#
#
# print(int(get_volume(7, 9)))
#
#
# # Напишите программу, которая рассчитает сколько бензина израсходовал транспорт в ср. на 100 км.
# # Формула: Расход = литры израсходованные на дорогу / пройденный путь * 100
# def get_fuel_consumption(length_km, litres):
#     result = (litres / length_km) * 100
#     return result
#
#
# print(get_fuel_consumption(157, 13))
import os

# Напишите программу, которая принимает имя файла и выводит его расширение.
# Расширения файлов - png,jpeg,html,doc,xlsx
# Если расширение будет не из ожидаемого списка, функция должна вернуть None.
# ПРИМЕР:
# >>> get_extension("my_photo.png")
# >>> "Расширение файла - png"
# >>> get_extension("my_photo.dkjkdfj")
# >>> None
extension = ["png", "jpeg", "html", "doc", "xlsx"]


def get_extension(filename):
    file_name = filename.split(".")[-1]
    for i in extension:
        if i == file_name:
            print(i, file_name)
            return (f"Расширение файла - {i}")
    else:
        print("Что-то пошло не так")


print(get_extension("get.html"))
