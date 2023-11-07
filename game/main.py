from game.scrabble import ScrabbleGame
import os

class Main:
    def __init__(self):
        os.system('clear')
        print("¡¡¡ WELCOME TO SCRABBLE !!!")
        self.game = ScrabbleGame(self.get_player_count())
        self.players_nicknames()
        self.game_status = True       

    def split1(self):
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    def split2(self):
        print ('_______________________________________________________________________________________________________\n')


    def get_player_count(self):
        while True:
            try:
                players_count = int(input("Ingrese la cantidad de jugadores: "))
                if 2 <= players_count <= 4:
                    return players_count
            except Exception as e:
                print(e,'Ingrese un número entre 2-4 por favor.')
        
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
        self.game.wild_tile_to_end()
        for i in range(len(self.game.current_player.tiles)):
            player_tiles.append(self.game.current_player.tiles[i].letter)
        print(f"Turno del jugardor {self.game.current_player.nickname}. Puntaje de {self.game.current_player.nickname}: {self.game.current_player.score}.\n Sus fichas son:\n                                          {player_tiles}\n")
        print('                  ','1- Jugar','   ','2- Intercambiar fichas','   ','3- Pasar','   ','4- Rendirse','\n')


    def get_word(self):
        try:
            word = str(input("¿Qué palabra quiere agregar al tablero?: "))
            word = word.upper()
            num = int(len(word))
            return word, num     
        except ValueError:
            print("Escriba una palabra por favor.")

    def get_location(self):
        word,num = self.get_word() # type: ignore
        location= []
        while True:
            try:
                location_row = (int(input("¿En qué fila quiere poner la palabra?(0-14): ")))
                location_column = (int(input("¿En qué columna quiere que comience la plabra?(0-14): ")))
                location = [location_row,location_column]
                if location_column is str or location_row is str:
                    raise ValueError
                elif self.game.board.is_empty() == True:
                    if location[0] > 7 or location[1] > 7:
                        raise ValueError
                    elif location[0] == 7 and location[1] <= 7 and (location[1]+(num)) <= 7 or location[1] == 7 and location[0] <= 7 and (location[0]+(num)) <= 7:
                        raise ValueError
                break
            except ValueError:
                print("Ubicación inválida.")
                location = []
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
                elif location[0] == 7 and orientation != 'H' or location[1] == 7 and orientation != 'V':
                    print('Recuerde pase por el centro...')
                else:
                    break
            else:
                break
        return word,location,orientation

    def play(self):
        if self.game.board.is_empty() == True:
            print("Recuerde que para comenzar el juego, debe iniciar con una palabra que pase por el centro del tablero.")
        else:
            print('La palabra debe cruzar con otra palabra.')
        word, location, orientation = self.get_orientation()
        if self.game.validate_word(word,location,orientation) == True:
            self.game.put_word(word,location,orientation)
            self.game.score_sum(word,location,orientation)
            self.game.refill_player_tiles()
            self.game.next_turn()
            os.system('clear')

    def ask_if_repeat_change(self):
        answ = None
        while True:
            try:
                answ = str(input("¿Quiere intercambiar otra letra más? Si/No: "))
                answ = answ.upper()
                if answ == 'SI' or answ == 'NO':
                    break
                elif answ == 'NO':
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Escriba Si / No por favor.")

        return answ

    def get_letters_to_change(self):
        exchange = []

        while True:
            letter = str(input("¿Qué letra quiere intercambiar? Escriba solo la letra: "))
            letter = letter.upper()
            exchange.append(letter)
            answ = self.ask_if_repeat_change()
            if answ == 'NO':
                break

        return exchange

    def get_tiles_to_change(self,exchange):
        tiles = []
        if len(exchange) > 1:
            for i in range(len(exchange)):
                for x in range(len(self.game.current_player.tiles)):
                    if exchange[i] == self.game.current_player.tiles[x].letter:
                        tiles.append(self.game.current_player.tiles[x])
                        del self.game.current_player.tiles[x]
                        break
        elif len(exchange) == 1:
            for x in range(len(self.game.current_player.tiles)):
                if exchange[0] == self.game.current_player.tiles[x].letter:
                    tiles.append(self.game.current_player.tiles[x])
                    del self.game.current_player.tiles[x]
                    break
        return tiles

    def get_just_letter_player(self):
        tiles = list.copy(self.game.current_player.tiles)
        for i in range(len(tiles)):
            if tiles[i].letter == '?':
                del tiles[i]
        return tiles

    def validate_and_get_tiles_to_change(self):
        exchange = []

        while True:
            exchange = self.get_letters_to_change()
            if self.game.validate_word_and_letters_change(exchange,player_tiles=self.get_just_letter_player()) == False:
                print("No tienes esas letras para intercambiar. Prueba nuevamente.")
            elif self.game.validate_word_and_letters_change(exchange,player_tiles=self.get_just_letter_player()) == True:
                break

        tiles = self.get_tiles_to_change(exchange)
        return tiles

    def change_tiles(self):
        tiles = self.validate_and_get_tiles_to_change()
        self.game.bag_tiles.put(tiles)
        self.game.refill_player_tiles()
        self.game.next_turn()

    def pass_turn(self):
        self.split2()
        self.game.next_turn()

    def surrender_2_players(self):
            self.game.next_turn()
            print(f'Ha ganado {self.game.current_player.nickname}!')
            self.game_status = False

    def surrender(self):
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

    def get_opcion(self):
        while True:
            try:
                opcion = int(input('Ingrese el número de la opcion que quiere realizar.(1-4): '))
                if opcion < 1 or opcion > 4:
                    raise ValueError
                return opcion
            except ValueError:
                print('Opcion invalida. Elegir (1;2;3;4).')

    def main_menu(self):
        while self.game_status is True:
            self.print_menu()
            opcion = self.get_opcion()              

            if opcion == 1:
                self.play()
            elif opcion == 2:
                self.change_tiles()
                os.system('clear')

            elif opcion == 3:
                self.pass_turn()
                os.system('clear')

            elif opcion == 4:
                if len(self.game.players) == 2:
                    self.surrender_2_players()
                elif len(self.game.players) > 2:
                    self.surrender()


if __name__ == '__main__':
    Main().main_menu()