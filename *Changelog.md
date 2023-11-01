# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [Unreleased]
## [0.2.7] - 2023-11-01
## Added
# I added a method to verify which letters are on the board so that the player is not asked for them when putting a word on the board.
# Based on the word and location, it searches the board with that data for letters that match the letters in the word. If some letters
# match, it removes them from the list of letters it asks the player, but if none of them match, it returns the same list and asks the
# player to have all the letters. The method is tested and works.

## [0.2.6] - 2023-10-31
## Added
# Added dictionary to check if the word the player wants to use exists. The method works with a local .txt file, looks for the word in
# the file and returns True or False depending on whether it is in the file or not. I tested it and works correctly.

## [0.2.5] - 2023-10-25
## Added
# I've fixed somo problems with the inputs, if it ask for an int and the player puts a str, or int in a str input. The game doesn't
# crash. Fixed the problem with the option change tiles and the wild tiles, now if the player puts a wrong letter, the game doesn't
# change the wild tile, it warns that the player doesn't have the tiles.

## [0.2.4] - 2023-10-24
## Added
# I created the methods to the option change tiles in the main menu. The method asks the player to write the letter that wants to
# change, then asks if the player wants to changer another tile, if the answer is yes, the method adds a tile to the list of letters
# to change and asks again, but if the answer is no, the method continius with the validate and get tile. It validates if the player
# has the tiles to change or not. Then takes the player's tiles and puts them into the bag tiles and takes others randomly to complete
# the number of seven tiles to play. 

## [0.2.3] - 2023-10-23
## Added
# I've added the tests to check if the game can put a word on the board when the player has wild tiles. I created methods to refill
# the player's tiles and validate if the player's word crosses with another word placed on the board. The method to refill is used when
# the player's turn ends and the player doesn't have 7 tiles. It also will be used in the option change tiles from the main menu. And
# the method to validate the words that cross eachother will avoid that the player places a word in a random location. I made tests for
# these methods and they word well.

## [0.2.2] - 2023-10-22
## Added
# I've fixed some minor bugs. Added methods to get the value of a tile and move the wild tile to the player's end tile list. The first
# method will be applied when the player uses a wild tile, it will search for the tile value with a letter form the word the player
# wants to put on the board, then the wild tile will have the correct letter and value. The second method takes the wild tile from the
# player's list of tiles and moves it to the end. It removes it and adds it back to the end of the list. Also, I tested to see if they
# work correctly, and they do. Additionally, I have improved the Main class to make testing easier.

## [0.2.1] - 2023-10-21
## Added
# The complex issue was fixed and now I've made a class main to make ir easier to test with the methods of the class. I also add the
# score_sum to the main so it can show the score of the current player.

## [0.2.0] - 2023-10-20
## Added
# In the next versions I'll be trying to fix the complex level issue, I had like 31 problems so I'm trying to fix then as soon as
# posible.

## [0.1.9] - 2023-10-10
## Addedm
# Today I worked in the option "Play" of the main menu. I make ir "work" well, I have just an issue with the part that adds the tile
# to the board because the method validates is modifying the list of tiles of the current player before the method put word can be
# called. I'll try to fix it to the following version, and the make the tests with patch.(I don't remerber very well how the patch
# works, so I will do the tests later, sorry).

## [0.1.8] - 2023-10-09
## Added
# Today I've done the methos to upload the score of every player so I can use it when the player's turn ends. I had to make a method
# in the class ScrabbleGame to build a list of the cells whith the tiles that forms the word so the game can calculate the word value.
# Now with that list of cells, the game can execute the method calculate_word_value and update the score of the player that had just
# finisshed its turn. I made tests to verify if the method that lists the cells and the method to update the score works correctly,
# and furtunately they do.

## [0.1.7] - 2023-10-07
## Added
# In this version I finished the method put word and finally fix the validate word, I made tests to check if all the posible variables
# are tested, with the method validate word and the two posible cases for the method put word. In the following version I'll be adding
# the score for each player in the game, I have to adapt the calculate word value to work well.

## [0.1.6] - 2023-10-06
## Added
# Today I made the methot to put a word, I've made one test and works correctly and some to tests the method to validate the words, 
# which I changed a little bit and now there is one test that it's not working. I'll do some more tests for the method to validate and
# put words. It's not done yet but tomorrow it will be finished.

## [0.1.5] - 2023-10-04
## Added
# - Split methods to validate and add words on the board.
# - Changes in methods to validate words when the player does an input with a word as a string.
# - Tests for the new methods.

## [0.1.4] - 2023-09-30
## Added
# Today I've finished the option 4, which is for surrender in the game. When the player wants to surrender, the game prints a messege
# that says the player has surrendered and how many players are remaining. I had to make the game check the number of players that
# are playing and based in that number decide the instruction that will execute. It has to delete the player that surrendered and
# update the players' ids so the index of the players list fits with the ids, and the game doesn't fail. Also, I slpit the method
# next_turn in two different methods, initial_turn and next_turn. 

## [0.1.3] - 2023-09-27
## Added
# In this version I reorganized the code in the main file, so it shows the wellcome messege and defines the players onece, and the
# starts the bucle where the main menu is shown, so the players can play contantly untill one of them lose, or win, or surrender.
# I added an atribute to the class player to know well who is the player 1,2,3 and 4, so when the game starts and the number of players
# is defined, the game asks for the nicknames of the players, so while they are playing, the game calls them by their nicknames so they
# don't get confused. Also I made the main able to show the tiles of the current player. I have to add the functions to put a word and
# exchange tiles with the bag tiles in the next version.

## [0.1.2] - 2023-09-26
## Added
# I created a method to print the board with the multiplier of its cells, and implemented in the main. The main.py file was changed
# a bit, changed the welcome messege, the disposition of the information, and the options to play. I'll try to make it to show the
# letters of the current player before it shows the options to play. That may be added in the next version. Now, at least, the main
# is better than before but not perfect yet.

## [0.1.1] - 2023-09-25
## Added
# I finally could fix the method to verify if the player can put a word on the board when a word has been put before. It reads the
# the tiles of the cells where the player is going to put a tile, if the cell hasn't a tile the method just add the player's tile,
# and if the cell has a tile, the method compares the letter of the player's tile with the letter of the cell's tile, then if the
# letters are equal, the method just leaves the tile inside the cell and continues with the next tile. And finally, if the letters
# aren't equal, the method retunrs False. I made tests to check if it works when the player wants to put a word in horizontal, both
# cases True and False, or vertical, both cases True and False. Also, I made a method to remove the tile from a cell, just in case it
# is needed. It's tested too.

## [0.1.0] - 2023-9-24
## Added
# In this version I disabled the method that check if the player can put a word on the board, when a word was already put, because it
# doesn't work anymore. I change the board constructor to create it with cells with multipliers and multipliers type. I also create
# some tests to check the cells' multipliers and work correctly. For the next version i'll try to fix the method for the player's word
# on the board when it has a word on it. 

## [0.0.9] - 2023-09-23
## Added
# I've added a method in the class Board to check if the board is empty or not with the center cell of the grid, which must be used to
# start the game because according to the rules you start putting a word on the center of the board. Also, I did a method to put a word
# on the board crossing with another word. It checks if the cells are empty or not, if they're not empty, the method compares the
# letter inside the cell with the one that the player wants to put in. If are equal, the method just leaves the letter inside and
# continues checking the rest of the following cells. This last one has an error that I can't understand very well why it happens, but
# the tests runs correctly, if I fix the error in the way it should be corrected, the tests don't run correctly anymore. I'll try to
# fix as soon as posible.

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
