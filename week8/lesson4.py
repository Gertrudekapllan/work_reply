# class decorators

def add_attrs(cls):
    class DecoretedClass(cls):
        test = "test"

        def print_text(self, text):
            print(text)

    return DecoretedClass


@add_attrs
class Test1:
    def print_hello(self):
        print("hello")


obj1 = Test1()
print(obj1.test)
obj1.print_text("jefber")
obj1.print_hello()

def add_prefix(prefix):
    def get_class(cls):
        class DecoretedClass(cls):
            def __init__(self, name):
                super().__init__(name)
                self.name = prefix + self.name
        return DecoretedClass
    return get_class


@add_prefix("Mr.")
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


junko = Person("Jakshylyk")
junko.get_name()

def add_year(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) + 1
        return result
    return wrapper


class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    @add_year
    def add_one_year_age(self, age):
        return age


nazi = Person("Nazgul")

# abstract
import csv
import random
from abc import ABC, abstractmethod


class FigureAbstract(ABC):

    @abstractmethod
    def get_sqare(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(FigureAbstract):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def get_sqare(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

reg1 = FigureAbstract()
print(reg1.get_sqare())
# mixin ооп

class RegisterMixin:
    def save_db(self):
        with open("employee.csv", "w") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(["id", "ФИО", "Номер телефона", "Заработная плата", "Электронная почта"])
            writer.writerow([self.id_number, self.full_name, self.phone_number, self.salary, self.email])
        print("уусе!!!")


class SendEmailMixin:
    def send_message(self):
        import smtplib
        import ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        subject = "Регистрация"
        text = f"Регистрация прошла успешно!\n Ваш идентификатор {self.id_number}"
        recipient = self.email

        sender_email = "tabyldieva1296@gmail.com"
        password = "hhef pjiv mchy uaxt"

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = recipient
        part1 = MIMEText(text, "plain")
        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient, message.as_string())


class Employee(RegisterMixin, SendEmailMixin):
    def __init__(self, phone_number, full_name, salary, email):
        self.phone_number = phone_number
        self.full_name = full_name
        self.salary = salary
        self.id_number = random.randint(1000, 9999)
        self.email = email


nazi = Employee("996555446677", "Tabyldieca Nazgul", 123456677, "tabyldieva1296@gmail.com")
junko = Employee("996555446678", "Асымкулов Жакшылык", 127456677, "jakshylykit@gmail.com")
nazi.save_db()
junko.save_db()
nazi.send_message()
junko.send_message()
