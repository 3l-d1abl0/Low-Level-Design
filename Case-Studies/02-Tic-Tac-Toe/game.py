from player import HumanUser
from collections import deque
from board import Board
from collections import deque


class Game:

    def __init__(self, board_size: int, player_one: HumanUser, player_two: HumanUser):
        self.board_size = board_size
        self.free_cells = board_size*board_size
        self.moves = 0
        self.player_one = player_one
        self.player_two = player_two
        self.board = Board(self.board_size)
        self.players = deque()
        self.players.append(player_one)
        self.players.append(player_two);


    def initialize_game(self):
        print("## Setting up Board##")
        self.board.initialize()
        self.board.display_board()

    def play(self):

        no_winner : bool = True

        while no_winner:

            current_player = self.players.popleft()

            current_player_cell = input(f"Player: {current_player.get_name()} Enter: X, Y: ")
            x, y = map(int, current_player_cell.split(','))
            print(x, y)


            symbol_added = self.board.addMove(x, y, current_player.get_symbol())

            if symbol_added == False:
                print("Invalid Move : Try Again")
                self.players.appendleft(current_player)
                continue

            #valid Move
            self.moves +=1
            self.free_cells -=1
            self.players.append(current_player)

            if self.check_winner(x, y, current_player):
                return current_player
            
            #otherwise prepare for next Move
            self.players.append(current_player)
            self.board.display_board()

    def check_winner(self, x: int, y: int, current_player: HumanUser) -> bool:

        row_check = True
        #1. Row Check
        for col in range(0, self.board.size):

            if self.board[x][col] != current_player.get_symbol().value:
                row_check = False
                break


        #2. Column Check
        col_check = True
        for row in range(0, self.board.size):

            if self.board[row][y] != current_player.get_symbol().value:
                col_check = False
                break
            
        #3. Diagonal Check (top-left to bottom right)
        dia_check = True
        for rc in range(0, self.board.size):

            if self.board[rc][rc] != current_player.get_symbol().value:
                dia_check = False
                break

        #4. anti-dia Check  (top-right to bottom-left)
        anti_dia_check = True
        row =0
        for col in range(self.board.size -1, 0, -1):
            if self.board[row][col] != current_player.get_symbol().value:
                anti_dia_check = False
                break
            row+=1


        return row_check | col_check | dia_check | anti_dia_check