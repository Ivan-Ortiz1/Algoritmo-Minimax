Gato y Ratón — Juego por turnos (POO)

Juego por turnos implementado en Python usando programación orientada a objetos. Diseño modular (clases Juego, Tablero, Personaje / Gato / Ratón, y módulo ia) pensado para escalar: agregar obstáculos, vidas, modos de juego o interfaz gráfica sin romper la arquitectura.

Características principales

Tablero dinámico: filas y columnas configurables por el usuario.

Posiciones iniciales del gato y del ratón definidas por el usuario (validación incluida).

Turnos máximos configurables.

IA basada en Minimax con evaluación por distancia Manhattan y elemento de aleatoriedad (70% elige la mejor jugada, 30% aleatorio).

Código organizado en módulos y clases para facilitar mantenimiento y testing.

Sin dependencias externas (Python estándar).

Estructura del proyecto
gato_raton/
│── main.py           # Punto de entrada (interacción con el usuario)
│── juego.py          # Clase Juego: flujo principal y condiciones de victoria
│── tablero.py        # Clase Tablero: representación e impresión
│── personajes.py     # Personaje, Gato, Raton (movimientos válidos, estado)
│── ia.py             # Minimax y funciones de decisión (mejor movimiento)
│── README.md         # Este archivo
│── .gitignore        # Recomendado (ver ejemplo más abajo)

Resumen del diseño (clases y responsabilidades)

Tablero (tablero.py)

Mantiene filas, columnas y la matriz base.

Método imprimir(gato, raton) para mostrar el estado actual.

Personaje (personajes.py)

Propiedades: nombre, posicion.

Método movimientos_validos(filas, columnas) que devuelve los movimientos cardinales permitidos.

Gato y Raton heredan de Personaje.

ia (ia.py)

minimax(gato, raton, profundidad, es_turno_raton, filas, columnas) — búsqueda Minimax limitada.

mejor_movimiento_raton(...) y mejor_movimiento_gato(...) — seleccionan jugadas (70% óptima, 30% aleatoria).

Evaluación: distancia Manhattan entre gato y ratón.

Juego (juego.py)

Inicializa las entidades y el tablero.

Controla el bucle de juego: mover ratón, comprobar colisión, mover gato, imprimir estado, contar turnos y decidir ganador.

Comportamiento de la IA (detalles relevantes)

Si gato.posicion == raton.posicion la evaluación termina (estado terminal).

En profundidad 0 la heurística es la distancia Manhattan (|dx| + |dy|).

El ratón busca maximizar la distancia; el gato busca minimizarla.

Profundidades usadas en la implementación actual: ratón 3, gato 5 (puedes cambiarlas en ia.py si quieres más lookahead a costa de tiempo de cómputo).

Para evitar jugadas 100% deterministas se introduce un 30% de jugada aleatoria.

Sugerencias rápidas para extender

Añadir obstaculos en Tablero y filtrar movimientos_validos.

Añadir atributos vidas o puntaje en Personaje o Juego.

Reemplazar la entrada por consola con argumentos CLI (argparse) o con una interfaz (Pygame / web).

Escribir tests unitarios (pytest) para movimientos_validos, minimax y juego_terminado.
