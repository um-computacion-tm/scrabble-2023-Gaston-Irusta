import unittest
from game.models import (BagTiles,Tile,)
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('C',3)
        self.assertEqual(tile.letter, 'C')
        self.assertEqual(tile.value, 3)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles),98,)
        self.assertEqual(patch_shuffle.call_count,1,)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.tiles,)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(8)
        self.assertEqual(len(bag.tiles),90,)
        self.assertEqual(len(tiles),8,)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 10), Tile('Y', 4)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles),100,)

if __name__ == '__main__':
    unittest.main()