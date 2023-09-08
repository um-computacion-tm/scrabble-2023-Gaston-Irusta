# from game.cell import Cell

# def calculate_word_value(word: list[Cell]): 
#     value: int = 0
#     multiplier_word = None
#     for cell in word:
#         value = value + cell.calculate_value()
#         if cell.multiplier_type == 'word' and cell.active:
#             multiplier_word = cell.multiplier
#         if multiplier_word:
#             value = value * multiplier_word
#             return value