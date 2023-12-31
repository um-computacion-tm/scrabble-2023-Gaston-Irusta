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
        
        for i in range(1, 5):
            self.grid[i][i] = Cell(2, 'word', Tile('', 0))
            self.grid[i + 9][i + 9] = Cell(2, 'word', Tile('', 0))
        
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
        rows = []
        rows.append('                ' + '  0    1    2    3    4    5    6    7    8    9   10   11   12   13   14\n')
        for i in range(15):
            row = ''
            for j in range(15):
                cell = self.grid[i][j]
                if cell.tile.letter != '':
                    row += '| ' + cell.tile.letter + ' |'
                elif cell.multiplier_type == 'word' and cell.multiplier == 2: 
                    row += '|2Pl|'
                elif cell.multiplier_type == 'word' and cell.multiplier == 3: 
                    row += '|3Pl|'
                elif cell.multiplier_type == 'letter' and cell.multiplier == 2:
                    row += '|2Lt|'
                elif cell.multiplier_type == 'letter' and cell.multiplier == 3:
                    row += '|3Lt|'
                else:
                    row += '|  ' + '' + ' |'
            if (i+1) <= 10:
                rows.append('                ' + row + ' ' + str(i))
            else:
                rows.append('                ' + row + '' + str(i))
        print('\n'.join(rows) + '\n')

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

    def verify_n(self,word,n):
        if n == len(word):
            return True
        elif n != len(word):
            return False

    def use_letter_on_board(self, word, location, orientation):
        word_return = list(word)
        for i, letter in enumerate(word):
            if self.location_letter(location, orientation, i) == letter:
                word_return.remove(letter)
        return word_return

    def validate_word_and_letters_play(self,word,location,orientation,player_tiles):
        word = self.use_letter_on_board(word,location,orientation)
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
        return self.verify_n(word,n)

    def location_cell(self,location,orientation,i):
        if orientation == 'H':
            return self.grid[int(location[0])][int(location[1]+i)]
        elif orientation == 'V':
            return self.grid[int(location[0]+i)][int(location[1])]
    
    def location_letter(self,location,orientation,i):
        cell = self.location_cell(location,orientation,i)
        return cell.tile.letter

    def validate_place_board_not_empty(self, word, location, orientation):
        cross = any(self.location_letter(location, orientation, i) != '' for i in range(len(word)))
        return cross

    def validate_word_board_not_empty(self,word,location,orientation):
        list_word = list(word)
        if self.validate_place_board_not_empty(word,location,orientation) == True:
           return self.validate_word(list_word,location,orientation)

        
    def validate_word(self, list_word, location, orientation):
        for i, letter in enumerate(list_word):
            board_letter = self.location_letter(location, orientation=orientation, i=i)
            if board_letter != '' and board_letter != letter:
                print('La palabra que quiere poner no coincide con las letras de las otras palabras del tablero.')
                return False
        return True

    def add_tile_to_cell(self, location, word_tiles, i, orientation):
        cell = self.location_cell(location,orientation,i)
        cell.add_tile(word_tiles[i])

    def add_word_empty_board(self, word_tiles, location, orientation):
        for i in range(len(word_tiles)):
            self.add_tile_to_cell(location,word_tiles,i,orientation='H') if orientation == 'H' else self.add_tile_to_cell(location,word_tiles,i,orientation='V')
        return True
        
    def add_word_not_empty_board(self, word_tiles, location, orientation):
        return self.add_word(word_tiles, location,orientation='H') if orientation == 'H' else self.add_word(word_tiles, location,orientation='V')
    
    def add_word(self, word_tiles, location, orientation):
        for i in range(len(word_tiles)):
            letter = self.location_letter(location, orientation=orientation, i=i)
            if letter == '':
                self.add_tile_to_cell(location, word_tiles, i, orientation)
            elif letter != '' and letter == word_tiles[i].letter:
                pass
            else:
                return False
        return True