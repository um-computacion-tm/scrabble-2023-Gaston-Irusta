# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [Unreleased]
## [0.0.1] - 2023-08-28
### Added

# I've created classes for the board, board's cells, players, tiles, tiles' bag, and scrabble. Class Board creates the
# 15x15 standart scrabble board, it creates 15 rows of 15 cells with a multiplier value 1 and with an empy multiplier
# type. Class Cell, for now, depending on the cell's multiplier value and type, it returns the value of the tile which is
# inside the cell, taking the value of the tile and multiplying it by the cell's multiplier. Class Player defines the
# amount of players. Class Tile defines all the letters with their respective value. Class BagTiles groups all the tiles
# and shuffles them to distribute them randomly later. Class Scrabble allows to build the game itself,put the board, the
# tiles' bag and the players in the same place. Also I made the respective tests for all the classes.
