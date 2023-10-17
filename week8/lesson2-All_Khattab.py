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

    def add_products_to_store(self, product_name, price, quantity):
        product = Product(product_name, price, quantity)
        self.catalog.append(product)

    def get_catalog(self):
        return self.catalog


class Cart():
    product_list: list
    summ: float
    quantity: int

    def __init__(self):
        self.quantity = 0
        self.summ = 0
        self.product_list = []

    def add_prod_in_cart(self, product, quantity):
        for i in range(quantity):
            print(product, i)
            self.product_list.append(product)

    def count_common_price(self):
        sum(self.product_list)


class Customer():
    __name: str
    __cart: Cart

    def __init__(self, name):
        self.__cart = Cart()
        self.__name = name

    def add_product_to_cart(self, product_name, quantity):
        catalog = store_globus.get_catalog()
        for product in catalog:
            if product.name == product_name:
                print(product.name)
                self.__cart.add_prod_in_cart(product, quantity)


aplle = Product("Яблоко", 400.0, 50)
store_globus = Store()
store_globus.add_products_to_store("bread", 10.0, 100)

cust = Customer("Imya")
cust.add_product_to_cart("bread", 11)
