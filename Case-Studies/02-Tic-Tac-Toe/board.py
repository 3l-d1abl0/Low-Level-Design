from symbol import Symbol

class Board:
    def __init__(self, N):
        self.size = N
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
    
    def initialize(self):
        for row in range(self.size):
            for col in range(self.size):
                self.board[row][col] = '_'

    def display_board(self):

        print('= ' * self.size)
        for row in self.board:
            print(row)
        print('= ' * self.size)

    def add_move(self, x: int, y: int, symbol: Symbol) -> bool:

        #Check out of Bound
        if not (0 <= x < self.size):
            return False
        
        if not (0<= y <self.size):
            return False
        
        #Check if not empty/occupied
        if self.board[x][y] != '_':
            return False
        
        self.board[x][y] = symbol.value;

        return True



