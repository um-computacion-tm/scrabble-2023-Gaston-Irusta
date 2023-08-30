import unittest
from game.cell import Cell
from game.models import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(2, 'letter')

        self.assertEqual(cell.multiplier,2,)
        self.assertEqual(cell.multiplier_type,'letter',)
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0,)

    def test_add_letter(self):
        cell = Cell(1, '')
        letter = Tile('P', 3)
        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(2, 'letter')
        letter = Tile('LL', 8)
        cell.add_letter(letter=letter)

        self.assertEqual(cell.calculate_value(),16,)

    def test_cell_multiplier_word(self):
        cell = Cell(2, 'word')
        letter = Tile('Q', 5)
        cell.add_letter(letter=letter)

        self.assertEqual(cell.calculate_value(),5,)

if __name__ == '__main__':
    unittest.main()
