from game.cell import Cell
from game.models import Tile

class Board:
    def __init__(self):
        self.grid = [[ Cell(1,'',Tile('',0)) for _ in range(15) ]for _ in range(15)]
        
        c = 0
        for _ in range(3):
            self.grid[0][c] = Cell(3,'word',Tile('',0))
            self.grid[14][c] = Cell(3,'word',Tile('',0))
            self.grid[3][c] = Cell(2,'letter',Tile('',0))
            self.grid[11][c] = Cell(2,'letter',Tile('',0))
            c += 7
        
        self.grid[7][0] = Cell(3,'word',Tile('',0))
        self.grid[7][7] = Cell(2,'word',Tile('',0))
        self.grid[7][14] = Cell(3,'word',Tile('',0))
        
        for i in range(1,5):
            self.grid[i][i] = Cell(2,'word',Tile('',0))

        for i in range(10,14):
            self.grid[i][i] = Cell(2,'word',Tile('',0))
        
        r1 = 13
        c1 = 1
        r2 = 4
        c2 = 10
        c3 = 1
        for _ in range(4):
            self.grid[r1][c1] = Cell(2,'word',Tile('',0))
            r1 -= 1
            c1 += 1
            self.grid[r2][c2] = Cell(2,'word',Tile('',0))
            r2 -= 1
            c2 += 1
            self.grid[5][c3] = Cell(3,'letter',Tile('',0))
            self.grid[9][c3] = Cell(3,'letter',Tile('',0))
            c3 += 4

        c1 = 2
        c2 = 5
        c3 = 8
        c4 = 3
        c5 = 6
        for _ in range(2):
            self.grid[6][c1] = Cell(2,'letter',Tile('',0))
            self.grid[8][c1] = Cell(2,'letter',Tile('',0))
            self.grid[1][c2] = Cell(3,'letter',Tile('',0))
            self.grid[13][c2] = Cell(3,'letter',Tile('',0))
            self.grid[6][c3] = Cell(2,'letter',Tile('',0))
            self.grid[8][c3] = Cell(2,'letter',Tile('',0))
            self.grid[0][c4] = Cell(2,'letter',Tile('',0))
            self.grid[7][c4] = Cell(2,'letter',Tile('',0))
            self.grid[14][c4] = Cell(2,'letter',Tile('',0))
            self.grid[2][c5] = Cell(2,'letter',Tile('',0))
            self.grid[12][c5] = Cell(2,'letter',Tile('',0))
            c1 += 4
            c2 += 4
            c3 += 4
            c4 += 8
            c5 += 2

    def print_board(self):
        boardRow = ''
        print ('                    ' , ' 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14\n')
        for i in range(15):
            for j in range(15):
                if self.grid[i][j].tile.letter != '':
                    boardRow += '[ ' + self.grid[i][j].tile.letter + ']'
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
            if (i+1) <= 10:
                print ('                ',str(i),' ',boardRow)
            else:
                print ('               ',str(i),' ',boardRow)
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
        if self.grid[7][7].tile.letter == '':
            return True
        else:
            return False

    def validate_word_and_letters(self,word,player_tiles):
        n = 0
        for i in range(len(word)):
            for x in range(len(player_tiles)):
                if word[i] == player_tiles[x].letter:
                    n += 1
                    del player_tiles[x]
                    break
                elif player_tiles[x].letter == '?':
                    n += 1
                    del player_tiles[x]
                    break
        if n == len(word):
            return True
        elif n != len(word):
            return False
    
    def validate_word_and_letters_change(self,word,player_tiles):
        n = 0
        for i in range(len(word)):
            for x in range(len(player_tiles)):
                if word[i] == player_tiles[x].letter:
                    n += 1
                    del player_tiles[x]
                    break
        if n == len(word):
            return True
        elif n != len(word):
            return False
        
    def validate_place_board_not_empty(self,word,location,orientation):
        cross = None
        if orientation == 'H':
            for i in range(len(word)):
                if self.grid[int(location[0])][int(location[1]+i)].tile.letter != '':
                    cross = True
        elif orientation == 'V':
            for i in range(len(word)):
                if self.grid[int(location[0]+i)][int(location[1])].tile.letter != '':
                    cross = True    
        return cross

    def validate_word_board_not_empty(self,word,location,orientation):
        list_word = list(word)
        if self.validate_place_board_not_empty(word,location,orientation) == True:
            if orientation == 'H':
                return self.validate_word_horizontal(list_word,location)
            elif orientation == 'V':
                return self.validate_word_vertical(list_word,location)
        
    def validate_word_horizontal(self,list_word,location):
        for i in range(len(list_word)):
            if self.grid[int(location[0])][int(location[1]+i)].tile.letter == '':
                pass
            elif self.grid[int(location[0])][int(location[1]+i)].tile.letter == list_word[i]:
                pass
            elif self.grid[int(location[0])][int(location[1]+i)].tile.letter != list_word[i]:
                print('La palabra que quiere poner no coincide con las letras de las otras palabras del tablero.')
                return False
        return True
        
    def validate_word_vertical(self,list_word,location):
        for i in range(len(list_word)):
            if self.grid[int(location[0]+i)][int(location[1])].tile.letter == '':
                pass
            elif self.grid[int(location[0]+i)][int(location[1])].tile.letter == list_word[i]:
                pass
            elif self.grid[int(location[0]+i)][int(location[1])].tile.letter != list_word[i]:
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
                self.grid[int(location[0]+i)][int(location[1])].add_tile(word_tiles[i])
            return True
        
    def add_word_not_empty_board(self,word_tiles,location,orientation):
        if orientation == 'H':
            return self.add_word_horizontal(word_tiles,location)
        elif orientation == 'V':
            return self.add_word_vertical(word_tiles,location)
    
    def add_word_horizontal(self,word_tiles,location):
        for i in range(len(word_tiles)):
            if self.grid[int(location[0])][int(location[1]+i)].tile.letter == '':
                self.grid[int(location[0])][int(location[1]+i)].add_tile(word_tiles[i])
            elif self.grid[int(location[0])][int(location[1]+i)].tile.letter != '' and self.grid[int(location[0])][int(location[1]+i)].tile.letter == word_tiles[i].letter:
                pass
            else:
                return False
        return True

    def add_word_vertical(self,word_tiles,location):
        for i in range(len(word_tiles)):
            if self.grid[int(location[0]+i)][int(location[1])].tile.letter == '':
                self.grid[int(location[0]+i)][int(location[1])].add_tile(word_tiles[i])
            elif self.grid[int(location[0]+i)][int(location[1])].tile.letter != '' and self.grid[int(location[0]+i)][int(location[1])].tile.letter == word_tiles[i].letter:
                pass
            else:
                return False
        return True