from game.board import Board
from game.player import Player
from game.models import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for index in range(players_count):
            self.players.append(Player(index, self.bag_tiles.take(7)))
            self.players[index].nickname = str(input(f'Ingrese su apodo: '))
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    def validate_word(self,word,location,orientation,player_tiles):
        # Hacer lista con letras de palabra y del jugador y comoararlas una por una y si coinciden sacarla de la lista y seguir con la siguiente.
        valid = True
        for i in range(len(word)):
            for x in range(len(player_tiles)):
                if word[i].letter == player_tiles[x].letter:
                    del player_tiles[x]
                    break
                else:
                    return False
        valid = self.board.validate_word_inside_board(word,location,orientation)
        return valid

    # def put_words(self,word,player_tiles,location,orientation):
