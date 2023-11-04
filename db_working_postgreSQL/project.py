from peewee import Model, CharField, BooleanField, PostgresqlDatabase

# Установите подключение к базе данных PostgreSQL
db = PostgresqlDatabase('имя_базы_данных', user='ваш_пользователь', password='ваш_пароль', host='localhost')


class Task(Model):
    title = CharField()
    description = CharField()
    completed = BooleanField(default=False)

    class Meta:
        database = db


db.connect()
db.create_tables([Task], safe=True)

# Создание консольного интерфейса
# Разработайте функции для взаимодействия с базой данных, например, для создания,
# отметки как выполненных, обновления и удаления задач. Вот примеры функций:

def create_task(title, description):
    task = Task.create(title=title, description=description)
    return task


def mark_as_completed(task_id):
    task = Task.get_or_none(Task.id == task_id)
    if task:
        task.completed = True
        task.save()
        return task
    return None


def update_task(task_id, new_title, new_description):
    task = Task.get_or_none(Task.id == task_id)
    if task:
        task.title = new_title
        task.description = new_description
        task.save()
        return task
    return None


def delete_task(task_id):
    task = Task.get_or_none(Task.id == task_id)
    if task:
        task.delete_instance()
        return True
    return False


# Разработайте функцию для отображения списка задач:

def list_tasks():
    tasks = Task.select()
    for task in tasks:
        status = "Завершена" if task.completed else "Не завершена"
        print(f"ID: {task.id}, Заголовок: {task.title}, Описание: {task.description}, Статус: {status}")


# Шаг 3: Логика работы с данными
# Используйте созданные функции для добавления новых задач, обновления статуса,
# изменения описания и других атрибутов, а также для удаления задач.
# Шаг 4: Предоставление информации о задачах
# Разработайте функцию для получения списка всех задач и их вывода.
# Шаг 5: Обработка ошибок и исключений

# Добавьте обработку ошибок ввода данных пользователя и обработку исключений, связанных с доступом к базе данных.
# Пример обработки ошибок:
try:
    task_id = int(input("Введите ID задачи: "))
    task = Task.get_or_none(Task.id == task_id)
    if task:
    # Выполните действия с задачей
    else:
        print("Задача с указанным ID не найдена.")
except ValueError:
    print("Некорректный ввод. Введите целое число.")

# Эти шаги позволят вам создать консольное приложение для управления задачами с использованием Peewee ORM
# и базы данных PostgreSQL. Замените 'имя_базы_данных', 'ваш_пользователь' и 'ваш_пароль' на актуальные
# значения подключения к вашей PostgreSQL базе данных.
