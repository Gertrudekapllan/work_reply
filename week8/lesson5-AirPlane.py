class Airplane:
    def __init__(self, make, model, year, max_speed, odometer=15000):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = False

    def take_off(self):
        if not self.is_flying:
            self.is_flying = True
            print(f"{self.make} {self.model} взлетел.")
        else:
            print(f"{self.make} {self.model} уже в воздухе.")

    def fly(self, distance):
        if self.is_flying:
            self.odometer += distance
            print(f"{self.make} {self.model} пролетел {distance} километров. Одометр: {self.odometer} км.")
        else:
            print(f"{self.make} {self.model} не может лететь, пока не взлетел.")

    def land(self):
        if self.is_flying:
            self.is_flying = False
            print(f"{self.make} {self.model} приземлился.")
        else:
            print(f"{self.make} {self.model} уже на земле.")

# Создаем объект класса Airplane
airplane = Airplane(make="Боинг", model="747", year=2010, max_speed=920, odometer=15000)

# Взлетаем
airplane.take_off()

# Полет на 500 километров
airplane.fly(500)

# Приземление
airplane.land()

# Попытка снова взлететь
airplane.take_off()

# Попытка полететь без взлета
airplane.fly(200)

# Взлетаем снова
airplane.take_off()

# Полет на 300 километров
airplane.fly(300)

# Приземление
airplane.land()
