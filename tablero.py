class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [["." for _ in range(columnas)] for _ in range(filas)]

    def imprimir(self, gato, raton):
        copia = [fila[:] for fila in self.matriz]
        fila_gato, columna_gato = gato.posicion
        fila_raton, columna_raton = raton.posicion
        copia[fila_gato][columna_gato] = "G"
        copia[fila_raton][columna_raton] = "R"

        for fila in copia:
            print(" ".join(fila))
        print()
