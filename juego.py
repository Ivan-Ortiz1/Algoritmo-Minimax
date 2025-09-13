from tablero import Tablero
from personajes import Gato, Raton
from ia import mejor_movimiento_gato, mejor_movimiento_raton


class Juego:
    def __init__(self, filas, columnas, pos_gato, pos_raton, movimientos_max):
        self.tablero = Tablero(filas, columnas)
        self.gato = Gato("Gato", pos_gato)
        self.raton = Raton("Ratón", pos_raton)
        self.movimientos_max = movimientos_max
        self.turno = 0

    def juego_terminado(self):
        if self.gato.posicion == self.raton.posicion:
            print("El gato atrapó al ratón.")
            return True
        if self.turno >= self.movimientos_max:
            print("El ratón escapó tras sobrevivir los turnos.")
            return True
        return False

    def jugar(self):
        self.tablero.imprimir(self.gato, self.raton)

        while not self.juego_terminado():
            print(f"Turno {self.turno + 1}:")
            # mueve ratón
            nueva_pos = mejor_movimiento_raton(
                self.gato, self.raton, self.tablero.filas, self.tablero.columnas
            )
            self.raton.posicion = nueva_pos

            if self.gato.posicion == self.raton.posicion:
                self.tablero.imprimir(self.gato, self.raton)
                break

            # mueve gato
            nueva_pos = mejor_movimiento_gato(
                self.gato, self.raton, self.tablero.filas, self.tablero.columnas
            )
            self.gato.posicion = nueva_pos

            self.tablero.imprimir(self.gato, self.raton)
            self.turno += 1
