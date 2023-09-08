from game.cell import Cell

class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]

    # def validate_word_inside_board(self, word, location, orientation):
    #     position_x = location[0]
    #     position_y = location[1]
    #     len_word = len(word)
    #     if orientation == "H":
    #         if position_x + len_word > 15:
    #             return False
    #         elif position_y + len_word > 1:
    #             return True 
