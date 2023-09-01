import unittest
from game.scrabble import ScrabbleGame
from game.scrabble import turn

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count= 3)
        game_turn = turn
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),3,)
        self.assertIsNotNone(scrabble_game.bag_tiles)
        self.assertEqual(game_turn,1)
        game_turn = scrabble_game.next_turn(game_turn,scrabble_game.players)
        self.assertEqual(game_turn, 2)
        game_turn = 3
        game_turn = scrabble_game.next_turn(game_turn,scrabble_game.players)
        self.assertEqual(game_turn, 1)


if __name__ == '__main__':
    unittest.main()