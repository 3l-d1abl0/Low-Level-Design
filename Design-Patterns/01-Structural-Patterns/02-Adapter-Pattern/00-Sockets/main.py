from Sockets import EuropeanSocket
from Application import AmericanKettle
from Adapter import Adapter


if __name__ == "__main__":


    #Eaxample 1: Fire
    print("Example 1")
    Esocket = EuropeanSocket()
    Akettle = AmericanKettle(Esocket)
    Akettle.boil()

    print("Example 2")
    Akettle2 = AmericanKettle(Adapter(Esocket))
    Akettle2.boil()
