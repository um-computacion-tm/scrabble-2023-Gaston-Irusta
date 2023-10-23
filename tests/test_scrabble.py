import unittest
from game.scrabble import ScrabbleGame
from game.models import Tile

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),3,)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_player_tiles(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        self.assertEqual(len(scrabble_game.players[0].tiles), 7)
        self.assertEqual(len(scrabble_game.players[1].tiles), 7)
        self.assertEqual(len(scrabble_game.players[2].tiles), 7)
        self.assertEqual(len(scrabble_game.bag_tiles.tiles),82)

    def test_joker_to_end(self):
        game = ScrabbleGame(2)
        game.initial_turn()
        game.current_player.tiles[2] = Tile('?',0)
        game.wild_tile_to_end()
        self.assertNotEqual(game.current_player.tiles[2].letter,'?')
        self.assertEqual(game.current_player.tiles[6].letter,'?')

    def test_inicial_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = None
        scrabble_game.initial_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[0])

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[1])

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[0])

    def test_list_cells_H(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.board.grid[7][5].add_tile(Tile('R',1))
        scrabble_game.board.grid[7][6].add_tile(Tile('A',1))
        scrabble_game.board.grid[7][7].add_tile(Tile('T',1))
        scrabble_game.board.grid[7][8].add_tile(Tile('O',1))
        scrabble_game.board.grid[7][9].add_tile(Tile('N',1))
        word = 'RATON'
        location = (7,5)
        orientation = 'H'
        cells = scrabble_game.list_cells(word,location,orientation)
        self.assertEqual(len(cells),5)
        self.assertEqual(cells[0].tile.letter,'R')
        self.assertEqual(cells[1].tile.value,1)
        self.assertEqual(cells[2].multiplier,2)
        self.assertEqual(cells[3].multiplier_type,'')
        self.assertNotEqual(cells[4].tile,None)

    def test_list_cells_V(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.board.grid[6][6].add_tile(Tile('L',1))
        scrabble_game.board.grid[7][6].add_tile(Tile('A',1))
        scrabble_game.board.grid[8][6].add_tile(Tile('T',1))
        scrabble_game.board.grid[9][6].add_tile(Tile('A',1))
        word = 'LATA'
        location = (6,6)
        orientation = 'V'
        cells = scrabble_game.list_cells(word,location,orientation)
        self.assertEqual(len(cells),4)
        self.assertEqual(cells[0].multiplier,2)
        self.assertEqual(cells[1].tile.value,1)
        self.assertEqual(cells[2].multiplier_type,'letter')
        self.assertEqual(cells[3].tile.letter,'A')

    def test_score_sum_1(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.initial_turn()
        scrabble_game.board.grid[5][7].add_tile(Tile('D',2))
        scrabble_game.board.grid[6][7].add_tile(Tile('U',1))
        scrabble_game.board.grid[7][7].add_tile(Tile('C',3))
        scrabble_game.board.grid[8][7].add_tile(Tile('H',4))
        scrabble_game.board.grid[9][7].add_tile(Tile('A',1))
        word = 'DUCHA'
        location = (5,7)
        orientation = 'V'
        scrabble_game.score_sum(word,location,orientation)
        self.assertEqual(scrabble_game.players[0].score,22)

    def score_sum_2(self):
        scrabble_game = ScrabbleGame(players_count=4)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.players[3].score = 24
        scrabble_game.next_turn()
        scrabble_game.board.grid[7][3].add_tile(Tile('L',1))
        scrabble_game.board.grid[7][4].add_tile(Tile('L',1))
        scrabble_game.board.grid[7][5].add_tile(Tile('A',1))
        scrabble_game.board.grid[7][6].add_tile(Tile('V',4))
        scrabble_game.board.grid[7][7].add_tile(Tile('E',1))
        word = 'LLAVE'
        location = (7,3)
        orientation = 'H'
        scrabble_game.score_sum(word,location,orientation)
        self.assertEqual(scrabble_game.current_player.score,42)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.score,0)
        self.assertEqual(scrabble_game.players[3].score,42)

    def test_validate_word_True(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C',3),
            Tile('A',1),
            Tile('S',1),
            Tile('A',1),
            Tile('D',2),
            Tile('F',4),
            Tile('G',2)
        ]
        word = 'CASA'
        location = (1,1)
        orientation = 'H'
        valid_word = scrabble_game.validate_word(word,location,orientation)
        self.assertEqual(valid_word, True)

    def test_validate_word_True_wild_tile(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('T',1),
            Tile('O',1),
            Tile('D',2),
            Tile('?',0),
            Tile('D',2),
            Tile('F',4),
            Tile('G',2)
        ]
        word = 'TODO'
        location = (1,1)
        orientation = 'H'
        valid_word = scrabble_game.validate_word(word,location,orientation)
        self.assertEqual(valid_word, True)

    def test_validate_word_not_emty_True(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('T',3),
            Tile('A',1),
            Tile('R',1),
            Tile('A',1),
            Tile('D',2),
            Tile('F',4),
            Tile('G',2)
        ]
        scrabble_game.board.grid[4][7].add_tile(Tile('A',1))
        scrabble_game.board.grid[5][7].add_tile(Tile('S',1))
        scrabble_game.board.grid[6][7].add_tile(Tile('A',1))
        scrabble_game.board.grid[7][7].add_tile(Tile('D',2))
        scrabble_game.board.grid[8][7].add_tile(Tile('O',1))
        word = 'RATA'
        location = (4,4)
        orientation = 'H'
        valid_word = scrabble_game.validate_word(word,location,orientation)
        self.assertEqual(valid_word, True)
        
    def test_validate_word_False_1(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[1]
        scrabble_game.current_player.tiles = [
            Tile('M',3),
            Tile('E',1),
            Tile('T',1),
            Tile('A',1),
            Tile('G',2),
            Tile('X',8),
            Tile('L',1),
        ]
        word = 'MOTO'
        location = (1,1)
        orientation = 'H'
        valid_word = scrabble_game.validate_word(word,location,orientation)
        self.assertEqual(valid_word, False)

    def test_validate_word_False_2(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.current_player.tiles = [
            Tile('C',3),
            Tile('O',1),
            Tile('S',1),
            Tile('T',1),
            Tile('A',1),
            Tile('Y',4),
            Tile('U',1),
        ]
        word = 'COSTA'
        location = (13,14)
        orientation = 'V'
        valid_word = scrabble_game.validate_word(word,location,orientation)
        self.assertEqual(valid_word, False)
  
    def test_validate_word_False_3(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.current_player.tiles = [
            Tile('C',3),
            Tile('O',1),
            Tile('S',1),
            Tile('T',1),
            Tile('A',1),
            Tile('Y',4),
            Tile('U',1),
        ]
        scrabble_game.board.grid[5][7].add_tile(Tile('F',4))
        scrabble_game.board.grid[6][7].add_tile(Tile('O',1))
        scrabble_game.board.grid[7][7].add_tile(Tile('F',4))
        scrabble_game.board.grid[8][7].add_tile(Tile('O',1))
        word = 'COSTA'
        location = (7,6)
        orientation = 'H'
        valid_word = scrabble_game.validate_word(word,location,orientation)
        self.assertEqual(valid_word, False)
  
    def test_put_word_empty(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C',3),
            Tile('O',1),
            Tile('R',1),
            Tile('C',3),
            Tile('H',4),
            Tile('O',1),
            Tile('C',3),
        ]
        word = 'CORCHO'
        location = (7,3)
        orientation = 'H'
        scrabble_game.put_word(word,location,orientation)
        self.assertEqual(scrabble_game.board.grid[7][3].tile.letter,'C')
        self.assertEqual(scrabble_game.board.grid[7][4].tile.letter,'O')
        self.assertEqual(scrabble_game.board.grid[7][5].tile.letter,'R')
        self.assertEqual(scrabble_game.board.grid[7][6].tile.letter,'C')
        self.assertEqual(scrabble_game.board.grid[7][7].tile.letter,'H')
        self.assertEqual(scrabble_game.board.grid[7][8].tile.letter,'O')

    def test_put_word_not_empty(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[1]
        scrabble_game.current_player.tiles = [
            Tile('A',1),
            Tile('S',1),
            Tile('M',3),
            Tile('L',1),
            Tile('O',1),
            Tile('L',1),
            Tile('O',1)
        ]
        scrabble_game.board.grid[7][5].add_tile(Tile('R',1))
        scrabble_game.board.grid[7][6].add_tile(Tile('A',1))
        scrabble_game.board.grid[7][7].add_tile(Tile('M',3))
        scrabble_game.board.grid[7][8].add_tile(Tile('O',1))
        scrabble_game.board.grid[7][9].add_tile(Tile('S',1))
        word = 'LOMA'
        location = (5,7)
        orientation = 'V'
        scrabble_game.put_word(word,location,orientation)
        self.assertEqual(scrabble_game.board.grid[5][7].tile.letter,'L')
        self.assertEqual(scrabble_game.board.grid[6][7].tile.letter,'O')
        self.assertEqual(scrabble_game.board.grid[7][7].tile.letter,'M')
        self.assertEqual(scrabble_game.board.grid[8][7].tile.letter,'A')
        


if __name__ == '__main__':
    unittest.main()