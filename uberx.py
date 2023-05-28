from car import Car
from account import Account

class UberX(Car):
    brand = str
    model = str

    def __init__(self, Car, brand, model):
        super(UberX, self).__init__(Car, Car.license)
        self.brand = brand
        self.model = model

