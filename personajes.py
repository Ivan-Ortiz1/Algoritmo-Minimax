class Personaje:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def movimientos_validos(self, filas, columnas):
        fila_actual, columna_actual = self.posicion
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        movimientos = []
        for df, dc in direcciones:
            nueva_fila, nueva_columna = fila_actual + df, columna_actual + dc
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                movimientos.append((nueva_fila, nueva_columna))
        return movimientos


class Gato(Personaje):
    pass


class Raton(Personaje):
    pass
