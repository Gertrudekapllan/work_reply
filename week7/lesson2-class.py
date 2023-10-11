# 1. Создайте систему классов для электронной библиотеки. У вас должен быть базовый класс Item для представления
# элементов библиотеки (например, книг и видео), с атрибутами, такими как title, author, и year. Создайте подклассы
# для разных типов элементов (например, Book и Video), которые будут наследовать от базового класса Item. Реализуйте
# инкапсуляцию, чтобы контролировать доступ к атрибутам, и добавьте методы для вывода информации о каждом элементе.
class Item():
    def __init__(self, name, title, author, year, rating):
        self.name = name
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"Имя объекта:{self.name}\nНазвание объекта:{self.title}\n" \
               f"Автор:{self.author}\nГод:{self.year}\nРейтинг:{self.rating}"


class Book(Item):

    def __init__(self, quantity_stranic, *args, **kwargs):
        self.quantity_stranic = quantity_stranic
        super(Book, self).__init__(*args, **kwargs)

    def __str__(self):
        return f"Имя объекта:{self.name}\nНазвание объекта:{self.title}\n" \
               f"Автор:{self.author}\nГод:{self.year}\nРейтинг:{self.rating}\n" \
               f"количество страниц:{self.quantity_stranic}"

    def book_presented(self, quantity_stranic):
        result = f"В данной книге {self.quantity_stranic} страниц"
        return result


class Video(Item):

    def video_presented(self, quantity_sec):
        if quantity_sec:
            result = f"В данном видео {quantity_sec} секунд"
            quantity_sec += quantity_sec
            return result


video_1 = Video("Video", "Title", "Author", 12024, 188)
book_1 = Book(name="IMYA", title="title", author="Aut", year=2044, rating=100, quantity_stranic=10000000)
# print(video_1.video_presented(2222))
# print(book_1.book_presented())
print(book_1.__str__().upper())


print(video_1.__str__().upper())

# 2. Создайте систему классов для представления заказов в интернет-магазине.
# Создайте класс Product с атрибутами, такими как name, price, и quantity.
# Затем создайте класс Order, который может содержать несколько
# экземпляров Product. Реализуйте методы для добавления и удаления товаров
# из заказа, а также для вычисления общей суммы заказа.

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Имя:{self.name} Прайс:{self.price} Количество:{self.quantity}"


class Order:
    def __init__(self):
        self.orders_list = list()

    def __str__(self):
        return f"{self.orders_list}"

    def add(self, order_name):
        self.orders_list.append(order_name)
        return self.orders_list

    def summa(self):
        summa_list = []
        for product in self.orders_list:
            a = product.price * product.quantity
            summa_list.append(a)
        return sum(summa_list)

    def delite(self, product_name):
        for count in range(0, len(self.orders_list)-1):
            if product_name == self.orders_list[count].name:
                print("THIS IS COUNT", count)
                a = self.orders_list.pop(count)
                print('DELETED', a)
        return self.orders_list



apple = Product(name="Apple", price=203, quantity=14)
apple_red = Product(name="Apple_red", price=2223, quantity=11)
apple_green = Product(name="Apple_green", price=233, quantity=114)

print(apple.__str__())
print(apple_red.__str__())
print(apple_green.__str__())

order = Order()
order.add(apple)
order.add(apple_green)
order.add(apple_red)
print(order.orders_list)
print(order.summa())
print(order.delite("Apple"))
print(order.summa())
