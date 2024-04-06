from director import Director
from builderInterface import JeepBuilder, NissanBuilder

if __name__ == "__main__":

    d1= Director()
    d1.setBuilder(JeepBuilder())
    jeepCar = d1.getCar()
    jeepCar.specification()


    print("--------------")
    d2= Director()
    d2.setBuilder(NissanBuilder())
    nissanCar = d2.getCar()
    nissanCar.specification()
