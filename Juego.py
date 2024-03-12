import random

class Gato:
    def __init__(self):
        # Tablero representado como un diccionario donde las claves son las posiciones y los valores son los marcadores ('X', 'O' o espacio vacío)
        self.tablero = {i: ' ' for i in range(1, 10)}
        self.turno = 'X'  # Empezamos con 'X'
    
    def mostrar_tablero(self):
        # Método para mostrar el tablero
        print("\n")
        for i in range(1, 10, 3):
            print(" | ".join([self.tablero[j] for j in range(i, i+3)]))
            if i < 7:
                print("-" * 9)

    def marcar_casilla(self, posicion):
        # Método para marcar una casilla en el tablero
        if self.tablero[posicion] == ' ':
            self.tablero[posicion] = self.turno
            return True
        else:
            return False

    def cambiar_turno(self):
        # Método para cambiar el turno
        self.turno = 'O' if self.turno == 'X' else 'X'

    def verificar_ganador(self):
        # Método para verificar si hay un ganador
        lineas_ganadoras = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        for linea in lineas_ganadoras:
            if self.tablero[linea[0]] == self.tablero[linea[1]] == self.tablero[linea[2]] != ' ':
                return self.tablero[linea[0]]
        if ' ' not in self.tablero.values():
            return 'Empate'
        return None

    def jugar(self):
        # Método principal para jugar el juego
        print("Bienvenido al juego de Gato! Las casillas están numeradas del 1 al 9, de izquierda a derecha y de arriba a abajo.")
        self.mostrar_tablero()
        while True:
            if self.turno == 'X':
                posicion = int(input("Jugador X, elige una casilla para marcar (1-9): "))
                if self.marcar_casilla(posicion):
                    self.cambiar_turno()
                else:
                    print("Esa casilla ya está ocupada. Por favor, elige otra.")
                    continue
            else:
                print("Turno de la computadora (O):")
                posicion = self.jugar_computadora()
                self.marcar_casilla(posicion)
                self.cambiar_turno()
            self.mostrar_tablero()
            ganador = self.verificar_ganador()
            if ganador:
                if ganador == 'Empate':
                    print("¡Es un empate!")
                else:
                    print("¡El jugador", ganador, "ha ganado!")
                break