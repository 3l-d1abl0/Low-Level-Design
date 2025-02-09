from board_entity import BoardEntity

class Cell:
    def __init__(self, number: int):
        self.__number: int = number
        self.__board_entity : BoardEntity = None

    

    #Getter-Setter for cell number
    def get_cell_number(self):
        return self.__number

    # creating a property object
    number = property(get_cell_number)


    # Getter for board entity - snake or Ladder
    @property
    def board_entity(self):
        return self.__board_entity

    # Setter for board_entity
    @board_entity.setter
    def start(self, snake_or_ladder: BoardEntity):
        self.__board_entity = snake_or_ladder