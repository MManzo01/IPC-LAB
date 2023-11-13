# Definir las constantes
TABLA_TAMANO = 10
NUM_BARCOS_PEQUENOS = 3
NUM_BARCOS_GRANDES = 2
TAMANO_BARCO_PEQUENO = 3
TAMANO_BARCO_GRANDE = 5

# Clase para representar el tablero
class Tablero:
    def __init__(self):
        self.tablero = [[' ' for _ in range(TABLA_TAMANO)] for _ in range(TABLA_TAMANO)]
        self.disparos = [[' ' for _ in range(TABLA_TAMANO)] for _ in range(TABLA_TAMANO)]

    def imprimir_tablero(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        for i in range(TABLA_TAMANO):
            fila = ' '.join(self.tablero[i])
            print(chr(65 + i) + ' ' + fila)

    def imprimir_disparos(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        for i in range(TABLA_TAMANO):
            fila = ' '.join(self.disparos[i])
            print(chr(65 + i) + ' ' + fila)

    def colocar_barco(self, fila, columna, orientacion, tamano):
        fila_idx = ord(fila) - ord('A')
        columna_idx = columna - 1

        if orientacion == "horizontal":
            for i in range(tamano):
                self.tablero[fila_idx][columna_idx + i] = 'S'
        else:
            for i in range(tamano):
                self.tablero[fila_idx + i][columna_idx] = 'S'

# Función para que el jugador coloque sus barcos
def colocar_barcos(jugador, tablero):
    print(f"Jugador {jugador}, coloca tus barcos:")
    for i in range(NUM_BARCOS_PEQUENOS):
        colocar_barco(jugador, tablero, TAMANO_BARCO_PEQUENO)
    for i in range(NUM_BARCOS_GRANDES):
        colocar_barco(jugador, tablero, TAMANO_BARCO_GRANDE)

# Función para colocar un barco en el tablero
def colocar_barco(jugador, tablero, tamano):
    print(f"Coloca un barco de tamaño {tamano}.")
    while True:
        try:
            coordenada = input("Ingresa la coordenada (por ejemplo, A2): ").strip().upper()
            fila = coordenada[0]
            columna = int(coordenada[1:])
            orientacion = input("Horizontal o vertical (H/V): ").strip().lower()

            if (fila < 'A' or fila > 'J') or (columna < 1 or columna > 10) or (orientacion not in ['h', 'v']):
                print("Coordenada u orientación inválida. Inténtalo de nuevo.")
                continue

            tablero.colocar_barco(fila, columna, "horizontal" if orientacion == 'h' else "vertical", tamano)
            tablero.imprimir_tablero()
            break
        except (ValueError, IndexError):
            print("Coordenada inválida. Inténtalo de nuevo.")

# Crear tableros para ambos jugadores
tablero_jugador1 = Tablero()
tablero_jugador2 = Tablero()

# Colocar barcos en los tableros
colocar_barcos(1, tablero_jugador1)
colocar_barcos(2, tablero_jugador2)

# Función para verificar si una coordenada es válida
def es_coordenada_valida(coordenada):
    return 'A' <= coordenada[0] <= 'J' and 1 <= int(coordenada[1:]) <= 10

# Función para realizar un disparo
def disparar(jugador, tablero, tablero_oponente):
    print(f"Jugador {jugador}, es tu turno.")
    while True:
        try:
            coordenada = input("Ingresa la coordenada a disparar (por ejemplo, A2): ").strip().upper()

            if not es_coordenada_valida(coordenada):
                print("Coordenada inválida. Inténtalo de nuevo.")
                continue

            fila = coordenada[0]
            columna = int(coordenada[1:])
            fila_idx = ord(fila) - ord('A')
            columna_idx = columna - 1

            if tablero_oponente.tablero[fila_idx][columna_idx] == 'S':
                print("¡Impacto!")
                tablero_oponente.tablero[fila_idx][columna_idx] = 'X'
                tablero.disparos[fila_idx][columna_idx] = 'X'
            else:
                print("Agua.")
                tablero_oponente.tablero[fila_idx][columna_idx] = 'O'
                tablero.disparos[fila_idx][columna_idx] = 'O'
            break
        except (ValueError, IndexError):
            print("Coordenada inválida. Inténtalo de nuevo.")

# Función para determinar al ganador:
def determinar_ganador(tablero):
    for fila in tablero.tablero:
     if 'S' in fila:
            return None
    return "Jugador 2" if tablero == tablero_jugador1 else "Jugador 1"

# Iniciar el juego
while True:
    # Turno del jugador 1
    tablero_jugador2.imprimir_disparos()
    disparar(1, tablero_jugador1, tablero_jugador2)

    # Verificar si el jugador 1 ganó
    ganador = determinar_ganador(tablero_jugador2)
    if ganador:
        print(f"{ganador} ha ganado. ¡Felicidades!")
        break

    # Turno del jugador 2
    tablero_jugador1.imprimir_disparos()
    disparar(2, tablero_jugador2, tablero_jugador1)

    # Verificar si el jugador 2 ganó
    ganador = determinar_ganador(tablero_jugador1)
    if ganador:
        print(f"{ganador} ha ganado. ¡Felicidades!")
        break

