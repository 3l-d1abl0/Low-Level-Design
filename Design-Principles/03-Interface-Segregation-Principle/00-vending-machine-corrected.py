import abc

class VendingMachine(object):
    '''Abstract Vending Machine Class'''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def take_money(self, value):
        raise NotImplementedError("Implement Take Money function")

class SnackVendingMachine(VendingMachine):

    def take_money(self, value):
        self.value = value

    def dispense_snack(self):
        print("Please collect your Snack")

class ColdBeverageMachine(VendingMachine):

    def take_money(self, value):
        self.value = value

    def dispense_water(self):
        print("Please take Water")

    def dispense_soda(self):
        print("Please Collect your Soda")


class HotBeverageMachine(VendingMachine):

    def take_money(self, value):
        self.value = value

    def brew_coffee(self):
        print("Please collect your Coffee")

    def brew_hot_chocolate(self):
        print("Please collect your hot chocolate")

    def brew_tea(self):
        print("Please collect you Tea")




if __name__ == "__main__":

    #Snacks vending machine with relevant functinality
    snack = SnackVendingMachine()
    snack.take_money(100)
    snack.dispense_snack()
    #snack.brew_coffee()

    coldVendingMachine = ColdBeverageMachine()
    coldVendingMachine.take_money(50)
    coldVendingMachine.dispense_soda()
    #coldVendingMachine.brew_hot_chocolate()

    hotVendingMachine = HotBeverageMachine()
    hotVendingMachine.take_money(123)
    hotVendingMachine.brew_coffee()
    hotVendingMachine.brew_hot_chocolate()
    hotVendingMachine.brew_tea()
