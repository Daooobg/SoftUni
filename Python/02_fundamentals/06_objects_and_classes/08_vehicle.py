class Vehicle:
    def __init__(self, type, model, price, owner = None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if self.owner:
           return 'Car already sold'
        else:
            if money >= self.price:
                self.owner = owner
                return f'Successfully bought a {self.type}. Change: {(money - self.price):.2f}'
            else:
                return 'Sorry, not enough money'

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return 'Vehicle has no owner'

    def __repr__(self):
        if self.owner:
            return f'{self.model} {self.type} is owned by: {self.owner}'

        return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
