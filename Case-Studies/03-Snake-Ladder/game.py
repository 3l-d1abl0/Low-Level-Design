from player import Player
from board import Board
from collections import deque
from dice import DiceType, DiceFactory


class Game:

    def __init__(self, num_players: int, dimension: int, num_ladders: int, num_snakes: int):
        self.num_players = num_players
        self.players = deque()
        self.board = Board(dimension, num_ladders, num_snakes)

    def prepare(self):

        #1. Initialize Players
        self.set_up_players()
        print("=====================")
        #2. Initialize Board
        self.set_up_board()

        #3. Initialize Dice
        self.set_up_dice()

    def set_up_players(self):

        self.players.append(Player("P1", 0))
        self.players.append(Player("P2", 0))
        self.players.append(Player("P3", 0))
        self.players.append(Player("P4", 0))
        self.players.append(Player("P5", 0))
        self.players.append(Player("P6", 0))
        
        for player in self.players:
            print(player)
    
    def set_up_board(self):
        self.board.init_board()

    def set_up_dice(self):
        self.dice = DiceFactory.create_die(DiceType.NORMAL, 'RED', 6)


    def game_start(self):

        print("=====================")
        print("#####Starting new Round of Snake and Ladder#####")

        self.winners_list = []
        self.winners_count = 3

        #Start a Game
        while(len(self.winners_list)<self.winners_count):

            current_player = self.players.popleft()

            #Dice for current Player
            val = self.dice.roll()
            new_position = current_player.current_position+val
            updated_new_position = self.board.process_position(new_position)
            current_player.current_position = updated_new_position

            print(f"{current_player.name} at {updated_new_position}")
            if(self.board.check_winner(updated_new_position)):
                print(f"WINNER #{len(self.winners_list)+1}: {current_player.name}")
                self.winners_list.append(current_player)#found a Winner
            else:
                self.players.append(current_player)

        
        if(len(self.winners_list) == self.winners_count):
            print("#####Winners of the Game:#####")
            for idx, player in enumerate(self.winners_list):
                print(f"#{idx+1}: {player}")
        else:
            raise Exception("Something went Wrong!")

if __name__ == "__main__":

    snake_and_ladder_game = Game(3, 10, 4, 4)
    
    snake_and_ladder_game.prepare()

    snake_and_ladder_game.game_start()