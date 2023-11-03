# TODO Использовать peewee для сохранения данных с парсинга в PostgreSQL.
import re
from urllib import request
from bs4 import BeautifulSoup
from bs4.element import Comment
from peewee import Model, CharField, FloatField, TextField, PostgresqlDatabase, ForeignKeyField

# Установите соединение с базой данных PostgreSQL
db = PostgresqlDatabase('ecoland', user='postgres', password='3823krasivoe', host='127.0.0.1')


# Определите модели данных для продуктов и категорий продуктов


class Category(Model):
    name = CharField(max_length=100)
    description = TextField()
    link = TextField()

    class Meta:
        database = db


class Product(Model):
    name = CharField()
    price = FloatField()
    category = ForeignKeyField(Category)

    class Meta:
        database = db


# Создайте таблицы в базе данных
db.connect()
# db.create_tables([Product, Category])

# URL веб-сайта для парсинга
url = 'https://ecoland.kg'  # Замените на реальный URL


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


def get_menu_categories(body):
    soup = BeautifulSoup(body, 'html.parser')
    list_of_category = soup.select(".mega_menu_item")
    for category in list_of_category:
        name = category.find(class_='mega_menu_item_link').text
        link = category.find('a')['href']
        # print(name, link)
        Category.insert(name=name, link=link, description=name).execute()



def save_products():
    result_list_of_categories = list(Category.select(Category.link, Category.name, Category.id).execute())
    for item in result_list_of_categories:
        response = request.urlopen(item.link)
        get_products_from_page(response, item.id)


def get_products_from_page(body, c_id):
    soup = BeautifulSoup(body, 'html.parser')
    product_list = soup.select(".product_item")
    for product_element in product_list:
        name = product_element.find(class_='product_item_title').text
        price = product_element.select_one('.product_item_price .amount').text
        price_digit = re.findall(r'\d+', price)
        Product.create(name=name, price=price_digit[0], category=c_id)



# Выполните HTTP-запрос и получите HTML-страницу
response = request.urlopen(url)
response2 = request.urlopen(url)
# html = text_from_html(response)
# get_menu_categories(response2)
save_products()

# Сохраните данные о продуктах в базу данных
# with db.atomic():
#     for data in product_data:
#         product = Product.create(**data)

# Закройте соединение с базой данных
db.close()
