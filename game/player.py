
from game.models import Tile
class Player:
    def __init__(self, id:int, tiles: list[Tile]):
        self.id = id
        self.tiles = tiles
        