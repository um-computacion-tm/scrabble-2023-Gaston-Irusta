from game.models import Tile
from calculate_word_value import calculate_word_value

class Player:
    def __init__(self, id:int, tiles: list[Tile],nickname = None,score = 0):
        self.id = id
        self.tiles = tiles
        self.nickname = nickname
        self.score = score
    
    def upgrd_score(self,word_tiles):
        self.score = (self.score + calculate_word_value(word_tiles))