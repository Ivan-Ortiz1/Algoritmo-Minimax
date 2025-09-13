from juego import Juego


def pedir_posicion(nombre, filas, columnas):
    while True:
        try:
            f = int(input(f"Ingrese fila inicial del {nombre} (0 a {filas-1}): "))
            c = int(input(f"Ingrese columna inicial del {nombre} (0 a {columnas-1}): "))
            if 0 <= f < filas and 0 <= c < columnas:
                return (f, c)
            else:
                print("Posición fuera del tablero. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Use números.")


if __name__ == "__main__":
    filas = int(input("Ingrese número de filas del tablero: "))
    columnas = int(input("Ingrese número de columnas del tablero: "))
    movimientos_max = int(input("Ingrese número máximo de turnos: "))

    pos_gato = pedir_posicion("GATO", filas, columnas)
    pos_raton = pedir_posicion("RATÓN", filas, columnas)

    juego = Juego(filas, columnas, pos_gato, pos_raton, movimientos_max)
    juego.jugar()
