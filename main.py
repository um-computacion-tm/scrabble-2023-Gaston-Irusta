from game.scrabble import ScrabbleGame
from game.player import Player

def split1():
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
           )
def split2():
    print ('_______________________________________________________________________________________________________\n'
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
    for i in range(len(scrabble_game.players)):
        scrabble_game.players[i].nickname = str(input('Ingrese su apodo: '))
    game_status = True
    while game_status is True:
        split1()
        scrabble_game.next_turn()
        scrabble_game.board.print_board()
        split1()
        player_tiles=[]
        for i in range(len(scrabble_game.current_player.tiles)):
            player_tiles.append(scrabble_game.current_player.tiles[i].letter)
        print(f"Turno del jugardor {scrabble_game.current_player.nickname}. Sus fichas son:\n                                          {player_tiles}\n")
        print('                  ','1- Jugar.','   ','2- Intercambiar fichas.','   ','3- Pasar','   ','4- Rendirse')
        opcion = int(input('Ingrese el número de la opcion que quiere realizar: '))
        print(opcion)
        if opcion == 1:
            print('jugar')
        elif opcion == 2:
            print('cambiar fichas')
        elif opcion == 3:
            split2()
            pass
        elif opcion == 4 and len(scrabble_game.players) == 2:
            perdedor = scrabble_game.current_player
            scrabble_game.next_turn()
            ganador = scrabble_game.current_player
            print(f'{perdedor.nickname} se ha rendido. El ganador es {ganador.nickname}')
            split2()
            break
        elif opcion == 4 and len(scrabble_game.players) > 2:
            if scrabble_game.current_player.id == 0:
                print(f'{scrabble_game.current_player.nickname} se ha rendido. Quedan {(len(scrabble_game.players))-1} jugadores.')
                
            
            elif 0 < scrabble_game.current_player.id < len(scrabble_game.players):
                print(f'{scrabble_game.current_player.nickname} se ha rendido. Quedan {(len(scrabble_game.players))-1} jugadores.')
                perdedor = scrabble_game.current_player
                scrabble_game.current_player = scrabble_game.players[(perdedor.id)-1]
                del scrabble_game.players[perdedor.id]
            
        elif opcion > 4:
            print('Valor invalido. Elegir (1;2;3).')


main()
