# Создайте класс Car. Пропишите в конструкторе параметры make, model, year, odometer, fuel.
# Пусть у показателя odometer будет первоначальное значение 0,а у fuel 70. Добавьте метод drive,
# который будет принимать расстояние в км. В самом начале проверьте, хватит ли вам бензина из расчета того,
# что машина расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,то пусть
# этот метод добавляет эти километры к значению одометра, но не напрямую, а с помощью приватного метода
# __add_distance. Помимо этого пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не хватит,
# то распечатайте “Need more fuel, please, fill more!” Расcчитанное количество бензина нужно округлить
# до ближайшего целого числа. Пример, 13км -> 1.3л -> 1 л; 17км -> 1.7 л -> 2л
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70
#
#     def drive(self, distance):
#         required_fuel = distance / 10           # Необходимое топливо = расстояние / 10
#         if self.fuel >= required_fuel:          # Если топливо >= необходимое топливо, то:
#             self.__add_distance(distance)       # Добавить расстояние
#             self.__subtract_fuel(required_fuel) # Вычесть топливо(Необходимое топливо)
#             print("Можем ехать")
#         else:
#             print("Нужно заправить машину")
#
#     def __add_distance(self, distance):         # Добавить расстояние в одометр
#         self.odometer += distance
#
#     def __subtract_fuel(self, fuel_used):       # Вычесть использованное топливо
#         self.fuel -= round(fuel_used)
#
# # Создаем экземпляр класса Car
# my_car = Car("Toyota", "Camry", 2022)
#
# # Пример использования метода drive
# my_car.drive(25)  # Попытка проехать 25 км
# my_car.drive(250)  # Попытка проехать 250 км
# my_car.drive(5)  # Попытка проехать 5 км
# print(f"Пройдено километров: {my_car.odometer} км")
# print(f"Остаток бензина: {my_car.fuel} л")
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.fuel = 70
#         self.odometer = 0
#
#     def drive(self, distance):
#         required_fuel = distance / 10
#         self.__add_distance(distance)
#         if self.fuel >= required_fuel:
#             self.__subtract_fuel(required_fuel)
#             print("Можем ехать")
#         else:
#             print("Нужно заправить машину")
#
#     def __add_distance(self, distance):
#         self.odometer += distance
#         return self.odometer
#
#     def __subtract_fuel(self, fuel_used):
#         self.fuel -= fuel_used
#         return self.fuel
#
#
# my_car = Car("Toyota", "Camry", 2022)
# my_car.drive(25)
# print(f"Пройдено километров: {my_car.odometer} км")
# print(f"Остаток бензина: {my_car.fuel} л")
# class Car:
#     fuel = 70
#     odometer = 0
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def drive(self, distance):
#         required_fuel = distance / 10
#         self.__add_distance(distance)
#         if Car.fuel >= required_fuel:
#             self.__subtract_fuel(required_fuel)
#             return "Можем ехать"
#         else:
#             return "Нужно заправить машину"
#
#     def __add_distance(self, distance):
#         Car.odometer += distance
#         return Car.odometer
#
#     def __subtract_fuel(self, fuel_used):
#         Car.fuel -= fuel_used
#         return Car.fuel
#
#
# my_car = Car("Toyota", "Camry", 2022)
# my_car.drive(25)
# print(f"Пройдено километров: {my_car.odometer} км")
# print(f"Остаток бензина: {my_car.fuel} л")
#
class Car:
    def init(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel

    def drive(self, distance):
        required_fuel = distance / 10
        if self.fuel >= required_fuel:
            self.__add_distance(distance)
            self.__subtract_fuel(required_fuel)
            print("Можем ехать")
        else:
            print("Нужно заправить машину")

    def __add_distance(self, distance):
        self.odometer += distance

    def __subtract_fuel(self, fuel_used):
        self.fuel = round(self.fuel - fuel_used)

my_car = Car()
my_car.drive(25)
print(my_car.odometer)
print(my_car.fuel)
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
#
# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage, capacity):
#         super().__init__(name, max_speed, mileage)
#         self.capacity = capacity
#
#     def seating_capacity(self, capacity):
#         return super().seating_capacity(capacity)
#
#
# my_bus = Bus("Mercedes", 100, 12, 50)
# print(my_bus.seating_capacity(22))
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage, capacity=50):
#         super().__init__(name, max_speed, mileage)
#         self.capacity = capacity
#
#     def seating_capacity(self):
#         return super().seating_capacity(self.capacity)
#
# my_bus = Bus("Mercedes", 100, 12)
# print(my_bus.seating_capacity())