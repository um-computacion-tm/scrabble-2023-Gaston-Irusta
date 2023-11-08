import unittest
from unittest.mock import patch
from game.main import Main
from game.models import Tile
from game.scrabble import ScrabbleGame

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value=2)
    def test_get_player_count(self, mock_input):
        main = Main()
        num = main.get_player_count()
        self.assertEqual(num, 2)

    def test_play_when_board_is_empty(self):
        with patch('builtins.input', side_effect=[2,'','',1,'pato',7,7,'H',4]):
            with patch('builtins.print'):
                main = Main()
                main.game.players[0].tiles = [
                    Tile('P', 1),
                    Tile('A', 1),
                    Tile('T', 1),
                    Tile('O', 1),
                    Tile('C', 1),
                    Tile('E', 1),
                    Tile('G', 1),
                ]
                main.main_menu()
                self.assertEqual(main.game.board.grid[7][7].tile.letter, 'P')
    
    def test_change_tiles(self):
        with patch('builtins.input', side_effect=[2,'','',2,'t','si','a','no',2,'r','no',4]):
            with patch('builtins.print'):
                main = Main()
                main.game.players[0].tiles = [
                    Tile('P', 1),
                    Tile('A', 1),
                    Tile('T', 1),
                    Tile('O', 1),
                    Tile('C', 1),
                    Tile('E', 1),
                    Tile('G', 1),
                ]
                main.game.players[1].tiles = [
                    Tile('R', 1),
                    Tile('?', 0),
                    Tile('T', 1),
                    Tile('A', 1),
                    Tile('S', 1),
                    Tile('E', 1),
                    Tile('G', 1),
                ]
                main.main_menu()
                self.assertNotEqual(main.game.players[0].tiles[2].letter, 'T')
                self.assertNotEqual(main.game.players[0].tiles[1].letter, 'A')
                self.assertNotEqual(main.game.players[1].tiles[0].letter, 'R')

    def test_pass_turn(self):
        with patch('builtins.input', side_effect=[2,'Player1','Player2',3,3,4]):
            with patch('builtins.print'):
                main = Main()
                main.main_menu()
                self.assertEqual(main.game.current_player.nickname, 'Player1')


if __name__ == '__main__':
    unittest.main()