# TODO Использовать peewee для сохранения данных с парсинга в PostgreSQL.

from urllib import request
from bs4 import BeautifulSoup
from bs4.element import Comment
from peewee import Model, CharField, FloatField, TextField, PostgresqlDatabase

# Установите соединение с базой данных PostgreSQL
db = PostgresqlDatabase('имя_базы_данных', user='ваш_пользователь', password='ваш_пароль', host='localhost')


# Определите модели данных для продуктов и категорий продуктов
class Product(Model):
    name = CharField()
    price = FloatField()
    category = CharField()

    class Meta:
        database = db


class CategoryProduct(Model):
    name = CharField(max_length=100)
    description = TextField()

    class Meta:
        database = db


# Создайте таблицы в базе данных
# db.connect()
# db.create_tables([Product, CategoryProduct])

# URL веб-сайта для парсинга
url = 'https://ecoland.kg/catalog/sladosti/page/2'  # Замените на реальный URL


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def get_element_from_page(body):
    soup = BeautifulSoup(body, 'html.parser')
    product_list = soup.select(".product_item")
    print(product_list, "get_element_from_page")
    for product_element in product_list:
        name = product_element.find(class_='product_item_title').text
        price = product_element.find(class_='product_item_price').text
        print(name, price)
        # price = float(product_element.find('span', class_='price').text.strip('$'))
        # category = 'Категория A'  # Замените на реальное значение категории
        # product_data.append({'name': name, 'price': price, 'category': category})


# Выполните HTTP-запрос и получите HTML-страницу
response = request.urlopen(url)
# html = text_from_html(response)
get_element_from_page(response)
# Используйте Beautiful Soup для парсинга HTML
# soup = BeautifulSoup(html, 'html.parser')

# Найдите данные о продуктах и категориях
product_data = []

# Пример парсинга данных (замените на репродукцию данных с вашего сайта)
# for product_element in soup.find_all('div', class_='product'):
#     name = product_element.find('h2').text
#     price = float(product_element.find('span', class_='price').text.strip('$'))
#     category = 'Категория A'  # Замените на реальное значение категории
#     product_data.append({'name': name, 'price': price, 'category': category})

# Сохраните данные о продуктах в базу данных
# with db.atomic():
#     for data in product_data:
#         product = Product.create(**data)
#
# # Закройте соединение с базой данных
# db.close()
