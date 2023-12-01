# Función para crear una matriz de 10x10 rellena de los números del 0 al 99
def crear_matriz():
    matriz = []
    num = 0
    for i in range(10):
        fila = []
        for j in range(10):
            fila.append(num)
            num += 1
        matriz.append(fila)
    return matriz

# Función para imprimir la matriz por pantalla
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para verificar si un número está disponible en la matriz
def numero_disponible(matriz, numero):
    for fila in matriz:
        if numero in fila:
            return True
    return False

# Función para cambiar el número por las iniciales indicadas
def cambiar_numero_por_iniciales(matriz, numero, iniciales):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                matriz[i][j] = iniciales

# - - - { Código principal } - - -

    # Prueba a ver si todo funciona, lo he hecho deprisa !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

    matriz_rifa = crear_matriz()
    imprimir_matriz(matriz_rifa)

    seguir = True

    while seguir:
        num_elegido = int(input("Elige un número (o escribe -1 para salir): "))
        
        if num_elegido == -1:
            seguir = false
        else
            if not numero_disponible(matriz_rifa, num_elegido):
                print("Número no disponible. Elige otro número.")
            else
                iniciales = input("Escribe tus iniciales para marcar el número: ")
                cambiar_numero_por_iniciales(matriz_rifa, num_elegido, iniciales)
                imprimir_matriz(matriz_rifa)
