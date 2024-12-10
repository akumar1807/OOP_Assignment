#OOP Assignment

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.__price = price
    
    def apply_discount(self, discount):
        self.price -= (discount*self.price)/100
        pass

    def get_info(self):
        info = (self.make, self.model, self.get_price())
        return info
    
    def get_price(self):
        return self.__price
    
    def set_price(self, p):
        self.__price = p

class ElectricCar(Car):
    def __init__(self, make, model, price, battery):
        super().__init__(make, model, price)
        self.battery_range = battery
    
    def get_info(self):
        info = (self.make, self.model, self.get_price(), self.battery_range)
        return info

class SportsCar(Car):
    def __init__(self, make, model, price, speed):
        super().__init__(make, model, price)
        self.top_speed = speed
    
    def get_info(self):
        info = (self.make, self.model, self.get_price(), self.top_speed)
        return info

#_main_
task1 = SportsCar("Hyundai", "Verna", 10000, 200.0)
print(task1.get_info())
print(task1.get_price())
task1.set_price(20000)
print(task1.get_price())
