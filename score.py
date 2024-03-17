from level import Level

class Score:
    
    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.revealed_cells = 0
        self.flagged_mines = 0
        self.incorrect_flags = 0
        self.revel_ans = 0
        
    def update_revealed_cells(self):
        self.revealed_cells +=1
    
    def update_revel_ans(self):
        self.revel_ans +=1
    
    def update_flagged_mines(self):
        self.flagged_mines+=1
    
    def update_incorrect_flags(self):
        self.incorrect_flags+=1
    
    def get_score(self):
        points = 0
        
        if self.difficulty == Level.EASY:
            points +=10
        if self.difficulty == Level.INTERMEDIATE:
            points+=20
        
        if self.difficulty == Level.EXPERT:
            points+=30
        
        else:
            raise ValueError("Invalid Difficulty Level")
        
        points *= self.revealed_cells
        points +=self.flagged_mines*50
        points-=self.incorrect_flags*20
        points -= self.revel_ans*10
        return points        