from game.board import Board
from game.player import Player
from game.models import BagTiles

turn = 1

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player)
    
    def next_turn(self,turn, players):
        if turn != len(players):
            turn += 1
            return turn
        elif turn == len(players):
            turn = 1
            return turn
        

    '''def playing(self):
        return True'''