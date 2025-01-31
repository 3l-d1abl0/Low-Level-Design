from symbol import Symbol

class Board:
    def __init__(self, N):
        self.__size = N
        self.__board = [[' ' for _ in range(N)] for _ in range(N)]
    
    def initialize(self):
        for row in range(self.__size):
            for col in range(self.__size):
                self.__board[row][col] = '_'

    def display_board(self):

        print('= ' * self.__size)
        for row in self.__board:
            print(row)
        print('= ' * self.__size)

    def get_size(self)-> int:
        return self.__size
    
    def get_cell(self, x, y) -> str:

        #Check out of Bound
        if not (0 <= x < self.__size):
            raise IndexError
        
        if not (0<= y <self.__size):
            raise IndexError
            
        return self.__board[x][y]

    def add_move(self, x: int, y: int, symbol: Symbol) -> bool:

        #Check out of Bound
        if not (0 <= x < self.__size):
            return False
        
        if not (0<= y <self.__size):
            return False
        
        #Check if not empty/occupied
        if self.__board[x][y] != '_':
            return False
        
        self.__board[x][y] = symbol.value;

        return True



