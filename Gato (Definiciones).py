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