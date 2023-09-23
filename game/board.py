from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]

    # def add_letter(self):
        
    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        valid = False
        if orientation == "V" and location[0] + len_word <= 15 and location[1] + len_word > 1:
            valid = True
        elif orientation == "H" and location[0] + len_word > 1 and location[1] + len_word <= 15:
            valid = True
        return valid