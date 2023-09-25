# Задача 1
# Напишите программу, которая постоянно просит пользователя ввести названия продуктов и цены.
# Эта программа предназначена для создания словаря продуктов и их цен. Она будет запрашивать
# у пользователя названия продуктов и цены и сохранять их в словаре, где названия продуктов будут ключами,
# а цены - значениями. После того, как пользователь закончит вводить продукты и цены, программа будет позволять
# им повторно вводить названия продуктов и выводить соответствующую цену или сообщение, если товара нет в словаре.

def get_dict():
    dict_food = {}
    while True:
        print('Введите ENTER если хотите выйти')
        name_one = input("Введите наименование продукта:")
        if name_one == '':
            break
        sale = int(input('Введите стоимость продукта:'))
        dict_food[name_one] = sale
    return dict_food


d = get_dict()
print(d)

# Задача 2
# Используя словарь, созданный в предыдущей задаче, попросите пользователя ввести сумму
# и распечатайте все товары, цена которых меньше этой суммы.

sales = int(input('Введите СУММУ:'))
empty_list = []
for x, y in d.items():
    if y < sales:
        empty_list.append(x)
        print(x)
print(empty_list)
# Задача 3
# Напишите программу которая использует словарь, где ключами являются названия месяцев,
# а значениями - количество дней в каждом месяце.
# (a) Программа запрашивает у пользователя название месяца и выводит количество дней,
# находящихся в этом месяце, используя словарь.
# (b) Все ключи словаря выводятся в алфавитном порядке.
# (c) Программа выводит все месяцы, в которых 31 день.
# (d) Пары (ключ-значение) выводятся в порядке возрастания количества дней в каждом месяце.
dict_mounts = {"Январь": 31,
               "Февраль": 28,
               "Март": 31,
               "Апрель": 30,
               "Май": 31,
               "Июнь": 30,
               "Июль": 31,
               "Август": 31,
               "Сентябрь": 3,
               "Октябрь": 31,
               "Ноябрь": 30,
               "Декабрь": 31, }


def quantity_day_in_month():
    print(dict(sorted(dict_mounts.items())))
    print(sorted(dict_mounts.keys()))
    print(sorted(dict_mounts.values()))
    one_mount = input('Введите месяц:')
    one_mount = one_mount.title()
    print(one_mount)
    result = dict_mounts.get(one_mount)
    return result


print(quantity_day_in_month())

# Задача 4
# Напишите программу которая использует словарь, который содержит десять имен пользователей и соответствующие пароли.
# При запуске, она запрашивает у пользователя имя пользователя и пароль.
# Если имя пользователя отсутствует в словаре, программа сообщает, что человек не является действительным пользователем системы.
# Если имя пользователя есть в словаре, но пароль неверный, программа сообщает, что пароль недействителен.
# Если имя пользователя и пароль верные, программа сообщает, что пользователь вошел в систему.
dict_u_p = {"Состав Вагонов": "qqq", "Рулон Обоев": "aqddww", "Отряд Ковбоев": "rtrrtr",
            "Иссяк Запалов": "qqwwe", "Камаз Бокалов": "dfdfdf", "Стакан Сводоев": "cvcvc",
            "Мешок Лимонов": "hjhjhjj"
            }


def check_user():
    username = input("Введите имя пользователя:")
    password = input("Введите пароль пользователя:")
    if username not in dict_u_p:
        print("Имя пользователя отсутствует в словаре")
    elif password not in dict_u_p.values():
        print("PASSWORD DID NOT MUCH")
    else:
        print("Пользователь Вошелвсистемов")