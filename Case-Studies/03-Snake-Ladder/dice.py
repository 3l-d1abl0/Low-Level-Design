import enum
from abc import ABC, abstractmethod
import random
import copy

class DiceType(enum.Enum):
    NORMAL = 1
    NEGATIVE = 2
    RANDOM = 3
    CUSTOM_VALUES = 4


#Base abstract class for Dice
class Dice(ABC):
        
        def __init__(self, color: str, sides: int):
            self.__color  = color
            self.__sides = sides

        @abstractmethod
        def roll(self):
            pass


#Normal Dice inherits Dice
class NormalDice(Dice):

    def __init__(self, color: str, sides: int):
        super().__init__(color, sides)
        self.radius = random.randint(10, 50)
        #RGB
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #Draw the normal dice and return a value between 1-6
    def roll(self):
        return random.randint(1,self.sides)
    
    @classmethod
    def checkDice(cls, sides):
        return True if sides >0 else False

#Negative Dice inherits Dice
class NegativeDice(Dice):

    def __init__(self, color: str, sides: int, custom_values: list[int]):
        super().__init__(color, sides)

        self.values = [1] * self.__sides
        self.dice_setup(custom_values)
    
    def dice_setup(self, custom_values: list[int]):
        side =0
        #Fill the negative values First
        for val in custom_values:
            self.values[side]= val
            side+=1
        #Fill the rest of the side with normal values
        val =1
        for idx in range(side, self.__sides):
            self.values[side] = val
            val+=1


    def __str__(self):
        return f"Negative Dice is just a normal dice with custom negative values"

    def roll(self):
        return random.choice(self.values)
    
    @classmethod
    def check_dice(cls, sides: int, custom_values: list[int]):
        if len(custom_values) == 0 or len(custom_values) > sides:
                return False, "Invalid size of Custom Values"
            
        if any(num >=0 for num in custom_values):
                return False, "All custom values should be Negative !"
        
        return True, ""
    

class RandomDice(Dice):

    def __init__(self, color: str, sides: int):
        super().__init__(color, sides)
        self.values = [random.randint(-sides, sides) for _ in range(sides)]
    
    def __str__(self):
        return f"Contain random values from -{self.sides} to {self.sides}"
    
    def roll(self):
        return random.choice(self.values)


class CustomDice(Dice):

    def __init__(self, color: str, sides: int, custom_values: list[int]):
        super().__init__(color, sides)
        self.values = copy.deepcopy(custom_values)
    
    def __str__(self):
        return f"Contain custom values !"
    
    def roll(self):
        return random.choice(self.values)
    
    @classmethod
    def check_dice(cls, sides: int, custom_values: list[int]):

        if len(custom_values) != sides:
                raise ValueError("Need custom values for all Sides !")
        
        return True, ""

class DiceFactory:
    @staticmethod
    def create_die(dice_type: DiceType, color: str, sides: int , custom_values: list[int]):

        if sides <= 0:
            raise ValueError("Side should be a positive Value !")
        elif dice_type == DiceType.NORMAL:
            if not NormalDice.checkDice(sides):
                raise ValueError("Invalid size for a Normal Dice !")
            return NormalDice('red', 6)
        
        elif dice_type == DiceType.NEGATIVE:
            status, msg = NegativeDice.checkDice(sides, custom_values)
            if not status:
                raise ValueError(msg)
            
            return NegativeDice(color, sides, custom_values)
        
        elif dice_type == DiceType.RANDOM:
            return RandomDice(color, sides)
        
        elif dice_type == DiceType.CUSTOM_VALUES:

            status, msg = CustomDice.checkDice(sides, custom_values)
            if not status:
                raise ValueError(msg)
            
            return CustomDice(color, sides, custom_values)
        
        else:
            print(dice_type)
            raise ValueError("Invalid Dice Type !")

