class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        self.fuel = fuel
        self.odometer = 0
        self.name = name

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return self.odometer

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
