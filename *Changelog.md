# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [Unreleased]
## [0.0.8] - 2023-09-22
## Added
# This time I created a method that checks if the player can really make the word that wants to, and validates if it fits on the board.
# It compares one by one the letters of the word and the player's letters. If the first letter is in the players letter, the method
# removes it form the list of the player's letters and continues comparing with the following letter from the word. Now, if the letter
# is not in the player's letters list, it return False. Then if the player has all the letter correctly, the method cheks if the word
# fits on the board. The tests run correctly.

## [0.0.7] - 2023-09-12
## Added
# I added the file main.py in this version. It will be the responsable of the game to work. It starts the game gretting the players,
# then asks for the amount of player that will play. When the players are already defined, the board and the menu are shown and the
# methos next_turn is called for start playing. Ones the current_player is defined, it's asked the player to choose what will do.
# Depending on the option that choose the player, there will be different instruction to follow. The file isn't finished yet, there
# are some detailes to work on and some mistakes to fix before testing.

## [0.0.6] - 2023-09-11
## Added
# In this upgrade I added a method to validate if the word that the player wants to put on the board not only fits on the board,
# also checks if the player has the tiles to form that word. I made the the test and runs correctly.

## [0.0.5] - 2023-09-10
## Added
# This version adds a method to validate if the word that the player wants to put on the board fits inside of it,
# calculating it from the location of the first letter of the word and the length of it. It takes the coordinates of the
# first letter and adds the length to the coordinate in x or y, depending if the word's orientation is horizontal or
# vertical. If the result is higher than 15, which is the board's length, it returns False that means that the word isn't
# valid, but if the result isn't higher tnah 15, it returns True and means that the word was validated. It works well
# and runs all the tests correctly.

## [0.0.4] - 2023-09-09
## Added
# This version adds the method to calculate the value of the word that the player puts on the board. The method takes
# the word as a list of cells, it uses the cells' atributes: multiplier type, multiplier value, and the tile with its
# value. It works as a repetitive method that takes the tiles's value and adds them to the word value variable one by
# one. It also checks if the word has a letter inside a cell with a word-multiplier, if there's a multiplier, it
# calculates the word value and multiplies it by the word-multiplier, and if there isn't a multiplier, the methos does
# the adds and returns the word value. The method is tested and it works correctly.

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
