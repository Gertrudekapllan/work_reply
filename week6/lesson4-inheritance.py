# наследование

class Doctor:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def health(self):
        print("лечить пациента")


class Parent:

    def __init__(self, count_baby):
        self.count_baby = count_baby

    def be_parent(self):
        print("воспитывать детей!!!")


class Dantist(Parent, Doctor):

    def __init__(self, count_baby, name, age, gender, exp):
        # Doctor.__init__(self, name, age, gender)
        Parent.__init__(self, count_baby)
        Doctor.__init__(self, name, age, gender)
        self.exp = exp

    def earn(self, money):
        self.wallet = money


dastan = Dantist(3, "Dastan", 20, "male", 5)
baha = Doctor("Baha", 27, "male")
print(dastan.__dict__)
baha.health()
dastan.health()
dastan.earn(23456664)
print(dastan.wallet)


class C():
    pass


class A(C):
    def test(self):
        print("i am test A")


class B(A):
    def test(self):
        return 3 + 7


class D(B, C):
    def test(self):
        old_test = A.test(self)
        print(old_test)


test_obj = D()
test_obj.test()
from functools import reduce

# Создайте три класса: Person, Student и Teacher.
# Класс Person должен содержать атрибуты name и age.
# Класс Student должен наследовать от Person и добавить атрибут
# student_id. Класс Teacher также должен наследовать от Person и
# добавить атрибут employee_id. Создайте объекты для каждого класса и выведите их атрибуты.

score_nazi = [("python", 243), ("python1", 213), ("python2", 223), ("python3", 233), ("python4", 423), ]


class Person:
    def __init__(self, name, age):
        self.avg = None
        self.name = name
        self.age = age

    def get_info(self):
        print(self.name, self.age, self.avg)


class Student(Person):

    def __init__(self, name, age, student_id, score):
        super(Student, self).__init__(name, age)
        self.student_id = student_id
        self.avg = reduce(lambda a, b: (None, a[1] + b[1]), score)[1] / len(score)


class Teacher(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


onj1 = Person("Test", 56)
nazi = Student("Nazi", 27, 1232, score_nazi)
nazi.get_info()
onj1.get_info()
