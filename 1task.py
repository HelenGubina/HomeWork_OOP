class Person:
    def __init__(self):
        self.__name = "Ann"
        self.__age = 18

    def change_age(self,  age):
        if isinstance(age, int) and age in range(0, 120):
            self.__age = age
        else:
            print("Incorrect value of age")

    def change_name(self,  name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            print("Incorrect value of name")

    def show_age(self):
        print(self.__age)

    def show_name(self):
        print(self.__name)


pers1 = Person()
pers1.change_name("Leonid23")
pers1.change_age(20)

pers1.show_age()
pers1.show_name()
