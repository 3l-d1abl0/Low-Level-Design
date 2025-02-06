class BoardEntity:
    def __init__(self, start: int, end: int, type: str):
        self.__start = start  # Private attribute
        self.__end = end      # Private attribute
        self.__type = None    # Private attribute, will be overridden in child classes

    # Getter for start
    @property
    def start(self):
        return self.__start

    # Setter for start
    @start.setter
    def start(self, value):
        self.__start = value

    # Getter for end
    @property
    def end(self):
        return self.__end

    # Setter for end
    @end.setter
    def end(self, value):
        self.__end = value

    # Getter for type
    @property
    def type(self):
        return self.__type

    # Setter for type
    @type.setter
    def type(self, value):
        self.__type = value

    def __str__(self):
        return f"{self.type.capitalize()}: Start at {self.start}, End at {self.end}"





class Ladder(BoardEntity):
    def __init__(self, start, end):
        super().__init__(start, end)
        self.type = 'ladder'  # Override the type
