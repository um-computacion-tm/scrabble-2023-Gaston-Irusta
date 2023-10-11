import unittest
from game.cell import Cell
from game.models import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(2, 'letter')
        self.assertEqual(cell.multiplier,2,)
        self.assertEqual(cell.multiplier_type,'letter',)
        self.assertIsNone(cell.tile)
        self.assertEqual(cell.calculate_value(),0,)

    def test_add_tile(self):
        cell = Cell(1, '')
        tile = Tile('P', 3)
        cell.add_tile(tile=tile)
        self.assertEqual(cell.tile, tile)

    def test_remove_tile(self):
        cell = Cell(1,'',Tile('A',1))
        cell.remove_tile()
        self.assertEqual(cell.tile.letter,'')
        self.assertEqual(cell.tile.value,0)

    def test_cell_value(self):
        cell = Cell(2, 'letter')
        tile = Tile('LL', 8)
        cell.add_tile(tile=tile)
        self.assertEqual(cell.calculate_value(),16,)

    def test_cell_multiplier_word(self):
        cell = Cell(2, 'word')
        tile = Tile('Q', 5)
        cell.add_tile(tile=tile)
        self.assertEqual(cell.calculate_value(),5,)

if __name__ == '__main__':
    unittest.main()
