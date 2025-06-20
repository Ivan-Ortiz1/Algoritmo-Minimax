 ## Resumen general del juego
Tablero de 5x5.

El ratón empieza en la esquina inferior derecha (4, 4).

El gato empieza en la esquina superior izquierda (0, 0).

Ambos se mueven alternadamente en las 4 direcciones cardinales.

El juego dura un máximo de 20 turnos.

El ratón gana si sobrevive los 20 turnos sin ser atrapado.

El gato gana si alcanza al ratón antes.

## Descripción paso a paso
1. 🧱 Tablero
La función imprimir_tablero muestra el estado del juego:

"|G|" para el gato

"|R|" para el ratón

"|.|" para las casillas vacías

## Movimientos válidos
Ambos personajes pueden moverse:

Arriba, abajo, izquierda o derecha.

No pueden salir del tablero.

## Algoritmo Minimax
El cerebro del juego.

Objetivo del minimax:
El ratón intenta maximizar la distancia con el gato (escapar).

El gato intenta minimizar esa distancia (acercarse y atraparlo).

Se usa una profundidad limitada (hasta 5 movimientos en adelante).

Detalles:
El ratón evalúa sus movimientos posibles y elige el mejor.

El gato hace lo mismo pero desde su perspectiva.

70% de las veces toman la mejor decisión, y 30% eligen al azar para agregar variedad.

## Condiciones para terminar el juego
La función juego_terminado detiene el juego cuando:

El gato atrapa al ratón (gato == raton).

Se alcanzan los 20 turnos y el ratón sigue vivo.

## Función principal jugar()
Controla el flujo del juego:

Alterna los turnos.

Llama a los movimientos del ratón y luego del gato.

Muestra el tablero tras cada turno.
