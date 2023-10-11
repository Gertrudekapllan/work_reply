import random
import uuid


class BankAccount:
    name = "RSK"

    # def __init__(self, owner, balance=0):
    #     self.owner = owner
    #     self.balance = balance
    def register(self, full_name, password):
        self.full_name = full_name
        self.__password = password
        self.__wallet = 0
        self.__pin_code = random.randint(1000, 9999)
        self.__account = uuid.uuid4()

    def deposit(self, money, account):
        if account == self.__account:
            self.__wallet += money
        else:
            raise Exception("Неверные цветные данные")

    def my_account(self, password):
        if password == self.__password:
            return self.__account

    def spend_wallet(self, pin_code, cash=None):
        if cash:
            if pin_code == self.__pin_code:
                if cash <= 25000:
                    if cash <= self.__wallet:
                        self.__wallet -= cash
                    else:
                        raise Exception("НЕДОСТАТОЧНО СРЕДСТВ")
                else:
                    raise Exception("Вы превысили лимит")
            else:
                raise Exception("Вы ввели неправильный ПИН")
        else:
            print(self.__wallet)

    @property
    def get_pin_code(self):
        return self.__pin_code


nana = BankAccount()
nana.register("Nananova Nana", "nana")
my_code = nana.my_account("nana")
nana.deposit(234567, my_code)
pin_code = nana.get_pin_code
nana.spend_wallet(pin_code=pin_code)


