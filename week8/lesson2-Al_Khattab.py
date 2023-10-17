# Задача 1
# Создайте симулятор магазина, включая классы Product, Customer, Cart и Store. Класс Product
# должен иметь атрибуты, такие как название, цена и количество на складе. Класс Customer представляет
# клиента и имеет атрибут cart для добавления товаров. Класс Store управляет инвентарем и покупками.
# Реализуйте функциональность добавления товаров в корзину, расчет общей суммы и обновление инвентаря.

class Product():
    name: str
    price: float
    quantity: int

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Store():
    catalog: list

    def __init__(self):
        self.catalog = []

    def add_products_to_store(self, product: Product):
        self.catalog.append(product)

    def get_catalog(self):
        return self.catalog

    def get_quantity_in_stock(self, product_name):
        for product in self.catalog:
            if product.name == product_name:
                return product.quantity
        return 0

    def update_store(self, product_list):
        print(len(product_list), len(self.catalog))
        for item in product_list:
            for product in self.catalog:
                if product.name == item['name']:
                    product.quantity -= item['quantity']
                    print(
                        f"Оставшееся количество 'tovarov'{product.name} на складе: {self.get_quantity_in_stock(product.name)}")


class Cart():
    __product_list: list
    quantity: int

    def __init__(self):
        self.quantity = 0
        self.__product_list = []

    def get_product_list(self):
        return self.__product_list

    def add_prod_in_cart(self, product, quantity):
        self.__product_list.append({
            "name": product.name,
            "quantity": quantity,
            "price": product.price
        })

    def count_common_price(self, product_list):  # нужно возвращать общую стоимость
        summ = 0
        for product in product_list:
            summ += product['price'] * product['quantity']
        return summ


class Customer():
    __name: str
    __cart: Cart

    def __init__(self, name):
        self.__cart = Cart()
        self.__name = name

    def to_buy(self):
        # TODO РЕАЛИЗОВАТЬ ФУНКЦИОНАЛ ПО ОЧИСТКЕ КОРЗИНЫ ?
        store_globus.update_store(self.__cart.get_product_list())

    def add_product_to_cart(self, product_name, quantity):
        catalog = store_globus.get_catalog()
        for product in catalog:
            if product.name == product_name:
                self.__cart.add_prod_in_cart(product, quantity)

    def return_result_sum(self):
        result = self.__cart.count_common_price(self.__cart.get_product_list())
        return result


aplle = Product("Яблоко", 400.0, 50)
tomato = Product("Tomato", 40.0, 51)
store_globus = Store()
store_globus.add_products_to_store(aplle)
store_globus.add_products_to_store(tomato)
cust = Customer("Imya")
cust.add_product_to_cart("Яблоко", 5)
cust.add_product_to_cart("Tomato", 5)
print(cust.return_result_sum())


# Задача 2
# Создайте приложение для управления задачами. Реализуйте классы Task, TaskList, и User.
# Task должен иметь атрибуты, такие как название, описание и статус (выполнено/не выполнено).
# TaskList содержит список задач, и методы для добавления, удаления и фильтрации задач.
# Класс User хранит информацию о пользователях и их списки задач. Реализуйте возможность регистрации
# и авторизации пользователей.

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.name}\nОписание: {self.description}\nСтатус: {status}"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def filter_tasks(self, completed=False):
        return [task for task in self.tasks if task.completed == completed]


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.task_lists = {}

    def create_task_list(self, list_name):
        if list_name not in self.task_lists:
            self.task_lists[list_name] = TaskList()

    def get_task_list(self, list_name):
        if list_name in self.task_lists:
            return self.task_lists[list_name]
        else:
            return None

    def authenticate(self, password):
        return self.password == password


# Создание пользователей
user1 = User("user1", "password1")
user2 = User("user2", "password2")

# Регистрация пользователей и создание списков задач
users = [user1, user2]
for user in users:
    user.create_task_list("Список дел")

# Авторизация
username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
authenticated_user = None

for user in users:
    if user.username == username and user.authenticate(password):
        authenticated_user = user
        break

if authenticated_user:
    print(f"Добро пожаловать, {authenticated_user.username}!")

    # Работа с задачами
    task1 = Task("Купить продукты", "Молоко, яйца, огурцы")
    task2 = Task("Записать видео", "Сделать видеоурок по программированию")

    task_list = authenticated_user.get_task_list("Список дел")
    if task_list:
        task_list.add_task(task1)
        task_list.add_task(task2)

        print("Задачи в списке:")
        for task in task_list.tasks:
            print(task)
    else:
        print("Список дел не найден.")
else:
    print("Ошибка авторизации.")