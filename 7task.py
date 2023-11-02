class CarDealer:
    def __init__(self, city, quantity):
        self.city = city
        self.quantity = quantity

    def add_car(self, num):
        self.quantity += num


class Car(CarDealer):
    def __init__(self, brand, model, city, quantity):
        CarDealer.__init__(self, city, quantity)
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} | {self.model} | {self.city}| available {self.quantity}")


car1 = Car("BMW", "X6", "Boston", 5)
car2 = Car("BMW", "X7", "Boston", 10)
car3 = Car("BMW", "X6", "Los angeles", 15)

car1.display_info()
car2.display_info()
car3.display_info()
car1.add_car(5)
car1.display_info()
