from game.scrabble import ScrabbleGame
from game.player import Player

def split():
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
           )

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
game_status = True

def main():
    while game_status is True:
        split()
        scrabble_game.next_turn()
        scrabble_game.board.print_board()
        split()
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
            pass
        elif opcion == 4:
            perdedor = scrabble_game.current_player
            scrabble_game.next_turn()
            ganador = scrabble_game.current_player
            print(f'{perdedor.nickname} se ha rendido. El ganador es {ganador.nickname}')
            break
        elif opcion > 4:
            print('Valor invalido. Elegir (1;2;3).')


main()