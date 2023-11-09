import unittest
import random
from unittest.mock import patch
from game.models import (BagTiles,Tile,)

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('C',3)
        self.assertEqual(tile.letter, 'C')
        self.assertEqual(tile.value, 3)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self,patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles),103,)
        self.assertNotEqual(bag.tiles[23].letter,'A')

    def test_get_letter_value(self):
        bag = BagTiles()
        word = 'HOLA'
        word = list(word)
        word_tiles = []
        for i in range(len(word)):
            word_tiles.append(Tile(word[i],bag.get_letter_value(word[i])))
        self.assertEqual(word_tiles[0].value,4)
        self.assertEqual(word_tiles[1].value,1)
        self.assertEqual(word_tiles[2].value,1)
        self.assertEqual(word_tiles[3].value,1)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(8)
        self.assertEqual(len(bag.tiles),95)
        self.assertEqual(len(tiles),8)

    def test_put(self):
        bag = BagTiles()
        tile1 = bag.tiles[0]
        put_tiles = [Tile('Z', 10), Tile('Y', 4)]
        bag.put(put_tiles)
        tile2 = bag.tiles[0]
        self.assertEqual(len(bag.tiles),105)
        self.assertNotEqual(tile1,tile2)

if __name__ == '__main__':
    unittest.main()