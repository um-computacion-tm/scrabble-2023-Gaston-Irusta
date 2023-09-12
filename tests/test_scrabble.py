import unittest
from game.scrabble import ScrabbleGame

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

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = None
        scrabble_game.next_turn()
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
        scrabble_game.current_player.tiles = ['C','A','S','A']
        word = 'casa'
        location = (1,1)
        orientation = 'H'
        player_tiles = scrabble_game.current_player.tiles
        valid_word = scrabble_game.validate_word(word,location,orientation,player_tiles)
        self.assertEqual(valid_word, True)

    def test_validate_word_False_1(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[1]
        scrabble_game.current_player.tiles = ['M','O','T','O']
        word = 'roca'
        location = (1,1)
        orientation = 'H'
        player_tiles = scrabble_game.current_player.tiles
        valid_word = scrabble_game.validate_word(word,location,orientation,player_tiles)
        self.assertEqual(valid_word, False)

    def test_validate_word_False_2(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.current_player.tiles = ['C','O','S','T','A']
        word = 'Costa'
        location = (14,15)
        orientation = 'V'
        player_tiles = scrabble_game.current_player.tiles
        valid_word = scrabble_game.validate_word(word,location,orientation,player_tiles)
        self.assertEqual(valid_word, False)
if __name__ == '__main__':
    unittest.main()