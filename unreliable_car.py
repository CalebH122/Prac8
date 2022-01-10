from car import Car
from random import randint


class Unreliable_car(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_distance_driven = 0

    def drive(self, distance):
        if self.reliability <= randint(0, 100):
            distance_drive = 0
            print("You can't drive this car!")
        else:
            distance_drive = super().drive(distance)
        self.current_distance_driven += distance_drive
        return self.current_distance_driven
