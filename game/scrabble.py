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
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    def validate_word(self,word,location,orientation,player_tiles):
            word = word.upper()
            letters = list(word)
            valid = True
            for i in range(len(letters)):
                if letters[i] not in player_tiles:
                    return False
            if valid == True:
                valid = self.board.validate_word_inside_board(word,location,orientation)
                if valid == True:
                    return True
                else:
                    return False
                
    # def get_words():
    #     '''
    #     Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion,orientacion.
    #     Preguntar al usuario, por cada una de esas opciones, las que considera reales.
    #     '''
    # def put_words():
    #     '''
    #     Modificar el tablero agregando las palabras correctas.
    #     '''