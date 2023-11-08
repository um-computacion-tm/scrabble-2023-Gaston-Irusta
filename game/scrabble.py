from game.board import Board
from game.player import Player
from game.models import BagTiles, Tile
from game.tools import Tools
from game.dictionary import Dictionary

class ScrabbleGame:
    def __init__(self, players_count):
        self.dic = Dictionary()
        self.tools = Tools()
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for index in range(players_count):
            self.players.append(Player(index, self.bag_tiles.take(7)))
        self.current_player = None

    def initial_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]

    def next_turn(self):
        if id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    def list_cells(self,word,location,orientation):
        cells = []
        if orientation == 'H':
            for i in range(len(word)):
                cells.append(self.board.grid[location[0]][location[1]+i])
        elif orientation == 'V':
            for i in range(len(word)):
                cells.append(self.board.grid[location[0]+i][location[1]])
        return cells

    def score_sum(self,word,location,orientation):
        cells = self.list_cells(word,location,orientation)
        self.current_player.score = self.current_player.score + self.tools.calculate_word_value(cells)

    def wild_tile_to_end(self):
        tiles = self.current_player.tiles
        n = 0
        for i in range(len(tiles)):
            if tiles[i].letter == '?':
                n += 1
                del tiles[i]
                tiles.append(Tile('?',0))
        self.current_player.tiles = tiles

    def refill_player_tiles(self):
        tiles = self.current_player.tiles
        tiles.extend(self.bag_tiles.take(int(7-(len(self.current_player.tiles)))))
        self.current_player.tiles = tiles

    def validate_word_and_letters_change(self,exchange,player_tiles):
        n = 0
        for j in range(len(exchange)):
            for y in range(len(player_tiles)):
                if exchange[j] == player_tiles[y].letter:
                    n += 1
                    del player_tiles[y]
                    break
        return self.board.verify_n(exchange,n)

    def validate_word(self,word,location,orientation):
        player_tiles = list.copy(self.current_player.tiles)
        word_letters = list(word)
        self.wild_tile_to_end()
        word = self.dic.remove_accents(word)
        answ = True
        if self.dic.verify_word(word) == False:
            print('La palabra no existe.')
            answ = False
        if self.board.validate_word_inside_board(word_letters,location,orientation) == False:
            print('La palabra no entra en el tablero.')
            answ = False
        if self.board.validate_word_and_letters_play(word_letters,location,orientation,player_tiles) == False:
            print('No tienes las letras para formar la plabra.')
            answ = False
        if self.board.is_empty() == False:
            answ = self.board.validate_word_board_not_empty(word_letters,location,orientation) 
        return answ

    def get_word(self):
        word = str(input("¿Qué palabra quiere agregar al tablero?: "))
        word = word.upper()
        num = int(len(word))
        return word, num     
 

    def get_location(self):
        word,num = self.get_word() # type: ignore
        location= []
        while True:
            try:
                location_row = (int(input("¿En qué fila quiere poner la palabra?(0-14): ")))
                location_column = (int(input("¿En qué columna quiere que comience la plabra?(0-14): ")))
                location = [location_row,location_column]
                if location_column is str or location_row is str:
                    raise ValueError
                elif self.board.is_empty() == True:
                    if location[0] > 7 or location[1] > 7:
                        raise ValueError
                    elif location[0] == 7 and location[1] <= 7 and (location[1]+(num)) <= 7 or location[1] == 7 and location[0] <= 7 and (location[0]+(num)) <= 7:
                        raise ValueError
                break
            except ValueError:
                print("Ubicación inválida.")
                location = []
        return word,location

    def get_orientation(self):
        word, location = self.get_location()
        while True:
            try:
                orientation = str(input("¿Qué orientación tendrá la palabra? (H/V): "))
                orientation = orientation.upper()
                if orientation != 'H' and orientation != 'V':
                    print('Debe escribir solo la letra H o V.')
                elif self.board.is_empty() == True:
                    if location[0] == 7 or location[1] == 7:
                        break
                    elif location[0] == 7 and orientation != 'H' or location[1] == 7 and orientation != 'V':
                        raise ValueError
                    else:
                        break
                else:
                    break
            except ValueError:
                print('Recuerde pase por el centro...')
        return word,location,orientation

    def put_word(self,word,location,orientation):
        word = list(word)
        word_tiles = []
        self.wild_tile_to_end()
        for i in range(len(word)):
            for x in range(len(self.current_player.tiles)):
                if word[i] == self.current_player.tiles[x].letter:
                    word_tiles.append(self.current_player.tiles[x])
                    del self.current_player.tiles[x]
                    break
                elif self.current_player.tiles[x].letter == '?':
                    self.current_player.tiles[x].value = self.bag_tiles.get_letter_value(word[i])
                    self.current_player.tiles[x].letter = word[i]
                    word_tiles.append(self.current_player.tiles[x])
                    break
        if self.board.is_empty() == True:
            self.board.add_word_empty_board(word_tiles,location,orientation)
        elif self.board.is_empty() == False:
            self.board.add_word_not_empty_board(word_tiles,location,orientation)