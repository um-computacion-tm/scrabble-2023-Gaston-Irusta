from game.models import Tile
class Cell:
    def __init__(self,multiplier,multiplier_type,tile=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.tile = tile
        self.active = True

    def add_tile(self, tile:Tile):
        self.tile = tile

    def remove_tile(self):
        self.tile = Tile('',0)

    def calculate_value(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.tile.value * self.multiplier
        else:
            return self.tile.value
