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
car1 = Car("Toyota", "Corolla", 10000)
car2 = ElectricCar("Tata", "Nexon", 20000, 500.0)
car3 = SportsCar("Bugatti", "Chiron", 80000, 300.0)

car_list = [car1, car2, car3]
for i in car_list:
    print(i.get_info())
