import unittest
from game.player import Player
from game.models import BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        bag_tiles = BagTiles()
        player_1 = Player(1,bag_tiles.take(7))
        player_2 = Player(2,bag_tiles.take(7))
        player_3 = Player(3,bag_tiles.take(7))
        self.assertEqual(player_1.id,1)
        self.assertEqual(len(player_1.tiles),7)
        self.assertEqual(player_2.id,2)
        self.assertEqual(len(player_2.tiles),7)
        self.assertEqual(player_3.id,3)
        self.assertEqual(len(player_3.tiles),7)

if __name__ == '__main__':
    unittest.main()
