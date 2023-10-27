# Создайте класс Abonent. Поля: Идентификационный номер,ФИО, Адрес, Номер кредитной карточки,
# Дебет, Кредит, Время междугородных и городских переговоров;
# (id_number, full_name,  address, credite, card_number, debet, call_time)
# Методы:
# display_info - Вывод информации  (ФИО, номер кредитной карты)
# Классметоды:
# get_overused - получает список объектов класса Abonent (параметр abos)
# и возвращает новый список из тех, кто превысил норму по времени на городских переговорах (15 min),
# также выводит информацию об абоненте.
# sort_abo - получает список объектов класса Abonent (параметр abos),
# и возвращает отсортированный список абонентов по алфавиту

class Abonent:
    def __init__(self, id_number, full_name, address, card_number, debet, credite, city_call_time=0, intercity_call_time=0):
        self.id_number = id_number
        self.full_name = full_name
        self.address = address
        self.card_number = card_number
        self.debet = debet
        self.credite = credite
        self.city_call_time = city_call_time
        self.intercity_call_time = intercity_call_time

    def display_info(self):
        return f"{self.full_name}, {self.card_number}"

    @classmethod
    def get_overused(cls, abos):
        return [abo for abo in abos if abo.city_call_time > 15]

    @classmethod
    def sort_abo(cls, abos):
        return sorted(abos, key=lambda abo: abo.full_name)
abonent1 = Abonent(1, "Вася Пупкин", "ул. Пушкина, 1", "1234-5678-9012-3456", 1000, 500, 25, 10)
abonent2 = Abonent(2, "Петя Сидоров", "пр. Ленина, 42", "9876-5432-1098-7654", 800, 600, 12, 20)
abonent3 = Abonent(3, "Жора Гагарин", "пр. Космонавтов, 3", "5678-1234-5678-4321", 1200, 300, 5, 5)
abonents = [abonent1, abonent2, abonent3]

print("Список абонентов, превысивших норму на городских переговорах:")
overused_abos = Abonent.get_overused(abonents)
for abo in overused_abos:
    print(abo.display_info())

print("\nСписок абонентов, отсортированных по алфавиту:")
sorted_abos = Abonent.sort_abo(abonents)
for abo in sorted_abos:
    print(abo.display_info())