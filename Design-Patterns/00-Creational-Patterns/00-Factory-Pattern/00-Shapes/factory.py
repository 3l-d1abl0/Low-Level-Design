import random
import abc
import enum


class ShapeSystem(enum.Enum):
    CIRCLE = 1
    RECTANGLE = 2


#Base abstract class for shapes
class Shape(object):
        '''Abstract Base Class Definition'''
        __metaclass__ = abc.ABCMeta

        def __init__(self, x: int, y: int):
            self.x  = x
            self.y = y

        @abc.abstractmethod
        def draw(self, screen: string):
            pass


#Circle inherits Shape
class Circle(Shape):
    def __init__(self, x: int, y:int):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        #RGB
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #Draw the circle on the Given Screen
    def draw(self, screen: string):
        print(f"Drawing Circle at {self.x}, {self.y} with radius {self.radius} and color {self.color}")


#Rectangele inherits Shape
class Rectangle(Shape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #Draw the circle on the Given Screen
    def draw(self, screen: string):
        print(f"Drawing Rectangle at {self.x}, {self.y} with height {self.height} and width {self.width} and color {self.color}")


#Shape factory class for Creating Shape Instances
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: ShapeSystem, x: int , y: int):

        if shape_type == ShapeSystem.CIRCLE:
            return Circle(x, y)
        elif shape_type == ShapeSystem.RECTANGLE:
            return Rectangle(x, y)
        else:
            print(shape_type)
            print(ShapeSystem.CIRCLE)
            raise ValueError("Invalid Shape Type")
