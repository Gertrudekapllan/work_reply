from datetime import datetime
from decouple import config
from peewee import *

# Подключение к базе данных с использованием настроек из .env файла
db = PostgresqlDatabase(
    database="web_market",
    user="postgres",
    password="3823krasivoe",
    host="127.0.0.1",
    port="5432"
)


# Определение модели Category (категория товаров)
class Category(Model):
    name = CharField(max_length=100)
    description = TextField()

    class Meta:
        database = db
        db_table = 'my_category'


# Определение модели Product (товар)
class Product(Model):
    name = CharField(max_length=50)
    price = IntegerField()
    count = IntegerField()
    available = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now())
    category = ForeignKeyField(Category)

    class Meta:
        database = db


# Подключение к базе данных
db.connect()

# Создание таблиц в базе данных для моделей Category и Product
db.create_tables([Category, Product])

# Примеры операций с моделями:
# Далее следуют примеры операций с моделями Category и Product. Раскомментируйте для использования.

# 1. Создание объекта Category (категория товаров) и сохранение его в базу данных
# category_obj = Category(name="fruits", description="cool")
# category_obj.save()

# 2. Создание новой категории "vegetables" и добавление ее в базу данных
# Category.insert(name="vegetables", description="nice").execute()

# 3. Создание объекта Product (товар) и сохранение его в базу данных
# category_obj = Product(name="cherry", price=300, count=20, category=1)
# category_obj.save()

# 4. Вставка нового товара "apple" в базу данных
# Product.insert(name="apple", price=280, count=50, category=1).execute()

# 5. Получение всех товаров из базы данных и сортировка их по ID по возрастанию
# data = Product.select().order_by(Product.id.asc())

# 6. Обновление поля "available" для каждого товара
# for i in data:
#     i.available = True
#     i.save()

# 7. Получение категории с ID 1
# data = Category.get(id=1)
# print(data.description)

# 8. Удаление товара "banana" из базы данных
# banana = Product.get(id(2))
# banana.delete_instance()

# 9. Обновление поля "available" для товара "banana" и сохранение его
# banana.available = False
# banana.save()
# Удаляем товар "banana" (в этом контексте бездействующая операция, поскольку "banana" не создана в этом фрагменте кода)
# banana = Product.get(name="banana")
# banana.delete_instance()

# 10. Получение всех товаров с именем "apple" из базы данных
# for product in Product.select().filter(Product.name=='apple'):
#     print(product.name)
