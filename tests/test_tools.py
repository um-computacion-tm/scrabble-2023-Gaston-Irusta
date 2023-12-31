import unittest
from game.cell import Cell
from game.models import Tile
from game.tools import Tools
from game.board import Board
class TestCalculateWordValue(unittest.TestCase):
    

    
    def test_calculate_word_value(self):
        tools = Tools()
        word=[
            Cell(tile=Tile('C', 3), 
                multiplier = 2, 
                multiplier_type = 'letter'),
            Cell(tile=Tile('A', 1),
                 multiplier=1,
                 multiplier_type=''
                 ),
            Cell(tile=Tile('S', 1),
                 multiplier= 1,
                 multiplier_type=''
                 ),
            Cell(tile=Tile('A', 1),
                 multiplier=1,
                 multiplier_type=''
                 )
         ]
        value = tools.calculate_word_value(word)
        self.assertEqual(value,9)

    def test_with_word_multiplier(self):
        tools = Tools()
        word =[
            Cell(tile=Tile('C', 3), 
                 multiplier = 2, 
                 multiplier_type = 'word'),
            Cell(tile=Tile('A', 1),
                 multiplier= 1,
                   multiplier_type= ''
                   ),
            Cell(tile=Tile('S', 1),
                 multiplier= 1,
                 multiplier_type= ''
                 ),
            Cell(tile=Tile('A', 1),
                 multiplier= 1,
                 multiplier_type=''
                 ),
        ]
        for index in range(len(word)):
            word[index].active = False

        value = tools.calculate_word_value(word)
        self.assertEqual(value,12)

    def test_with_letter_word_multiplier(self):
        tools = Tools()
        word =[
            Cell(tile=Tile('C', 3), 
                 multiplier = 2, 
                 multiplier_type = 'letter'),
            Cell(tile=Tile('A', 1),
                 multiplier=1,
                 multiplier_type=''
                 ),
            Cell(tile=Tile('S', 1),
                 multiplier=1,
                 multiplier_type=''
                 ),
            Cell(tile=Tile('A', 1),
                 multiplier = 2,
                 multiplier_type = 'word'
                 ),

        ]
        value = tools.calculate_word_value(word)
        self.assertEqual(value,18)


if __name__ == '__main__':
    unittest.main()