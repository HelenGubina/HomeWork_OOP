class Car:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model


class Sedan(Car):
    def __init__(self, mark, model, doors_quantity):
        Car.__init__(self, mark, model)
        self.doors_quantity = doors_quantity

    def display_info(self):
        print(f"{self.mark} | {self.model} | doors quantity {self.doors_quantity}")


class Suv(Car):
    def __init__(self, mark, model, seats_quantity):
        Car.__init__(self, mark, model)
        self.seats_quantity = seats_quantity

    def display_info(self):
        print(f"{self.mark} | {self.model} | seats quantity  - {self.seats_quantity}")


class SportCar(Car):
    def __init__(self, mark, model, max_speed):
        Car.__init__(self, mark, model)
        self.max_speed = max_speed

    def display_info(self):
        print(f"{self.mark} | {self.model} | max speed  - {self.max_speed}")


sedan = Sedan("Audi", "A8", 4)
suv = Suv("BMW", "X6", 5)
sport_car = SportCar("McLaren ", "750S", 330)

sedan.display_info()
suv.display_info()
sport_car.display_info()
