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
