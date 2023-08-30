class Player:
    def __init__(self,bag_tiles):
        self.tiles = bag_tiles.take(7)
        self.tiles += bag_tiles.take(7 - len(self.tiles))
        