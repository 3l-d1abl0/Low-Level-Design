from copy import deepcopy

class Address:

    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):

        return f'{self.street_address}, {self.city}, {self.country}'



class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'



if __name__ == "__main__":

    john = Person('John', Address('123 London Road', 'London', 'UK'))
    print(john)

    '''
    jane = john
    jane.name = 'Jane'
    jane.address = '13B, Baker Street'


    print('John: ', john)
    print('Jane: ', jane)
    '''

    #If address Creation was difficult, we could have copied the Address Object

    holmes = Person('Sherlock', Address('13B, baker streer', 'London', 'UK'))

    watson = deepcopy(holmes)

    watson.name = 'Watson'


    print(holmes)
    print(watson)
