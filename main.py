from game.scrabble import ScrabbleGame

def split():
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
           )

def main():
    print("¡¡¡ WELCOME TO SCRABBLE !!!")
    while True:
        try:
            num_players = int(input("Ingrese la cantidad de jugadores: "))
            if num_players <= 1 or num_players > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")
    scrabble_game = ScrabbleGame(players_count = num_players)
    print("Cantidad de jugadores: ", len(scrabble_game.players))
    split()
    scrabble_game.next_turn()
    scrabble_game.board.print_board()
    split()
    scrabble_game.next_turn()
    print(f"Turno del jugardor {scrabble_game.current_player.id}")
    print('                              ','1- Jugar.','     ','2- Intercambiar fichas.')
    # option = int(input())
    # if option == 1:
    #     word = input("Ingrese palabra.")
    #     location_x = input("Ingrese posicion X.")
    #     location_y = input("Ingrese pocision Y")
    #     location = (location_x,location_y)
    #     orientation = input("Ingrese orientación (V/H)")
    #     scrabble_game.validate_word(word, location, orientation, player_tiles=scrabble_game.current_player.tiles)
    # if option == 2:
    #     print('Fichas del jugador:\n',scrabble_game.current_player.tiles)
    # if option == 3:
    #     tile = str(input('¿Qué ficha quiere intercambiar?\n'))
    #     tile = tile.upper()
    #     '''Buscar esa letra en las fichas del jugador y asignarla a tile para meterla en la bolsa.???'''
    #     scrabble_game.bag_tiles.put(tile)
    #     scrabble_game.bag_tiles.take(1)
main()