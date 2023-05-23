class Car:
    """A simple way to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_car_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has an odometer reading of {self.odometer_reading}")

    def update_odometer(self, miles):
        self.odometer_reading += miles
        return self.odometer_reading

class ElectricCar(Car):
    """Represents an electric vehicle"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)

my_polestar = ElectricCar('Polestar', 'PS2', 2023)

print(f"My car's name is {my_polestar.get_car_name()}.")