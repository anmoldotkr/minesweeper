# from minesweeper import Minesweeper
from minesweeper import Minesweeper
from level import Level
class Play:
    
    def __init__(self):
        self.sc = input
        self.game()
    
    def game(self):
        
        print("-----Enter your Name-------")
        name = input()
        m1 = Minesweeper(Level.EASY,name)
        
        while True:
            
            print(m1.print_board())
            print("Enter your choice:\n"+
                  "1. click on position\n"+
                  "2. Mark as flagged\n"+
                  "3. Mark as unflaggd\n"+
                  "4. Reveal the Bombs\n"+
                  "5. Restart the game\n"+
                  "6. Quit Game")
            choice = int(input())
            
            if m1.win():
              print("CONGRATULATIONS! YOU WON THE MATCH")
            
            if choice == 6:
                break
            
            elif choice == 1:
                print("Enter the position  to be clicked : eg:(0,0 as 00)")
                position = input()
                row = int(position[0])
                col = int(position[1])
                print(m1.make_click(row,col))
                
                if m1.get_boardd().get_board()[row][col].is_mine():
                    break
            
            elif choice in [2,3]:
                flag_text = "flagged" if choice == 2 else  "unflagged"
                print("Enter the position to be nake it as "+flag_text+": ")
                pos = input()
                row = int(pos[0])
                col = int(pos[1])
                m1.make_flagged(row,col, choice==2)
            
            elif choice == 4:
                print(m1.reveal_mine())
            
            elif choice == 5:
                self.game()                
            
            else:
                print("enter valid choice")
                

            