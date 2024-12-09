#OOP Assignment

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
    
    def apply_discount(self, discount):
        self.price -= (discount*self.price)/100
        pass

    def get_info(self):
        info = (self.make, self.model, self.price)
        return info
    
#_main_
task1 = Car("Hyundai", "Verna", 10000)
print(task1.get_info())
