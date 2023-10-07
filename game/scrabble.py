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

    def initial_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]

    def next_turn(self):
        if id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    def validate_word(self,word,location,orientation,player_tiles):
        word = list(word)
        n = 0
        for i in range(len(word)):
            for x in range(len(player_tiles)):
                if word[i] == player_tiles[x].letter:
                    n += 1
                    del player_tiles[x]
                    break
        if n != len(word):
            return False
        if self.board.validate_word_inside_board(word,location,orientation) == True:
            if self.board.is_empty == False:
                if self.board.validate_word_board_not_empty(word,location,orientation) == True:
                    return True
                else:
                    return False
            return True
        else:
            return False

    def put_word(self,word,location,orientation,player_tiles):
        word = list(word)
        word_tiles = []
        for i in range(len(word)):
            for x in range(len(player_tiles)):
                if word[i] == player_tiles[x].letter:
                    word_tiles.append(player_tiles[x])
                    break
        if self.board.is_empty() == True:
            self.board.add_word_empty_board(word_tiles,location,orientation)
        elif self.board.is_empty() == False:
            self.board.add_word_not_empty_board(word_tiles,location,orientation)