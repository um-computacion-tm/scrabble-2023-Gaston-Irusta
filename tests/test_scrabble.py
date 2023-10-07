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
        self.assertEqual(len(scrabble_game.bag_tiles.tiles),77)

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
        valid_word = scrabble_game.validate_word(word,location,orientation,scrabble_game.current_player.tiles)
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
        valid_word = scrabble_game.validate_word(word,location,orientation,scrabble_game.current_player.tiles)
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
        valid_word = scrabble_game.validate_word(word,location,orientation,scrabble_game.current_player.tiles)
        self.assertEqual(valid_word, False)

    # def test_validate_word_False_2(self):
    #     scrabble_game = ScrabbleGame(players_count= 3)
    #     scrabble_game.current_player = scrabble_game.players[2]
    #     scrabble_game.current_player.tiles = [
    #         Tile('C',3),
    #         Tile('O',1),
    #         Tile('S',1),
    #         Tile('T',1),
    #         Tile('A',1),
    #         Tile('Y',4),
    #         Tile('U',1),
    #     ]
    #     scrabble_game.board.grid[5][7].add_tile(Tile('F',4))
    #     scrabble_game.board.grid[6][7].add_tile(Tile('O',1))
    #     scrabble_game.board.grid[7][7].add_tile(Tile('F',4))
    #     scrabble_game.board.grid[8][7].add_tile(Tile('O',1))
    #     word = 'COSTA'
    #     location = (7,7)
    #     orientation = 'H'
    #     valid_word = scrabble_game.validate_word(word,location,orientation,scrabble_game.current_player.tiles)
    #     self.assertEqual(valid_word, False)

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
        word = 'COSTA'
        location = (13,14)
        orientation = 'V'
        valid_word = scrabble_game.validate_word(word,location,orientation,scrabble_game.current_player.tiles)
        self.assertEqual(valid_word, False)
    
    def test_put_word(self):
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
        scrabble_game.put_word(word,location,orientation,scrabble_game.current_player.tiles)
        print(scrabble_game.board.grid[7][7].tile.letter)
        self.assertEqual(scrabble_game.board.grid[7][7].tile.letter,'H')

if __name__ == '__main__':
    unittest.main()