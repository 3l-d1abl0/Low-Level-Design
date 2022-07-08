'''Breaks OCP
class Discount:

    def __init__(self, customer_type, price):
        self.customer = customer_type
        self.price = price

    def give_discount(self):

        if self.customer == "fav":
            return self.price * 0.2

        #New type of discount (violation of Open Closed Principle)
        if self.customer == "vip":
            return self.price * 0.4
'''

class Discount:

    def __init__(self, customer_type, price):
        self.customer = customer_type
        self.price = price

    def get_discount(self):
        
        return self.price*0.2

class VIPDiscount(Discount):
    
    def get_discount(self):
        
        return super().get_discount()*2

class VVIPDiscount(Discount):
    
    def get_discount(self):
        
        return super().get_discount()*4


if __name__ == "__main__":

    '''Breaks OCP
    price = 100
    dd = Discount("fav", price)
    discounted_price = dd.give_discount()
    print(discounted_price)
    '''

    price = 1000

    #Favourite Customer
    dd = Discount("fav", price)
    discounted_price = dd.get_discount()
    print(discounted_price)

    #VIP Customer
    dd = VIPDiscount("VIP", price)
    discounted_price = dd.get_discount()
    print(discounted_price)

    #VVIP Customer
    dd = VVIPDiscount("VVIP", price)
    discounted_price = dd.get_discount()
    print(discounted_price)
