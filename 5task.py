class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie


class Mammal(Animal):
    def __init__(self, name, specie, diet_type):
        Animal.__init__(self, name, specie)
        self.diet_type = diet_type
    def display_info(self):
        print(f"Animal:  {self.name} \nSpecie: {self.specie} \nDiet Type: {self.diet_type} ")


class Carnivore(Mammal):
    def __init__(self, name, specie, diet_type, teeth_quantity):
        Mammal.__init__(self, name, specie, diet_type)
        self.teeth_quantity = teeth_quantity
    def display_info(self):
        print(f"Animal:  {self.name} \nSpecie: {self.specie} \nDiet Type: {self.diet_type} "
              f"\nTeeth quantity: {self.teeth_quantity} ")


class Lion(Carnivore):
    def __init__(self, name, specie, diet_type, teeth_quantity, mane_size):
        Carnivore.__init__(self, name, specie, diet_type, teeth_quantity)
        self.mane_size = mane_size

    def display_info(self):
        print(f"Animal:  {self.name} \nSpecie: {self.specie} \nDiet Type: {self.diet_type} "
              f"\nTeeth quantity: {self.teeth_quantity} \nMane size: {self.mane_size} ")


mammal = Mammal("Deer", "Mammal", "Herbivore")
carnivore = Carnivore("Cougar", "Mammal", "Carnivore", 30)
lion = Lion("Lion", "Mammal", "Carnivore", 30, "Large")

mammal.display_info()
print("-"*100)
carnivore.display_info()
print("-"*100)
lion.display_info()
