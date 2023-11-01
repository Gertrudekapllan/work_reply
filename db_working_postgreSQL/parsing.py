# TODO Использовать peewee для сохранения данных с парсинга в PostgreSQL.
from datetime import datetime

from peewee import Model, CharField, FloatField, PostgresqlDatabase, IntegerField, BooleanField, DateTimeField, \
    TextField, ForeignKeyField

# Установите соединение с вашей базой данных PostgreSQL
db = PostgresqlDatabase('имя_базы_данных', user='ваш_пользователь', password='ваш_пароль', host='localhost')


class Category_product(Model):
    name = CharField(max_length=100)
    description = TextField()

    class Meta:
        database = db
        db_table = 'my_category_product'


class Product_parsing(Model):
    name = CharField(max_length=50)
    price = IntegerField()
    count = IntegerField()
    available = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now())
    category = ForeignKeyField(Category_product)

    class Meta:
        database = db


db.connect()
db.create_tables([Product])

# Допустим, у вас есть данные для сохранения
product_data = [
    {"name": "Продукт 1", "price": 10.99},
    {"name": "Продукт 2", "price": 19.99},
]

# Сохраняем данные в базу данных
with db.atomic():
    for data in product_data:
        Product.create(**data)
