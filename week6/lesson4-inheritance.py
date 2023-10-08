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
# baha.health()
# dastan.health()
# dastan.earn(23456664)
# print(dastan.wallet)

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