# coordinates
# Ввести координаты. Определить четверть координатной плоскости, которой принадлежит точки.
# 1, 2, 3, 4 в числовом типе! Пример, '1', '4'


def determine_quarter_of_coordinate(x, y):
    if x > 0 and y > 0:
        return '1'
    elif x < 0 and y > 0:
        return '2'
    elif x < 0 and y < 0:
        return '3'
    elif x > 0 and y < 0:
        return '4'


result = determine_quarter_of_coordinate(1, 4)
print(result)
