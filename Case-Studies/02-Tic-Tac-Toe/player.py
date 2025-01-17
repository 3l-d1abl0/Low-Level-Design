from abc import ABC, abstractmethod
from symbol import Symbol
import random

# Abstract Player class
class Player(ABC):
    def __init__(self, symbol: Symbol, name: str):
        self.symbol = symbol
        self.name = name

    def get_symbol(self) -> Symbol:
        return self.symbol
    
    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def make_move(self):
        pass

# HumanUser class (inherits from Player)
class HumanUser(Player):
    def __init__(self, symbol: Symbol, name: str):
        super().__init__(symbol, name)

    def make_move(self):
        # Logic for human input (e.g., user typing row/column coordinates)
        print(f"Human ({self.symbol.value}) make your move!")



# # ComputerUser class (inherits from Player)
# class ComputerUser(Player):
#     def __init__(self, symbol: Symbol):
#         super().__init__(symbol, "COMPUTER_"+random.randint(1000,9999))

#     def make_move(self):
#         # Logic for computer move (AI/Random move for simplicity)
#         print(f"Computer ({self.symbol.value}) makes a move!")
