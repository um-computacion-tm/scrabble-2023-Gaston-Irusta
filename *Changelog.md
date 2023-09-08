# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [Unreleased]
## [0.0.3] - 2023-09-08
## Added
# I changed the function responsable of the manege of the turns, now it works with a variable named current_player
# without a defined value. When the game begings, it's call a method called next_turn to check if that variable is not
# defined to give it the value of the first player of the players' list. Later in mid-game, it's called again to change
# the turn, it reads the current_player and changes it with the following player of the list, if it's the first
# player, it changes it with the second, and if it's the last player of the list, it changes it with the first player
# again. I also made the tests to check if it works correctly.

## [0.0.2] - 2023-09-01
## Added
# In this version I've added a función with a variable to change the playing turns for the players in function of the
# total number of players. The variable begins with the value 1, then when the player finishes its turn, the program
# calls the function "next_turn" and increases the variable's value by 1. When the value is equal to the extension of
# the players' list, instead of adding by 1, the value becomes 1, so it restarts the cycle. I also added the test for
# this funtion.  

## [0.0.1] - 2023-08-28
## Added

# I've created classes for the board, board's cells, players, tiles, tiles' bag, and scrabble. Class Board creates the
# 15x15 standart scrabble board, it creates 15 rows of 15 cells with a multiplier value 1 and with an empy multiplier
# type. Class Cell, for now, depending on the cell's multiplier value and type, it returns the value of the tile which is
# inside the cell, taking the value of the tile and multiplying it by the cell's multiplier. Class Player defines the
# amount of players. Class Tile defines all the letters with their respective value. Class BagTiles groups all the tiles
# and shuffles them to distribute them randomly later. Class Scrabble allows to build the game itself,put the board, the
# tiles' bag and the players in the same place. Also I made the respective tests for all the classes.
