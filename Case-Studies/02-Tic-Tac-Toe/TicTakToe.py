#import game
from symbol import Symbol
from player import HumanUser

class TicTakToe:

    def play(self):

        print('## Setting up a New Game ##')
        '''
            A game has two Player and a Board

            Later:
                - Player can be human or computer
                - Add Playing strategy if computer

        '''
        #Gather Board Size
        board_size = input("Enter the Board Size: ")

        all_symbols = {symbol.value : symbol for symbol in Symbol}
        available_symbols = set(all_symbols.keys())

        #Gather Player one Detail
        player_one = self.gather_player_details("player1", all_symbols, available_symbols)

        #Gather Player two Detail
        player_two = self.gather_player_details("player2", all_symbols, available_symbols)


        print(player_one)
        print(player_two)
        



    def gather_player_details(self, player, all_symbols, available_symbols):
        print(f"## {player} Attention !!! ##")
        player_one_name = input(f"Enter {player} name: ")

        player_one_symbol = input(f"Enter {player} symbol: {available_symbols} ")

        #print(f"ALL: {available_symbols}")
        if player_one_symbol not in available_symbols:
            return;
    
        #Remove players choice from Symbol
        available_symbols.discard(player_one_symbol)

        new_player = HumanUser(all_symbols[player_one_symbol], player_one_name)

        return new_player