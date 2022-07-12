import abc

class VendingMachine(object):
    '''Abstract Vending Machine Class'''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def take_money(self, value):
        raise NotImplementedError("Implement take money method")

    @abc.abstractproperty
    def brew_coffee(self):
        raise NotImplementedError("Cannot bre coffee")

    @abc.abstractproperty
    def brew_hot_chocolate(self):
        raise NotImplementedError("Cannot brew hot chocolate")

    @abc.abstractproperty
    def brew_tea(self):
        raise NotImplementedError("Cannot brew Tea")

    @abc.abstractproperty
    def dispense_water(self):
        raise NotImplementedError("Cannot dispense water")

    @abc.abstractproperty
    def dispense_soda(self):
        raise NotImplementedError("Cannot dispense Soda")



class SnackVendingMachine(VendingMachine):

    def take_money(self, value):
        self.value = value

    def dispense_snack(self):
        print("Please collect your Snack")

    def brew_coffee(self):
        pass

    def brew_hot_chocolate(self):
        pass

    def brew_tea(self):
        pass

    def dispense_water(self):
        pass

    def dispense_soda(self):
        pass

class ColdBeverageMachine(VendingMachine):

    def take_money(self, value):
        self.value = value

    def dispense_snack(self):
        pass

    def brew_coffee(self):
        pass

    def brew_hot_chocolate(self):
        pass

    def brew_tea(self):
        pass

    def dispense_water(self):
        pass

    def dispense_soda(self):
        print("Please Cllect your Soda")

if __name__ == "__main__":

    snack = SnackVendingMachine()
    snack.take_money(100)
    snack.dispense_snack()
    snack.brew_coffee()

    coldVendingMachine = ColdBeverageMachine()
    coldVendingMachine.take_money(50)
    coldVendingMachine.dispense_soda()
    coldVendingMachine.brew_hot_chocolate()
