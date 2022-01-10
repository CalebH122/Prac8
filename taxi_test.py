from taxi import Taxi


def main():
    taxi_one = Taxi("Prius 1", 100)
    taxi_one.drive(40)
    print(taxi_one)
    current_fare = taxi_one.get_fare()
    print("current fare: {}".format(current_fare))
    taxi_one.start_fare()
    taxi_one.drive(100)
    print(taxi_one)
    current_fare = taxi_one.get_fare()
    print("current fare: {}".format(current_fare))


if __name__ == '__main__':
    main()
