from tateti import Tateti
from jugador import Jugador


def main():
    print("Bienvenidos al Tateti")
    nombre1 = input("Nombre del jugador 1 (X): ")
    nombre2 = input("Nombre del jugador 2 (O): ")
    jugador1 = Jugador(nombre1, "X")
    jugador2 = Jugador(nombre2, "O")
    juego = Tateti(jugador1, jugador2)
    while True:
        print("Tablero:")
        for fila in juego.tablero.contenedor:
            print(fila)
        print(f"Turno de: {juego.jugador_actual.nombre} ({juego.jugador_actual.ficha})")
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese col (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
            if juego.hay_ganador():
                print(f"¡Ganó {juego.jugador_actual.nombre}!")
                break
            if juego.tablero_lleno():
                print("¡Empate!")
                break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()