from game.models import Tile

class Player:
    def __init__(self, id:int, tiles: list[Tile],nickname = None,score = 0):
        self.id = id
        self.tiles = tiles
        self.nickname = nickname
        self.score = score
    