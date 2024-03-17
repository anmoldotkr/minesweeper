from board import Board
from score import Score
import random
from topscore import TopScorer


class Minesweeper:
    def __init__(self, lev, name):
        self.level = lev
        self.numMines = lev.value[2]
        self.board = Board(lev)
        self.score = Score(lev)
        self.ts = TopScorer(name)
        self.numberOfClick = 0

    def print_board(self):
        s = "----------------------GAME-BOARD---------------------\n"
        for i in range(self.level.rows):
            s += "-----------------------------------------------------\n"
            for j in range(self.level.cols):
                if self.board.get_board()[i][j].is_clicked():
                    s += " " + str(self.board.get_board()[i][j].get_num_neighbors()) + " | "
                elif self.board.get_board()[i][j].is_flagged():
                    s += "# # # | "
                else:
                    s += str(i) + "," + str(j) + " | "
            s += "\n"
        s += "-----------------------------------------------------\n"
        s += "----------------------GAME-BOARD---------------------\n"
        return s

    def reveal_mine(self):
        s = "------------------------BOMBS------------------------\n"
        for i in range(len(self.board.get_board())):
            s += "-----------------------------------------------------\n"
            for j in range(len(self.board.get_board()[i])):
                if not self.board.get_board()[i][j].is_mine():
                    if self.board.get_board()[i][j].get_num_neighbors() != -1:
                        s += " " + str(self.board.get_board()[i][j].get_num_neighbors()) + " | "
                        continue
                    s += str(i) + "," + str(j) + " | "
                else:
                    s += " * | "
            s += "\n"
        s += "-----------------------------------------------------\n"
        s += "------------------------BOMBS------------------------\n"
        return s

    def make_first_click(self, row, col):
        if self.numberOfClick == 0:
            self.score.update_revel_ans()
            self.board.get_board()[row][col].set_clicked(True)
            self.numberOfClick += 1
            self.mine_generator()
            self.set_number_to_neighboring_mines(self.board)

    def make_click(self, row, col):
        self.make_first_click(row, col)
        if self.board.get_board()[row][col].is_mine():
            self.ts.set_score(self.score.get_score())
            try:
                self.ts.write_file()
                self.ts.read_file()
            except Exception as e:
                print(e)
            return "----------------------game over----------------------\n" + "\n" + self.reveal_mine()
        elif self.board.get_board()[row][col].get_num_neighbors() > 0:
            self.board.get_board()[row][col].set_clicked(True)
            self.score.update_revealed_cells()
        elif self.board.get_board()[row][col].get_num_neighbors() == 0:
            self.check_neighbour(row, col)
            self.show_neighbour_of_zero()
        return ""
    
    def check_neighbour(self, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i >= 0 and row + i < len(self.board.get_board()) and col + j >= 0 and col + j < len(self.board.get_board()[0]) and self.board.get_board()[row + i][col + j].get_num_neighbors() == 0 and not self.board.get_board()[row + i][col + j].is_flagged() and not self.board.get_board()[row + i][col + j].is_clicked():
                    self.board.get_board()[row + i][col + j].set_clicked(True)
                    self.score.update_revealed_cells()
                    self.check_neighbour(row + i, col + j)

    def show_neighbour_of_zero(self):
        for x in range(len(self.board.get_board())):
            for y in range(len(self.board.get_board()[x])):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if self.board.get_board()[x][y].get_num_neighbors() == 0 and self.board.get_board()[x][y].is_clicked():
                            if x + i >= 0 and x + i < len(self.board.get_board()[x]) and y + j >= 0 and y + j < len(self.board.get_board()[x]):
                                if not self.board.get_board()[x + i][y + j].is_flagged() and not self.board.get_board()[x + i][y + j].is_clicked():
                                    self.board.get_board()[x + i][y + j].set_clicked(True)
                                    self.score.update_revealed_cells()

    def mine_generator(self):
        rand = random.Random()
        for _ in range(self.numMines):
            x = rand.randint(0, self.level.rows - 1)
            y = rand.randint(0, self.level.cols - 1)
            if not self.board.get_board()[x][y].is_mine() and not self.board.get_board()[x][y].is_clicked():
                self.board.get_board()[x][y].set_mine(True)
            else:
                _ -= 1

    def make_flagged(self, row, col, f):
        if self.numberOfClick > 0:
            if not self.board.get_board()[row][col].is_clicked():
                self.board.get_board()[row][col].set_flagged(f)
                if self.board.get_board()[row][col].is_flagged() and self.board.get_board()[row][col].is_mine():
                    self.score.update_flagged_mines()
                elif self.board.get_board()[row][col].is_flagged() and not self.board.get_board()[row][col].is_mine():
                    self.score.update_incorrect_flags()
                return "set to falagged"
        return "cannot set to falgged"

    def set_number_to_neighboring_mines(self, board):
        for x in range(len(board.get_board())):
            for y in range(len(board.get_board()[x])):
                num_neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x + i >= 0 and x + i < len(board.get_board()[x]) and y + j >= 0 and y + j < len(board.get_board()[x]):
                            if board.get_board()[x + i][y + j].is_mine():
                                num_neighbors += 1
                board.get_board()[x][y].set_num_neighbors(num_neighbors)

    def get_boardd(self):
        return self.board

    def win(self):
        count = 0
        for x in range(len(self.board.get_board())):
            for y in range(len(self.board.get_board()[x])):
                if self.board.get_board()[x][y].is_clicked() or self.board.get_board()[x][y].is_flagged():
                    count += 1
        if self.level.cols * self.level.rows == count:
            try:
                self.ts.write_file()
                self.ts.read_file()
            except Exception as e:
                print(e)
            return True
        return False