
# Задача 1 Напишите декоратор, который проверяет, что результат функции является
# числом, и возвращает его. Если результат не является числом, декоратор
# должен вернуть None.

def check_type(func):
    def check_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is int:
            return result
        else:
            return None

    return check_wrapper


@check_type
def my_func(val):
    return val


print(my_func(3456))


# Задача 2 Напишите декоратор, который добавляет к результату функции префикс и суффикс.
# Префикс и суффикс должны задаваться при вызове декоратора.
# Пример:
def add_prefix_suffix(pref, suf):
    def decor(func):
        def wrapper(*args, **kwargs):
            result = pref + func(*args, **kwargs) + suf
            return result

        return wrapper

    return decor


@add_prefix_suffix("Result: ", "!")
def my_func():
    return "Hello, world"


print(my_func())
