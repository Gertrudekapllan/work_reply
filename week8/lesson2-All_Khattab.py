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
    summ: float
    quantity: int

    def __init__(self):
        self.quantity = 0
        self.summ = 0
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
            print(product, 'eee')
            summ += product['price'] * product['quantity']
            print(summ,'summ')
        return summ


class Customer():
    __name: str
    __cart: Cart

    def __init__(self, name):
        self.__cart = Cart()
        self.__name = name

    def to_buy(self):
        # TO DO   РЕАЛИЗОВАТЬ ФУНКЦИОНАЛ ПО ОЧИСТКЕ КОРЗИНЫ
        store_globus.update_store(self.__cart.get_product_list())

    def add_product_to_cart(self, product_name, quantity):
        catalog = store_globus.get_catalog()
        for product in catalog:
            if product.name == product_name:
                self.__cart.add_prod_in_cart(product, quantity)

    def return_result_sum(self):
        print((self.__cart.get_product_list()),'liii')
        result = self.__cart.count_common_price(self.__cart.get_product_list())
        print(result,'salt')
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
