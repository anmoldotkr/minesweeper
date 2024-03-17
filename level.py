from enum import Enum

class Level(Enum):
    EASY = (9,9,10)
    INTERMEDIATE = (16,16,40)
    EXPERT = (16,30,99)
    
    
    def __init__(self,rows,cols,bombs):
        self.bombs = bombs
        self.rows = rows
        self.cols = cols