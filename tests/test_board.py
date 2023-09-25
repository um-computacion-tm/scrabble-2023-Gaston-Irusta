import unittest
from game.board import Board
from game.models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15,)
        self.assertEqual(len(board.grid[5]),15,)
        self.assertEqual(board.grid[0][0].multiplier,3)
        self.assertEqual(board.grid[0][0].multiplier_type,'word')
        self.assertEqual(board.grid[10][10].multiplier,2)
        self.assertEqual(board.grid[10][10].multiplier_type,'word')
        self.assertEqual(board.grid[6][8].multiplier,2)
        self.assertEqual(board.grid[6][8].multiplier_type,'letter')
        self.assertEqual(board.grid[5][9].multiplier,3)
        self.assertEqual(board.grid[5][9].multiplier_type,'letter')
        

    
    def test_H_True_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (10,3)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, True)
    
    def test_H_False_word_inside_board(self):
        board = Board()
        word = "Universidad"
        location = (6,10)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, False)

    def test_V_True_word_inside_board(self):
        board = Board()
        word = 'Terreno'
        location = (8,9)
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, True)

    def test_V_False_word_inside_board(self):
        board = Board()
        word = 'Sierra'
        location = (15,10)
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, False)

    def test_board_is_empty_True(self):
        board = Board()
        board.grid[7][7].letter = None
        empty = board.is_empty()
        self.assertEqual(empty,True)
        board.grid[7][7].add_letter(Tile('A',1))
        empty = board.is_empty()
        self.assertEqual(empty, False)

    # def test_place_word_not_empty_board_horizontal_fine(self):
    #     board = Board()
    #     board.grid[7][7].add_letter(Tile('C', 1))
    #     board.grid[8][7].add_letter(Tile('A', 1)) 
    #     board.grid[9][7].add_letter(Tile('S', 1)) 
    #     board.grid[10][7].add_letter(Tile('A', 1)) 
    #     word = [
    #         Tile('F',4),
    #         Tile('A',1),
    #         Tile('C',1),
    #         Tile('U',1),
    #         Tile('L',1),
    #         Tile('T',1),
    #         Tile('A',1),
    #         Tile('D',2),
    #     ]
    #     location = (8, 6)
    #     orientation = "H"
    #     word_is_valid_inside = board.validate_word_inside_board(word, location, orientation)
    #     self.assertEqual(word_is_valid_inside,True)
    #     word_is_valid = board.word_not_empty_board(word,location,orientation)
    #     self.assertEqual(word_is_valid,True)
    
    # def test_place_word_not_empty_board_horizontal_bad(self):
    #     board = Board()
    #     board.grid[7][7].add_letter(Tile('C', 1))
    #     board.grid[8][7].add_letter(Tile('O', 1)) 
    #     board.grid[9][7].add_letter(Tile('S', 1)) 
    #     board.grid[10][7].add_letter(Tile('A', 1)) 
    #     word = [
    #         Tile('F',4),
    #         Tile('A',1),
    #         Tile('C',1),
    #         Tile('U',1),
    #         Tile('L',1),
    #         Tile('T',1),
    #         Tile('A',1),
    #         Tile('D',2),
    #     ]
    #     location = (8, 6)
    #     orientation = "H"
    #     word_is_valid_inside = board.validate_word_inside_board(word, location, orientation)
    #     self.assertEqual(word_is_valid_inside,True)
    #     word_is_valid = board.word_not_empty_board(word,location,orientation)
    #     self.assertEqual(word_is_valid,False)

if __name__ == '__main__':
    unittest.main()
