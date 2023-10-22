from game.scrabble import ScrabbleGame

class Main:
    def __init__(self):
        print("¡¡¡ WELCOME TO SCRABBLE !!!")
        self.players_count = self.get_player_count()
        self.game = ScrabbleGame(self.players_count)
        

    def split1(self):
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    def split2(self):
        print ('_______________________________________________________________________________________________________\n')

    def get_player_count(self):
        while True:
            num_players = int(input("Ingrese la cantidad de jugadores: "))
            if self.validate_player_count(num_players) is True:
                return num_players
            else:
                print("Valor invalido, elgir entre 2-4 jugadores.")

    def validate_player_count(self,player_count):
        try:
            if 2 <= int(player_count) <= 4 :
                return True
        except ValueError:
                return False
        
    def play(self):

        print("Cantidad de jugadores: ", len(self.game.players))
        for i in range(len(self.game.players)):
            self.game.players[i].nickname = str(input('Ingrese su apodo: '))
        game_status = True
        while game_status is True:
            self.split1()
            self.game.initial_turn()
            self.game.board.print_board()
            self.split1()
            player_tiles=[]
            for i in range(len(self.game.current_player.tiles)):
                player_tiles.append(self.game.current_player.tiles[i].letter)
            print(f"Turno del jugardor {self.game.current_player.nickname}. Puntaje de {self.game.current_player.nickname}: {self.game.current_player.score}.\n Sus fichas son:\n                                          {player_tiles}\n")
            print('                  ','1- Jugar','   ','2- Intercambiar fichas','   ','3- Pasar','   ','4- Rendirse','\n')
            opcion = int(input('Ingrese el número de la opcion que quiere realizar: '))
            print(opcion)
            if opcion == 1:
                while True:
                    word = str(input("¿Qué palabra quiere agregar al tablero? Si se equivoco de opcion escriba (atras): "))
                    word = word.upper()
                    if word == 'ATRAS':
                        break
                    location = []
                    if self.game.board.is_empty() == True:
                        print("Recuerde que para comenzar el juego, debe iniciar con una palabra que pase por el centro del tablero.")
                    else:
                        print('La palabra debe cruzar con otra palabra.')
                    while True:
                        if self.game.board.is_empty() == True:
                            location.append(int(input("¿En qué fila quiere poner la palabra?: ")))
                            location.append(int(input("'En qué columna quiere que comience la plabra?: ")))
                            if location[0] == 7:
                                break
                            elif location[1] == 7:
                                break
                            else:
                                print("Debe comenzar pasando por el centro...")
                        else:
                            location.append(int(input("¿En qué fila quiere poner la palabra?: ")))
                            location.append(int(input("'En qué columna quiere que comience la plabra?: ")))
                            break
                    orientation = None
                    while True:
                        orientation = str(input("¿Qué orientación tendrá la palabra? (H/V): "))
                        orientation = orientation.upper()
                        if orientation != 'H' and orientation != 'V':
                            print('Debe escribir solo la letra H o V.')
                        elif self.game.board.is_empty() == True:
                            if location[0] == 7 and orientation != 'H':
                                print('Recuerde pase por el centro...')
                            elif location[1] == 7 and orientation != 'V':
                                print('Recuerde pase por el centro...')
                            else:
                                break
                        else:
                            break
                    if self.game.validate_word(word,location,orientation) == True:
                        print('Pasa por aqui')
                        self.game.put_word(word,location,orientation)
                        self.game.score_sum(word,location,orientation)
                        self.game.next_turn()
                        break
                    else:
                        print('La palabra no es válida.')

            elif opcion == 2:
                print('cambiar fichas')

            elif opcion == 3:
                self.split2()
                self.game.next_turn()

            elif opcion == 4 and len(self.game.players) == 2:
                perdedor = self.game.current_player.nickname
                self.game.next_turn()
                ganador = self.game.current_player.nickname
                print(f'{perdedor} se ha rendido. El ganador es {ganador}')
                self.split2()
                break

            elif opcion == 4 and len(self.game.players) > 2:
                if self.game.current_player.id == 0:
                    print(f'{self.game.current_player.nickname} se ha rendido. Quedan {(len(self.game.players))-1} jugadores.')
                    self.game.next_turn()
                    del self.game.players[0]  
                    for i in range(len(self.game.players)):
                        self.game.players[i].id -= 1

                elif 0 < self.game.current_player.id < len(self.game.players) and len(self.game.players) == 3:
                    print(f'{self.game.current_player.nickname} se ha rendido. Quedan {(len(self.game.players))-1} jugadores.')
                    perdedor = self.game.current_player
                    self.game.next_turn()
                    del self.game.players[perdedor.id]
                    self.game.current_player.id -= 1

                elif 0 < self.game.current_player.id < len(self.game.players) and len(self.game.players) == 4:
                    print(f'{self.game.current_player.nickname} se ha rendido. Quedan {(len(self.game.players))-1} jugadores.')
                    perdedor = self.game.current_player
                    self.game.next_turn()
                    del self.game.players[perdedor.id]
                    if perdedor.id == 1:
                        self.game.players[1].id = 1
                        self.game.players[2].id = 2
                    if perdedor.id == 2:
                        self.game.players[2].id = 2

                elif self.game.current_player.id == len(self.game.players):
                    print(f'{self.game.current_player.nickname} se ha rendido. Quedan {(len(self.game.players))-1} jugadores.')
                    perdedor = self.game.current_player
                    self.game.current_player = self.game.players[(perdedor.id)-1]
                    del self.game.players[perdedor.id]

            elif opcion > 4:
                print('Valor invalido. Elegir (1;2;3).')

if __name__ == '__main__':
    main = Main()
    main.play()