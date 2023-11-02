class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Store:
    def __init__(self, store_name):
        self.store_name = store_name

    def display_store(self):
        print(self.store_name)


class Dairy(Goods, Store):
    def __init__(self, name, price, store_name):
        Goods.__init__(self, name, price)
        Store.__init__(self, store_name)

    def display_info(self):
        print(self.name + " - " + str(self.price) + " in " + self.store_name)


dairy1 = Dairy("Milk", 1.2, "Metro")
dairy1.display_info()
dairy1.display_store()

