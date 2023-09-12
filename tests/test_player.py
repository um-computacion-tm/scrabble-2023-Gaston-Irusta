import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(1,7)
        player_2 = Player(2,7)
        player_3 = Player(3,7)
        self.assertEqual(player_1.id,1)
        self.assertEqual(player_1.tiles,7)
        self.assertEqual(player_2.id,2)
        self.assertEqual(player_2.tiles,7)
        self.assertEqual(player_3.id,3)
        self.assertEqual(player_3.tiles,7)

if __name__ == '__main__':
    unittest.main()
