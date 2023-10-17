#Магические методы    #Magical methods
class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.diametr = radius * 2

    def __str__(self):
        return f"это круг с радиусом {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        result = None
        if isinstance(other, Circle):
            result = self.radius + other.radius
        elif type(other) == int:
            result = self.radius + other
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        result = None
        if isinstance(other, Circle):
            result = self.radius * other.radius
        elif type(other) == int:
            result = self.radius * other
        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    # def __sub__(self, other):
    #     pass
    # def __divmod__(self, other):
    #     pass

obj1 = Circle(12)
obj2 = Circle(16)
print(obj1 + 2)
print(2 + obj1)
# print(obj2 * obj2)
# print(obj1 + 5)
# print(5 + obj1)
# +, -, *, /
# print(obj1.__repr__())
# now_date = datetime.now()
# print(now_date)
# print(now_date.__repr__())
# a = datetime(2023, 10, 11, 9, 15, 19, 606457)
# print(type(a))

# ооп
# getattr() setattr(), delattr()


# class Car:
#
#     def __init__(self, model, color):
#         self.color = color
#         self.model = model
#
# mers = Car("mers", "white")
# name = "Nazi"
# print(getattr(name, "replace"))
# setattr(mers, "fuel", "test")
# delattr(mers, "models")
# print(mers.__dict__)
# print(hasattr(mers, "colors"))


# dunder methods магические сетоды
from datetime import datetime


# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#         self.diametr = radius * 2
#
#     def __str__(self):
#         return f"это круг с радиусом {self.radius}"
#
#     def __repr__(self):
#         return f"Circle({self.radius})"
#
#     def __add__(self, other):
#         result = None
#         if isinstance(other, Circle):
#             result = self.radius + other.radius
#         elif type(other) == int:
#             result = self.radius + other
#         return result
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#     def __mul__(self, other):
#         result = None
#         if isinstance(other, Circle):
#             result = self.radius * other.radius
#         elif type(other) == int:
#             result = self.radius * other
#         return result
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     # def __sub__(self, other):
#     #     pass
#     # def __divmod__(self, other):
#     #     pass
#
# obj1 = Circle(12)
# obj2 = Circle(16)
# print(obj1 + 2)
# print(2 + obj1)
# # print(obj2 * obj2)
# # print(obj1 + 5)
# # print(5 + obj1)
# # +, -, *, /
# # print(obj1.__repr__())
# # now_date = datetime.now()
# # print(now_date)
# # print(now_date.__repr__())
# # a = datetime(2023, 10, 11, 9, 15, 19, 606457)
# # print(type(a))

# class Rectangle:
#
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#
#     def area(self):
#         return self.side_b * self.side_a
#
#     def perimeter(self):
#         return (self.side_b + self.side_a) * 2
    #
    # def __eq__(self, other):
    #     if isinstance(other, Rectangle):
    #         return self.area() == other.area()
    #     return self.area() == other
    #
    # def __hash__(self):
    #     return hash((self.side_b + self.side_a, ))
    #  def __gt__(self, other):
    #      pass
    # def __lt__(self, other):
    #     pass
    #

# obj1 = Rectangle(3, 10)
# obj2 = Rectangle(5, 6)

# print(dir(obj2))
# print(hash(546))
# print(hash("tegdvd"))
# print(hash(["tegdvdd", ]))
# print(hash(("tegdvdd", )))
# print(hash(("tegdvdd", )))


# моносостояние
#
# class Minon:
#
#     atrs = {
#         "name": "Mini",
#         "eyes": 1,
#         "color": "yellow"
#     }
#
#     def __init__(self):
#         self.__dict__ = Minon.atrs
#
# min1 = Minon()
# min2 = Minon()
# print(min1.__dict__)
# print(min2.__dict__)
# min2.eyes = 2
# print(min1.__dict__)
# print(min2.__dict__)

