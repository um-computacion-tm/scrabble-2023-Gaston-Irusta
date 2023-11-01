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
        empty = board.is_empty()
        self.assertEqual(empty,True)

    def test_board_is_empty_False(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('A',1))
        empty = board.is_empty()
        self.assertEqual(empty, False)

    def test_use_letters_on_board(self):
        board = Board()

        board.grid[5][3].add_tile(Tile('G',1))
        board.grid[5][4].add_tile(Tile('A',1))
        board.grid[5][5].add_tile(Tile('T',1))
        board.grid[5][6].add_tile(Tile('O',1))

        board.grid[9][3].add_tile(Tile('C',1))
        board.grid[9][4].add_tile(Tile('O',1))
        board.grid[9][5].add_tile(Tile('C',1))
        board.grid[9][6].add_tile(Tile('O',1))

        word = 'CORCHO'
        word = list(word)
        location = [4,6]
        word_return = board.use_letter_on_board_V(word,location)
        self.assertNotEqual(word_return,word)

    def test_validate_word_and_letters_True(self):
        board = Board()
        word = 'LENTO'
        word = list(word)
        player_tiles = [
            Tile('L',1),
            Tile('E',1),
            Tile('N',1),
            Tile('T',1),
            Tile('O',1),
            Tile('S',1),
            Tile('A',1),
        ]
        location = [5,7]
        orientation = 'V'
        valid = board.validate_word_and_letters(word,location,orientation,player_tiles)
        self.assertEqual(valid,True)

    def test_validate_word_and_letters_False(self):
        board = Board()
        word = 'PUNTO'
        word = list(word)
        player_tiles = [
            Tile('L',1),
            Tile('E',1),
            Tile('N',1),
            Tile('T',1),
            Tile('O',1),
            Tile('S',1),
            Tile('A',1),
        ]
        location = [7,5]
        orientation = 'H'
        valid = board.validate_word_and_letters(word,location,orientation,player_tiles)
        self.assertEqual(valid,False)

    def test_validate_place_board_not_empty_H(self):
        board = Board()
        board.grid[5][7].add_tile(Tile('L',1))
        board.grid[6][7].add_tile(Tile('O',1))
        board.grid[7][7].add_tile(Tile('S',1))
        board.grid[8][7].add_tile(Tile('A',1))
        word = 'APESTA'
        location = (7,2)
        orientation = 'H'
        valid = board.validate_place_board_not_empty(word,location,orientation)
        self.assertEqual(valid,True)

    def test_validate_place_board_not_empty_V(self):
        board = Board()
        board.grid[7][5].add_tile(Tile('L',1))
        board.grid[7][6].add_tile(Tile('O',1))
        board.grid[7][7].add_tile(Tile('S',1))
        board.grid[7][8].add_tile(Tile('A',1))
        word = 'RESTA'
        location = (3,8)
        orientation = 'V'
        valid = board.validate_place_board_not_empty(word,location,orientation)
        self.assertEqual(valid,True)       

    def test_validate_word_board_not_empty_H_True(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('C', 1))
        board.grid[8][7].add_tile(Tile('A', 1)) 
        board.grid[9][7].add_tile(Tile('S', 1)) 
        board.grid[10][7].add_tile(Tile('A', 1))
        word = 'FACULTAD'
        location = (8,6)
        orientation = 'H'
        word_is_valid = board.validate_word_board_not_empty(word,location,orientation)
        self.assertEqual(word_is_valid,True)

    def test_validate_word_board_not_empty_H_False(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('C', 1))
        board.grid[8][7].add_tile(Tile('O', 1)) 
        board.grid[9][7].add_tile(Tile('S', 1)) 
        board.grid[10][7].add_tile(Tile('A', 1))
        word = 'FACULTAD'
        location = (8,6)
        orientation = 'H'
        word_is_valid  = board.validate_word_board_not_empty(word,location,orientation)
        self.assertEqual(word_is_valid,False)

    def test_validate_word_board_not_empty_V_True(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('L', 1))
        board.grid[7][8].add_tile(Tile('O', 1)) 
        board.grid[7][9].add_tile(Tile('M', 1)) 
        board.grid[7][10].add_tile(Tile('A', 1))
        word = 'TORNADO'
        location = (6,8)
        orientation = 'V'
        word_is_valid = board.validate_word_board_not_empty(word,location,orientation)
        self.assertEqual(word_is_valid,True)

    def test_validate_word_board_not_empty_V_False(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('L', 1))
        board.grid[7][8].add_tile(Tile('A', 1)) 
        board.grid[7][9].add_tile(Tile('N', 1)) 
        board.grid[7][10].add_tile(Tile('A', 1))
        word = 'PALOMA'
        location = (5,8)
        orientation = 'V'
        word_is_valid = board.validate_word_board_not_empty(word,location,orientation)
        self.assertEqual(word_is_valid,False)

    def test_add_word_empty_board_H(self):
        board = Board()
        word_tiles = [
            Tile('A',1),
            Tile('M',1),
            Tile('A',1),
            Tile('C',1),
            Tile('A',1)
        ]
        location = (7,3)
        orientation = 'H'
        word_is_added = board.add_word_empty_board(word_tiles,location,orientation)
        self.assertEqual(word_is_added,True)
        
    def test_add_word_empty_board_V(self):
        board = Board()
        word_tiles = [
            Tile('A',1),
            Tile('T',1),
            Tile('R',1),
            Tile('A',1),
            Tile('S',1)
        ]
        location = (3,7)
        orientation = 'V'
        word_is_added = board.add_word_empty_board(word_tiles,location,orientation)
        self.assertEqual(word_is_added,True)

    def test_add_word_not_empty_board_H_True(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('C', 1))
        board.grid[8][7].add_tile(Tile('A', 1)) 
        board.grid[9][7].add_tile(Tile('S', 1)) 
        board.grid[10][7].add_tile(Tile('A', 1)) 
        word_tiles = [
            Tile('F',4),
            Tile('A',1),
            Tile('C',1),
            Tile('U',1),
            Tile('L',1),
            Tile('T',1),
            Tile('A',1),
            Tile('D',2),
        ]
        location = (8, 6)
        orientation = "H"
        word_is_valid_inside = board.validate_word_inside_board(word_tiles, location, orientation)
        self.assertEqual(word_is_valid_inside,True)
        word_is_added = board.add_word_not_empty_board(word_tiles,location,orientation)
        self.assertEqual(word_is_added,True)
    
    def test_add_word_not_empty_board_H_False(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('C', 1))
        board.grid[8][7].add_tile(Tile('O', 1)) 
        board.grid[9][7].add_tile(Tile('S', 1)) 
        board.grid[10][7].add_tile(Tile('A', 1)) 
        word_tiles = [
            Tile('F',4),
            Tile('A',1),
            Tile('C',1),
            Tile('U',1),
            Tile('L',1),
            Tile('T',1),
            Tile('A',1),
            Tile('D',2),
        ]
        location = (8, 6)
        orientation = "H"
        word_is_valid_inside = board.validate_word_inside_board(word_tiles, location, orientation)
        self.assertEqual(word_is_valid_inside,True)
        word_is_added = board.add_word_not_empty_board(word_tiles,location,orientation)
        self.assertEqual(word_is_added,False)

    def test_add__word_not_empty_board_V_True(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('L', 1))
        board.grid[7][8].add_tile(Tile('O', 1)) 
        board.grid[7][9].add_tile(Tile('M', 1)) 
        board.grid[7][10].add_tile(Tile('A', 1)) 
        word_tiles = [
            Tile('T',1),
            Tile('O',1),
            Tile('R',1),
            Tile('N',1),
            Tile('A',1),
            Tile('D',2),
            Tile('O',1),
        ]
        location = (6, 8)
        orientation = "V"
        word_is_valid_inside = board.validate_word_inside_board(word_tiles, location, orientation)
        self.assertEqual(word_is_valid_inside,True)
        word_is_added = board.add_word_not_empty_board(word_tiles,location,orientation)
        self.assertEqual(word_is_added,True)
    
    def test_add_word_not_empty_board_V_False(self):
        board = Board()
        board.grid[7][7].add_tile(Tile('L', 1))
        board.grid[7][8].add_tile(Tile('A', 1)) 
        board.grid[7][9].add_tile(Tile('N', 1)) 
        board.grid[7][10].add_tile(Tile('A', 1)) 
        word_tiles = [
            Tile('P',3),
            Tile('A',1),
            Tile('L',1),
            Tile('O',1),
            Tile('M',3),
            Tile('A',1),
        ]
        location = (5, 8)
        orientation = "V"
        word_is_valid_inside = board.validate_word_inside_board(word_tiles, location, orientation)
        self.assertEqual(word_is_valid_inside,True)
        word_is_added = board.add_word_not_empty_board(word_tiles,location,orientation)
        self.assertEqual(word_is_added,False)

if __name__ == '__main__':
    unittest.main()
