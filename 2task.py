class Car:
    def __init__(self, year, mileage):
        self.__make = "Ford"
        self.__model = "Fusion"
        self.year = year
        self.mileage = mileage

    def show_make(self):
        print(self.__make)

    def show_model(self):
        print(self.__model)

    def drive(self, miles):
        if self.mileage + miles < 300000:
            self.mileage += miles
        else:
            print("Mileage limit reached")


car1 = Car(2015, 10000)
car1.show_make()
car1.show_model()
car1.drive(100000)
car1.drive(200000)
