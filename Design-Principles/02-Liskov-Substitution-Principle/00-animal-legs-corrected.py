class Animal:

    def __init__(self, hind_leg, rear_leg):
        self.hind_leg = hind_leg
        self.rear_leg = rear_leg

    def leg_count(self):
        pass

class Lion(Animal):

    def leg_count(self):
        return self.hind_leg+self.rear_leg

class Mouse(Animal):

    def leg_count(self):
        return self.hind_leg+self.rear_leg

class Pigeon(Animal):

    def leg_count(self):
        return self.hind_leg+self.rear_leg


def animal_leg_count(animals):
    
    for animal in animals:
        print(animal.leg_count())


if __name__== "__main__":

    ob_list = [Lion(2,2), Mouse(2,2), Pigeon(0,2)]

    animal_leg_count(ob_list)

