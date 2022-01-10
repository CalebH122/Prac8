from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    print("Let' drive!")
    print(MENU)
    user_choose = input("").lower()
    while user_choose != "q":

        if user_choose == "c":
            pass

        elif user_choose == "d":
            pass

        print("Bill to date: {}".format(total_bill))
        print(MENU)
        user_choose = input("").lower()
    print("Total trip cost:{}".format(total_bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()
