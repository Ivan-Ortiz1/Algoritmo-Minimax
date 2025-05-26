import random

# Variables de posicion de los personajes, movimientos maximos y cantidad de filas y columnas,
Tamaño = 5
posicion_inicial_gato = (0, 0)
posicion_inicial_raton = (4, 4)
movimientos_max = 20


# Crea el tablero e imprime las posiciones
def imprimir_tablero(gato, raton):
    print()
    for fila in range(Tamaño):
        for columna in range(Tamaño):
            if (fila, columna) == gato:
                print("|G|", end=" ")
            elif (fila, columna) == raton:
                print("|R|", end=" ")
            else:
                print("|.|", end=" ")
        print()
    print()


# Movimiento posibles: arriba, abajo, izquierda, derecha, y evita salir del tablero


def movimientos_validos(posicion):
    fila_actual, columna_actual = posicion
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    movimientos = []
    for desplazamiento_fila, desplazamiento_columna in direcciones:
        nueva_fila = fila_actual + desplazamiento_fila
        nueva_columna = columna_actual + desplazamiento_columna
        if 0 <= nueva_fila < Tamaño and 0 <= nueva_columna < Tamaño:
            movimientos.append((nueva_fila, nueva_columna))
    return movimientos


def distancia(posicion1, posicion2):
    return abs(posicion1[0] - posicion2[0]) + abs(posicion1[1] - posicion2[1])


def minimax(pos_gato, pos_raton, profundidad, es_turno_raton):
    if pos_gato == pos_raton:
        return -10000 if es_turno_raton else 10000

    if profundidad == 0:
        return distancia(pos_gato, pos_raton) * (1 if es_turno_raton else -1)

    if es_turno_raton:
        mejor_valor = -float("-inf")
        for nuevo_raton in movimientos_validos(pos_raton):
            valor = minimax(pos_gato, nuevo_raton, profundidad - 1, False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float("-inf")
        for nuevo_gato in movimientos_validos(pos_gato):
            valor = minimax(nuevo_gato, pos_raton, profundidad - 1, True)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor


def mejor_movimiento_raton(gato, raton):
    if random.random() < 0.7:
        mejor_valor = -float("inf")
        mejor_mov = raton
        for mov in movimientos_validos(raton):
            valor = minimax(gato, mov, 3, False)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_mov = mov

        return mejor_mov
    else:
        return random.choice(movimientos_validos(raton))


def mejor_movimiento_gato(gato, raton):
    if random.random() < 0.7:
        mejor_valor = float("inf")
        mejor_mov = gato
        for mov in movimientos_validos(gato):
            valor = minimax(mov, raton, 5, True)
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_mov = mov
        return mejor_mov
    else:
        return random.choice(movimientos_validos(gato))


def juego_terminado(gato, raton, turno, max_turnos):
    if gato == raton:
        print("El gato atrapó al ratón.")
        return True
    if turno >= max_turnos:
        print("El ratón escapó tras sobrevivir los turnos.")
        return True
    return False


def jugar():
    turno = 0
    gato = posicion_inicial_gato
    raton = posicion_inicial_raton

    imprimir_tablero(gato, raton)

    while not juego_terminado(gato, raton, turno, movimientos_max):
        print(f"Turno {turno + 1}:")
        raton = mejor_movimiento_raton(gato, raton)

        if gato == raton:
            imprimir_tablero(gato, raton)
            break

        gato = mejor_movimiento_gato(gato, raton)

        imprimir_tablero(gato, raton)
        turno += 1

        print(f"RATÓN se mueve a {raton}")
    print(f"GATO se mueve a {gato}")


if __name__ == "__main__":
    jugar()
