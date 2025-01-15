class Board:
    def __init__(self, N):
        self.size = N
        self.board = [[' ' for _ in range(N)] for _ in range(N)]
    
    def initialize(self):
        for row in self.board:
            for col in row:
                col = '_'

    def display_board(self):

        print('=' * self.size)
        for row in self.board:
            print(row)
        print('=' * self.size)

