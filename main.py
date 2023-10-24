from game.scrabble import ScrabbleGame

class Main:
    def __init__(self):
        print("¡¡¡ WELCOME TO SCRABBLE !!!")
        self.players_count = self.get_player_count()
        self.game = ScrabbleGame(self.players_count)
        self.players_nicknames()
        self.game_status = True       

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
        
    def players_nicknames(self):
        print("Cantidad de jugadores: ", len(self.game.players))
        for i in range(len(self.game.players)):
            self.game.players[i].nickname = str(input('Ingrese su apodo: '))
    
    def print_menu(self):
        self.split1()
        self.game.initial_turn()
        self.game.board.print_board()
        self.split1()
        player_tiles=[]
        for i in range(len(self.game.current_player.tiles)):
            player_tiles.append(self.game.current_player.tiles[i].letter)
        print(f"Turno del jugardor {self.game.current_player.nickname}. Puntaje de {self.game.current_player.nickname}: {self.game.current_player.score}.\n Sus fichas son:\n                                          {player_tiles}\n")
        print('                  ','1- Jugar','   ','2- Intercambiar fichas','   ','3- Pasar','   ','4- Rendirse','\n')

    def get_word(self):
        word = str(input("¿Qué palabra quiere agregar al tablero?: "))
        word = word.upper()
        return word
        
    def get_location(self):
        word = self.get_word()
        while True:
            location_row = (int(input("¿En qué fila quiere poner la palabra?: ")))
            location_column = (int(input("¿En qué columna quiere que comience la plabra?: ")))
            location = [location_row,location_column]
            if location[0] == 7 and location[1] <= 7 and (location[1]+(len(word)-1)) >= 7:
                break
            if location[1] == 7 and location[0] <= 7 and (location[0]+(len(word)-1)) >= 7:
                break
            else:
                location = []
                print("Debe comenzar pasando por el centro...")
        return word,location
    
    def get_orientation(self):
        word, location = self.get_location()
        while True:
            orientation = str(input("¿Qué orientación tendrá la palabra? (H/V): "))
            orientation = orientation.upper()
            if orientation != 'H' and orientation != 'V':
                print('Debe escribir solo la letra H o V.')
            elif self.game.board.is_empty() == True:
                if location[0] == 7 and location[1] == 7:
                    break
                elif location[0] == 7 and orientation != 'H':
                    print('Recuerde pase por el centro...')
                elif location[1] == 7 and orientation != 'V':
                    print('Recuerde pase por el centro...')
                else:
                    break
            else:
                break
        return word,location,orientation

    def get_args(self):
        return self.get_orientation()

    def play(self):
        if self.game.board.is_empty() == True:
            print("Recuerde que para comenzar el juego, debe iniciar con una palabra que pase por el centro del tablero.")
        else:
            print('La palabra debe cruzar con otra palabra.')
        word, location, orientation = self.get_args()
        if self.game.validate_word(word,location,orientation) == True:
            self.game.put_word(word,location,orientation)
            self.game.score_sum(word,location,orientation)
            self.game.next_turn()
        else:
            print('La palabra no es válida.')

    def change_tiles(self):
        pass

    def pass_turn(self):
        self.split2()
        self.game.next_turn()

    def surrender(self):
        if len(self.game.players) == 2:
            print(f'{self.game.current_player.nickname} se ha rendido. El juego ha acabado.')
            self.game_status = False
            self.split2()

        elif len(self.game.players) > 2:
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

    def main(self):
        while self.game_status is True:
            self.print_menu()
            opcion = int(input('Ingrese el número de la opcion que quiere realizar: '))
            if opcion == 1:
                self.play()

            elif opcion == 2:
                print('cambiar fichas')

            elif opcion == 3:
                self.pass_turn()

            elif opcion == 4:
                self.surrender()
                if len(self.game.players) == 1:
                    break
            elif opcion > 4:
                print('Valor invalido. Elegir (1;2;3).')

if __name__ == '__main__':
    main = Main()
    main.main()