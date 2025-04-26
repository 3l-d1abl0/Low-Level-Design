import uuid

#Player for Snak & Ladder
class Player:
    def __init__(self, name: str, pos: int):
        self.__name = name
        self.__id = uuid.uuid4()
        self.__current_position = pos


    def get_id(self) -> str:
        return str(self.__id)
    
    @property
    def name(self) -> str:
        return self.__name
    
    # Getter for board entity - snake or Ladder
    @property
    def current_position(self):
        return self.__current_position
    
    @current_position.setter
    def current_position(self, new_pos):
        self.__current_position = new_pos

    def __str__(self):
        return f"Player: {self.__name}({self.__id}), Position: {self.__current_position}"