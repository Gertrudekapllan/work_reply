class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Customer:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):          # Добавить в корзину:
        if product.quantity >= quantity:               # Если количество товара >= количества, то:
            self.cart.append((product, quantity))      # Добавляем товар и количество в корзину
            product.quantity -= quantity               # Отнимаем количество от общего количества
            return True
        else:
            return False

    def calculate_total(self):                         # Рассчитать итог:
        total = 0                                      # Итог изначально равен = 0
        for product, quantity in self.cart:            # Товар и количество в корзине
            total += product.price * quantity          # Итог += товар.цена * количество
        return total

    def checkout(self):                                # Оформить покупку
        total = self.calculate_total()                 # Рассчитать итог
        return total


class Store:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):                         # Добавить товар
        self.inventory.append(product)

    def show_inventory(self):                               # Показать товар в инвентаре
        for product in self.inventory:
            print(f"Product: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

    def restock_product(self, product, quantity):           # Пополнить товар
        for product_in_inventory in self.inventory:         # Для товар_в_инвентаре в инвентарь
            if product_in_inventory.name == product.name:   # Если товар_в_инвентаре.название == товар.название
                product_in_inventory.quantity += quantity   # товар_в_инвентаре.количество += количество

# Пример использования:

product1 = Product("Laptop", 800, 5)
product2 = Product("Smartphone", 400, 10)
product3 = Product("Tablet", 300, 7)

store = Store()
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

customer1 = Customer()
customer2 = Customer()

customer1.add_to_cart(product1, 2)
customer1.add_to_cart(product2, 3)

customer2.add_to_cart(product1, 1)
customer2.add_to_cart(product3, 4)

print(store.show_inventory())

total1 = customer1.checkout()
total2 = customer2.checkout()

print(f"Customer 1's total: ${total1}")
print(f"Customer 2's total: ${total2}")
