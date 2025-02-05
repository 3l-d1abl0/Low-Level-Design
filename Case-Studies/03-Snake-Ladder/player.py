import uuid

#Player for Snak & Ladder
class Player:
    def __init__(self, name: str, pos: int):
        self.__name = name
        self.__id = uuid.uuid4()
        self.__current_position = pos


    def get_id(self) -> str:
        return str(self.__id)
    
    def get_name(self) -> str:
        return self.__name
    
    def get_current_position(self)-> int:
        return self.__current_position
    
    def update_current_position(self, new_pos)-> int:
        self.__current_position = new_pos