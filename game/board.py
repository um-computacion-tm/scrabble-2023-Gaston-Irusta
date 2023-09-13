from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]

    def validate_word_inside_board(self, word, location, orientation):
        orientation = orientation.upper()
        valid = False
        if orientation == "H":
            if location[0] + len(word) <= 15 and location[1] + len(word) > 1:
                valid = True
        elif orientation == "V":
            if location[1] + len(word) <= 15 and location[0] + len(word) > 1:
                valid = True
        return valid
    