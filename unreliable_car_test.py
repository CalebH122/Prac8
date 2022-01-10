from unreliable_car import Unreliable_car


def main():
    unreliable_car = Unreliable_car("car", 200, 50)
    unreliable_car.drive(20)
    print(unreliable_car)


if __name__ == '__main__':
    main()
