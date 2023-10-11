#ПОЛИМОРФИЗМ
# полиморфизм
# # ПОЛИМОРФИЗМ
# # реализовать класс Student  который принимает в аргументы full_name, age, course
# # также создать @classmethod который создает объект по full_name, year, admission(год поступления)
# # и создать   @staticmethod который возвращает по admission(год поступления) курс
# from datetime import date
#
# class Student:
#
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     @classmethod
#     def make_student_from_year(cls, name, year, course_year):
#         my_age = 2023 - year
#         course = cls.return_course(course_year)
#         return cls(name, my_age, course)
#
#     @staticmethod
#     def return_course(course_year):
#         return 2023 - course_year
#
#     def info(self):
#         print(self.age, self.name, self.course)
#
#
# dastan = Student("Omurkanov Dastan", 22, 3)
# baha = Student.make_student_from_year("Usenov Bahtyar", 2000, 2020)
# dastan.info()
# baha.info()

# Создайте класс Employee,
# представляющий сотрудника организации, с атрибутами,
# такими как имя, фамилия, зарплата и статической переменной,
# отслеживающей общее количество сотрудников.
# Добавьте статический метод get_employee_count,
# который будет возвращать общее количество сотрудников.
# добавить классметод который принимает в виде строки все данные отделенными запятой и должен создать обьект
# Employee(name, surname, salary)
# "name, surname, salary"
# написать метод который принимает процент повышения salary и установить новое значение salary
class Employee:
    employee_count = 0

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        Employee.employee_count += 1

    @classmethod
    def new_obj(cls, employee_str: str):

        my_list = employee_str.split()
        # return cls(my_list[0], my_list[1], int(my_list[2]))
        return cls(*my_list)

    def procent(self, procent):
        # проент добавления к зп
        # Добавить проетк текущему зп
        # установить
        summa = self.salary / 100 * procent
        print(summa, procent)
        print(summa + self.salary)
        self.salary += summa
        print(self.salary)





nazi = Employee("Nazgul", "Tabyldieva", 130000)
anya = Employee.new_obj("Anya Polivanova 145000")
# print(type(nazi.salary))
# print(type(anya.salary))
# print(Employee.employee_count)
anya.procent(20)
# +, *

# print(3 + 4)
# print("3" + "4")
# print(["3", ] + ["4",])

# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print("I am Dog, my name is {}".format(self.name))
#
#     def make_sound(self):
#         print("gav gav")


# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print("I am cat, my name is {}".format(self.name))
#
#     def make_sound(self):
#         print("mew mew")


# pitbul = Dog("Grisha")

#
# bengal = Cat("Test")
# bengal1 = Cat("Test2")
# object_list = [pitbul1, bengal, bengal1, pitbul]
#
# for i in object_list:
#     i.info()
#     i.make_sound()
#
# class Pitbul(Dog):
#
#     def make_sound(self):
#         print("gav gav mrr mrr")
#
#
# obj = Pitbul("Dog")
# obj.info()
# obj.make_sound()
# pitbul1 = Dog("Grisha3")
# pitbul1.make_sound()

# staticmethod, classmethod, instance method

# def area(r):
#     import math
#     return math.pi * r ** 2


# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def make_pizza(self):
#
#         print("Pizza consist of {0} area: {1}".format(self.ingredients, self.area(15)))
#
#     @classmethod
#     def fabric_pizza(cls):
#         print(cls.area(34))
#         return cls(["ananas", "cheese mazarella", "cheese dorblu", "potato"])
#
#     @staticmethod
#     def area(r):
#         import math
#         return math.pi * r**2


# obj = Pizza(["mozarella", "tomato", "cheese cheder"])
# obj.make_pizza()
# print(obj.area(15))
# obj2 = Pizza.fabric_pizza()
# obj2.make_pizza()
# print(Pizza.area(25))
