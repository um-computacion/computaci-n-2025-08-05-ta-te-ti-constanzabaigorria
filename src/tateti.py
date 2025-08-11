from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.jugadores = [jugador1, jugador2]
        self.turno_idx = 0
        self.tablero = Tablero()

    @property
    def jugador_actual(self):
        return self.jugadores[self.turno_idx]

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.jugador_actual.ficha)
        if not self.hay_ganador():
            self.turno_idx = 1 - self.turno_idx

    def hay_ganador(self):
        c = self.tablero.contenedor
        f = self.jugador_actual.ficha
        # filas, columnas y diagonales
        for i in range(3):
            if all(c[i][j] == f for j in range(3)) or all(c[j][i] == f for j in range(3)):
                return True
        if all(c[i][i] == f for i in range(3)) or all(c[i][2-i] == f for i in range(3)):
            return True
        return False

    def tablero_lleno(self):
        return all(cell != "" for row in self.tablero.contenedor for cell in row)
