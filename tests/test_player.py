import unittest
from game.player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(0)
        player_2 = Player(0)
        player_3 = Player(0)
        self.assertEqual(player_1.tiles,0,)
        self.assertEqual(player_2.tiles,0,)
        self.assertEqual(player_3.tiles,0,)

if __name__ == '__main__':
    unittest.main()
