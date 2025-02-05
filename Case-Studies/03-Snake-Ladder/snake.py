from board_entity import BoardEntity

class Snake(BoardEntity):
    def __new__(cls, start, end):
        # Validate that start > end for Snake
        if start <= end:
            raise ValueError("For Snake, start must be greater than end.")
        return super().__new__(cls)

    def __init__(self, start, end):
        super().__init__(start, end, 'snake')