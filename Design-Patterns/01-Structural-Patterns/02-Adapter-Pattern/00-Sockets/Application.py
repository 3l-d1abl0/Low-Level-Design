class AmericanKettle(object):

    __power = None

    def __init__(self, power):
        self.__power = power


    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle is on fire !")
        else:

            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print('Coffee Time !')
            else:
                print("No Power !")
