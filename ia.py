from personajes import Gato, Raton


def evaluar(gato, raton):
    # Distancia Manhattan: cuanto más lejos está el ratón, mejor para él
    return abs(gato.posicion[0] - raton.posicion[0]) + abs(
        gato.posicion[1] - raton.posicion[1]
    )


def minimax(gato, raton, profundidad, maximizando, filas, columnas):
    if profundidad == 0 or gato.posicion == raton.posicion:
        return evaluar(gato, raton)

    if maximizando:  # turno del ratón
        mejor_valor = float("-inf")
        for mov in raton.movimientos_validos(filas, columnas):
            nuevo_raton = Raton("ratón", mov)
            valor = minimax(gato, nuevo_raton, profundidad - 1, False, filas, columnas)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:  # turno del gato
        mejor_valor = float("inf")
        for mov in gato.movimientos_validos(filas, columnas):
            nuevo_gato = Gato("gato", mov)
            valor = minimax(nuevo_gato, raton, profundidad - 1, True, filas, columnas)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor


def mejor_movimiento_raton(gato, raton, filas, columnas):
    # Se queda con el primer movimiento que maximice el valor
    mejor_valor = float("-inf")
    mejor_movimiento = raton.posicion
    for mov in raton.movimientos_validos(filas, columnas):
        nuevo_raton = Raton("ratón", mov)
        valor = minimax(gato, nuevo_raton, 3, False, filas, columnas)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = mov
    return mejor_movimiento


def mejor_movimiento_gato(gato, raton, filas, columnas):
    # Se queda con el primer movimiento que minimice el valor
    mejor_valor = float("inf")
    mejor_movimiento = gato.posicion
    for mov in gato.movimientos_validos(filas, columnas):
        nuevo_gato = Gato("gato", mov)
        valor = minimax(nuevo_gato, raton, 3, True, filas, columnas)
        if valor < mejor_valor:
            mejor_valor = valor
            mejor_movimiento = mov
    return mejor_movimiento
