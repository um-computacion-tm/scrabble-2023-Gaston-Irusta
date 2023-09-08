import unittest
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15,)
        self.assertEqual(len(board.grid[5]),15,)
    
'''    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5,10)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word,location,orientation)'''


if __name__ == '__main__':
    unittest.main()
