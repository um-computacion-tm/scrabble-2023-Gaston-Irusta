from game.cell import Cell
from game.models import Tile

class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '',Tile('',0)) for _ in range(15) ]for _ in range(15)]
        # Multiplier x3 word
        c = 0
        for _ in range(3):
            self.grid[0][c] = Cell(3,'word',Tile('',0))
            self.grid[14][c] = Cell(3,'word',Tile('',0))
            c += 7
        self.grid[7][0] = Cell(3,'word',Tile('',0))
        self.grid[7][14] = Cell(3,'word',Tile('',0))
        # Multiplier x2 word
        for i in range(1,5):
            self.grid[i][i] = Cell(2,'word',Tile('',0))
        self.grid[7][7] = Cell(2,'word',Tile('',0))
        for i in range(10,14):
            self.grid[i][i] = Cell(2,'word',Tile('',0))
        r = 13
        c = 1
        for _ in range(4):
            self.grid[r][c] = Cell(2,'word',Tile('',0))
            r -= 1
            c += 1
        r = 4
        c = 10
        for _ in range(4):
            self.grid[r][c] = Cell(2,'word',Tile('',0))
            r -= 1
            c += 1
        # Multiplier x3 letter
        c = 5
        for _ in range(2):
            self.grid[1][c] = Cell(3,'letter',Tile('',0))
            self.grid[13][c] = Cell(3,'letter',Tile('',0))
            c += 4
        c = 1
        for _ in range(4):
            self.grid[5][c] = Cell(3,'letter',Tile('',0))
            self.grid[9][c] = Cell(3,'letter',Tile('',0))
            c += 4
        # Multiplier x2 letter
        c = 3
        for _ in range(2):
            self.grid[0][c] = Cell(2,'letter',Tile('',0))
            self.grid[7][c] = Cell(2,'letter',Tile('',0))
            self.grid[14][c] = Cell(2,'letter',Tile('',0))
            c += 8
        c = 6
        for _ in range(2):
            self.grid[2][c] = Cell(2,'letter',Tile('',0))
            self.grid[12][c] = Cell(2,'letter',Tile('',0))
            c += 2
        c = 0
        for _ in range(3):
            self.grid[3][c] = Cell(2,'letter',Tile('',0))
            self.grid[11][c] = Cell(2,'letter',Tile('',0))
            c += 7
        c1 = 2
        c2 = 8
        for _ in range(2):
            self.grid[6][c1] = Cell(2,'letter',Tile('',0))
            self.grid[8][c1] = Cell(2,'letter',Tile('',0))
            self.grid[6][c2] = Cell(2,'letter',Tile('',0))
            self.grid[8][c2] = Cell(2,'letter',Tile('',0))
            c1 += 4
            c2 += 4
    
    def print_board(self):
        boardRow = ''
        print ('                    ' , ' 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15\n')
        for i in range(15):
            for j in range(15):
                if self.grid[i][j].tile.letter != '':
                    boardRow += '[ ' + self.grid[i][j].tile.letter + ' ]'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 2: 
                    boardRow += '[2P]'
                elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 3: 
                    boardRow += '[3P]'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 2:
                    boardRow += '[2L]'
                elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 3:
                    boardRow += '[3L]'
                else:
                    boardRow += '[ ' + self.grid[i][j].tile.letter + ' ]'
            if (i+1) <= 9:
                print ('                ',str(i+1),' ',boardRow)
            else:
                print ('               ',str(i+1),' ',boardRow)
            boardRow = ''
        print('\n')


    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        valid = False
        if orientation == "V" and location[0] + len_word <= 15 and location[1] + len_word > 1:
            valid = True
        elif orientation == "H" and location[0] + len_word > 1 and location[1] + len_word <= 15:
            valid = True
        return valid
    
    def is_empty(self):
        if self.grid[7][7].tile.value == 0:
            return True
        else:
            return False
    
    def validate_word_board_not_empty(self,word,location,orientation):
        word = list(word)
        if orientation == 'H':
            for i in range(len(word)):
                if self.grid[int(location[0])][int(location[1]+i)].tile.letter == '':
                    pass
                elif self.grid[int(location[0])][int(location[1]+i)].tile.letter != '':
                    if self.grid[int(location[0])][int(location[1]+i)].tile.letter == word[i]:
                        pass
                    else:
                        print('La palabra que quiere poner no coincide con las letras de las otras palabras del tablero.')
                        return False
            return True
        elif orientation == 'V':
            for i in range(len(word)):
                if self.grid[int(location[0]+i)][int(location[1])].tile.letter == '':
                    pass
                elif self.grid[int(location[0]+i)][int(location[1])].tile.letter != '':
                    if self.grid[int(location[0]+i)][int(location[1])].tile.letter == word[i]:
                        pass
                    else:
                        print('La palabra que quiere poner no coincide con las letras de las otras palabras del tablero.')
                        return False
            return True

    def add_word_empty_board(self,word_tiles,location,orientation):
        if orientation == 'H':
            for i in range(len(word_tiles)):
                self.grid[int(location[0])][int(location[1]+i)].add_tile(word_tiles[i])
            return True
        elif orientation == 'V':
            for i in range(len(word_tiles)):
                self.grid[int(location[0]+i)][int(location[1])].add_tile(word_tiles)
            return True
    def add_word_not_empty_board(self,word_tiles,location,orientation):
        if orientation == 'H':
            for i in range(len(word_tiles)):
                if self.grid[int(location[0])][int(location[1]+i)].tile.letter == '':
                    self.grid[int(location[0])][int(location[1]+i)].add_tile(word_tiles[i])
                elif self.grid[int(location[0])][int(location[1]+i)].tile.letter != '':
                    if self.grid[int(location[0])][int(location[1]+i)].tile.letter == word_tiles[i].letter:
                        pass
                    else:
                        return False
            return True
        elif orientation == 'V':
            for i in range(len(word_tiles)):
                if self.grid[int(location[0]+i)][int(location[1])].tile.letter == '':
                    self.grid[int(location[0]+i)][int(location[1])].add_tile(word_tiles[i])
                elif self.grid[int(location[0]+i)][int(location[1])].tile.letter != '':
                    if self.grid[int(location[0]+i)][int(location[1])].tile.letter == word_tiles[i].letter:
                        pass
                    else:
                        return False
            return True