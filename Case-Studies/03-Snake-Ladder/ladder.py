from board_entity import BoardEntity

class Ladder(BoardEntity):
    def __new__(cls, start, end):
        # Validate that start < end for Ladder
        if start >= end:
            raise ValueError("For Ladder, start must be less than end.")
        return super().__new__(cls)

    def __init__(self, start, end):
        super().__init__(start, end, 'ladder')