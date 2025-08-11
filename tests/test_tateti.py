import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest

from tateti import Tateti
from jugador import Jugador

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.j1 = Jugador("Sofía", "X")
        self.j2 = Jugador("Juan", "O")
        self.juego = Tateti(self.j1, self.j2)

    def test_turnos(self):
        self.assertEqual(self.juego.jugador_actual, self.j1)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.jugador_actual, self.j2)

    def test_ganador_fila(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 0)  # O
        self.juego.ocupar_una_de_las_casillas(0, 1)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(0, 2)  # X
        self.assertTrue(self.juego.hay_ganador())

    def test_empate(self):
        jugadas = [
            (0,0), (0,1), (0,2),
            (1,1), (1,0), (1,2),
            (2,1), (2,0), (2,2)
        ]
        for i, (f, c) in enumerate(jugadas):
            self.juego.ocupar_una_de_las_casillas(f, c)
        self.assertTrue(self.juego.tablero_lleno())
        self.assertFalse(self.juego.hay_ganador())

if __name__ == "__main__":
    unittest.main()
    os.system('python -m unittest discover __tests__')