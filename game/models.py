import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A',1),
            Tile('B',3),
            Tile('c',3),
            Tile('CH',5),
            Tile('D',2),
            Tile('E',1),
            Tile('F',4),
            Tile('G',2),
            Tile('H',4),
            Tile('I',1),
            Tile('J',8),
            Tile('L',1),
            Tile('LL',8),
            Tile('M',3),
            Tile('N',1),
            Tile('Ñ',8),
            Tile('O',1),
            Tile('P',3),
            Tile('Q',5),
            Tile('R',1),
            Tile('RR',8),
            Tile('S',1),
            Tile('T',1),
            Tile('U',1),
            Tile('V',4),
            Tile('X',8),
            Tile('Y',4),
            Tile('Z',10)
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)