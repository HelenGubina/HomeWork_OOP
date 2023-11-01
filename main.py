class Person:
    def __init__(self):
        self.__name = "Ann"
        self.__age = 18

    def change_private(self, name, age):
        self.__name = name
        self.__age = age

    def show_age(self):
        print(self.__age)

    def show_name(self):
        print(self.__name)


pers1 = Person()
pers1.change_private("Leonid", 23)
pers1.show_age()
pers1.show_name()
