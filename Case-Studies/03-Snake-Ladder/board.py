import random
from cell import Cell
from snake import Snake
from ladder import Ladder

class Board:

    def __init__(self, dimension: int, num_snakes: int, num_ladders: int):

        self.__dimension = dimension
        self.__num_snakes = num_snakes
        self.__num_ladders = num_ladders

    @property
    def board_dimension(self):
        return self.__dimension
    
    @property
    def board_snakes(self):
        return self.__num_snakes
    
    @property
    def board_ladders(self):
        return self.__num_ladders

    def init_board(self):
        #Create Board
        self.matrix = [[Cell(row * self.__dimension + col + 1) for col in range(self.__dimension)] for row in range(self.__dimension)]
        self.add_snake_and_ladder()
        self.display_board_info()

    def add_snake_and_ladder(self):
        
        cells_taken = set()
        self.ladder_positions = set()
        self.snake_positions = set()

        # Fill ladders first
        while len(self.ladder_positions) < self.__num_ladders:
            start = random.randint(2, self.__dimension * self.__dimension - 1)
            if start in cells_taken:
                continue
            end = random.randint(start + 1, self.__dimension * self.__dimension)
            if (start,end) not in self.ladder_positions and start != 1 and end != self.__dimension * self.__dimension:
                self.ladder_positions.add((start, end))
                cells_taken.add(start)

        # Place ladders on the board
        for start_cell, end_cell in self.ladder_positions:
            ladder = Ladder(start_cell, end_cell)
            start_cell-=1
            self.matrix[start_cell//self.__dimension][start_cell%self.__dimension].board_entity = ladder

        # Fill snakes next
        while len(self.snake_positions) < self.__num_snakes:
            start = random.randint(2, self.__dimension * self.__dimension - 1)
            if start in cells_taken:
                continue
            end = random.randint(1, start - 1)
            if (start,end) not in self.snake_positions and start != 1 and end != self.__dimension * self.__dimension:
                self.snake_positions.add((start, end))
                cells_taken.add(start)

        # Place snakes on the board
        for start_cell, end_cell in self.snake_positions:
            snake = Snake(start_cell, end_cell)
            start_cell-=1
            self.matrix[start_cell//self.__dimension][start_cell%self.__dimension].board_entity = snake


    def display_board_info(self):

        print(f"Board initalized: ({self.__dimension} x {self.__dimension})")
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                if self.matrix[row][col].board_entity is None:
                    print(self.matrix[row][col].number," ",end="")
                elif isinstance(self.matrix[row][col].board_entity, Snake): 
                    print("S"," ", end="")
                else:
                    print("L"," ", end="")
            print()

        print("=====================")
        print("#####Laddders Info:#####")
        for start_cell, end_cell in self.ladder_positions:
            start_cell-=1
            print(self.matrix[start_cell//self.__dimension][start_cell%self.__dimension].board_entity)

        print("=====================")
        print("#####Snakes Info:#####")
        for start_cell, end_cell in self.snake_positions:
            start_cell-=1
            print(self.matrix[start_cell//self.__dimension][start_cell%self.__dimension].board_entity)


    def process_position(self, pos:int):
        '''
            CAUTION: this function assumes there is not loop caused by ladder+snakes
        '''
        #if position already crosses the winning mark
        if pos >= self.__dimension*self.__dimension:
            return pos
    
        row, col = (pos-1)//self.__dimension, (pos-1)%self.__dimension
        if(self.matrix[row][col].board_entity is None):
            return pos
        else:
            return self.process_position(self.matrix[row][col].board_entity.end)
        

    def check_winner(self, pos: int):

        return True if pos >= self.__dimension*self.__dimension else False