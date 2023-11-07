import unittest
from unittest.mock import patch
from game.main import Main
from game.scrabble import ScrabbleGame

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value=2)
    def test_get_player_count(self, mock_input):
        main = Main()
        num = main.get_player_count()
        self.assertEqual(num, 2)

    # @patch('builtins_input',side_effect=['gg','ff'])
    # def test_player_nickname(self,mock_nickname):
    #     main = Main()
    #     main.game = ScrabbleGame(2)
    #     main.players_nicknames()
    #     self.assertEqual(main.game.players[0].nickname,'gg')
    #     self.assertEqual(main.game.players[1].nickname,'ff')

    # @patch('game.main.Main.get_player_count',return_value=2)
    # @patch('game.main.Main.players_nicknames', side_effect=['Player1', 'Player2'])
    # @patch('game.main.Main.main_menu',return_value=4)
    # def test_players_nicknames(self, mock_count, mock_nicknames, mock_opcion):
    #     Main()
    #     Main().players_nicknames()
    #     self.assertEqual(Main().game.players[0].nickname, 'Player1')
    #     self.assertEqual(Main().game.players[1].nickname, 'Player2')



if __name__ == '__main__':
    unittest.main()