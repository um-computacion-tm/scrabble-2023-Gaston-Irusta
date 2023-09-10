from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.cell import Cell


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for index in range(players_count):
            self.players.append(Player(id=index))
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    # def validate_word(self,word: list[Cell],location,orientation):
    #     '''
    #     1- Validar que el usuario tiene esas letras.
    #     2- Validar que la palabra entra en el tablero.
    #     '''
    # def get_words():
    #     '''
    #     Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion,orientacion.
    #     Preguntar al usuario, por cada una de esas opciones, las que considera reales.
    #     '''
    # def put_words():
    #     '''
    #     Modificar el tablero agregando las palabras correctas.
    #     '''