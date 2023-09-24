from game.cell import Cell
from game.models import Tile

class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]

    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        valid = False
        if orientation == "V" and location[0] + len_word <= 15 and location[1] + len_word > 1:
            valid = True
        elif orientation == "H" and location[0] + len_word > 1 and location[1] + len_word <= 15:
            valid = True
        return valid
    
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
    
    def word_not_empty_board(self,word:list[Tile],location,orientation):
        if orientation == 'H':
            for i in range(len(word)):
                row = int(location[0])
                column = int(location[1]+i)
                if self.grid[row][column].letter == None:
                    self.grid[row][column].add_letter(word[i])
                elif self.grid[row][column].letter != None:
                    if self.grid[row][column].letter.letter == word[i].letter:
                        pass
                    else:
                        return False
            return True