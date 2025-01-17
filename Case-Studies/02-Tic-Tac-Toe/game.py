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

            for pla in self.players:
                print(pla.get_name(),)
            
            current_player = self.players.popleft()

            current_player_cell = input(f"Move: #{self.moves} Player: {current_player.get_name()} ({current_player.get_symbol().value}) Enter: X, Y: ")
            x, y = map(int, current_player_cell.split(','))
            print(x, y)


            symbol_added = self.board.add_move(x, y, current_player.get_symbol())

            if symbol_added == False:
                print("Invalid Move : Try Again")
                self.players.appendleft(current_player)
                continue

            #valid Move
            self.moves +=1
            self.free_cells -=1
            print('valid Move')
            
            self.board.display_board()

            if self.check_winner(x, y, current_player):
                print("WINNER !!!: ", current_player.get_name())
                return current_player
            
            if self.free_cells == 0:
                print("Its a TIE !!!!!")
                return False
            
            #otherwise prepare for next Move
            self.players.append(current_player)
            

    def check_winner(self, x: int, y: int, current_player: HumanUser) -> bool:

        row_check = True
        #1. Row Check
        for col in range(0, self.board.get_size()):

            if self.board.get_cell(x, col)!= current_player.get_symbol().value:
                row_check = False
                break


        #2. Column Check
        col_check = True
        for row in range(0, self.board.get_size()):

            if self.board.get_cell(row,y) != current_player.get_symbol().value:
                col_check = False
                break
            
        #3. Diagonal Check (top-left to bottom right)
        dia_check = True
        for rc in range(0, self.board.get_size()):

            if self.board.get_cell(rc, rc) != current_player.get_symbol().value:
                dia_check = False
                break

        #4. anti-dia Check  (top-right to bottom-left)
        anti_dia_check = True
        row =0
        for col in range(self.board.get_size() -1, -1, -1):
            if self.board.get_cell(row, col) != current_player.get_symbol().value:
                anti_dia_check = False
                break
            row+=1


        return row_check | col_check | dia_check | anti_dia_check