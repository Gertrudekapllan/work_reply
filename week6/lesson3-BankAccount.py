# 1):Создайте класс BankAccount с атрибутом класса interest_rate и методами экземпляра deposit()
# и withdraw(). Метод deposit() увеличивает баланс на указанную сумму, а метод withdraw() уменьшает баланс.
# При создании объекта этого класса, установите начальный баланс и процентную ставку. Затем выполните несколько
# операций по депозиту и снятию средств, используя методы экземпляра, и выведите итоговый баланс.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Владелец счёта:\t\t{self.owner}\nБаланс счёта:\t\t{self.balance}$'

    def deposit(self, dep):
        self.balance += dep
        print(f'Поступило пополнение средств на карту в размере: {dep}$ \nБаланс счёта составляет: {self.balance}$')

    def withdraw(self, wi):
        if self.balance - wi < 500:
            print(f'Недостаточно средств!\nБаланс счёта составляет:{self.balance}$')
            return

        if self.balance >= wi:
            self.balance -= wi
            print(f'Снятие средств в размере: {wi}$ \nБаланс счёта составляет:{self.balance}$')
        else:
            print(f'Недостаточно средств!\nБаланс счёта составляет:{self.balance}$')

    def interest_rate(self, interest_rate):
        result = self.balance * interest_rate / 100
        print(f"Ваш баланс составляет:{self.balance}\n"
              f"Процентная ставка: {interest_rate}")

        return result


vlad = BankAccount(owner="vlad", balance=3030)
print(vlad.deposit(234))
print(vlad.withdraw(24))
print(vlad.withdraw(22224))
print(vlad.interest_rate(10))



# 2): Создайте класс Rectangle, у которого есть атрибуты экземпляра width и height. Добавьте
# метод экземпляра calculate_area(), который возвращает площадь прямоугольника (ширина * высота).
# Создайте объект этого класса и вызовите метод calculate_area().

class Rectangle():
    def __int__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self, width, height):
        return width * height


example = Rectangle()
print(example.calculate_area(20, 4))
print(example)


# 3): Создайте класс Counter, у которого есть атрибут экземпляра count со значением 0. Добавьте методы increment()
# и decrement(), которые увеличивают и уменьшают значение атрибута count. Создайте объект этого класса и вызовите
# методы для изменения значения count.

class Counter():
    count = 0

    def increment(self, count):
        count += 1
        return count

    def decrement(self, count):
        count -= 1
        return count


cou = Counter()
print(cou.increment(2))
