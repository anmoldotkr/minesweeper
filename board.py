from cell import Cell
from level import Level


class Board:
    
    def __init__(self,lev:Level):
        """
        Constructor for the Board class.

        Parameters:
        - lev (Level): The difficulty level of the game.
        """
        self.board = self.initialize_array(lev.rows,lev.cols)
    
    
    def get_board(self)->list:
        """
        Return 2d array  representing the board.
        
        return: 2D list of cell instances representing the game
        board.
        """
        return self.board
    
    def initialize_array(self,rows:int,cols:int)->list:
        """
                Initializes the 2D array representing 
                the gameboard with Cell instances.
                
                return: 2D list of cell instances representing the 
                 game board. 

        """
        arr = []
        for i in range(rows):
            row = []
            for j in range(cols):
                c = Cell()
                row.append(c)
            
            arr.append(row)
        return arr
        