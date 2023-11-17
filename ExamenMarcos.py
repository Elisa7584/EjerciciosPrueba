import random

def longitud(lista):
    longitud = 0
    for elemento in lista:
        longitud += 1
    return longitud

def buscarLetra(lista,letra,num):
    letraEncontrada = "no encontrada"
    for pos in range(longitud(lista)):
        if lista[pos] == letra:
            letraEncontrada = lista[pos+num]
    return letraEncontrada

def desordenar_lista(lista):
    # Se itera sobre la lista.
    for i in range(longitud(lista)):
        # Se genera un índice aleatorio.
        j = random.randint(0, longitud(lista)-1)
        # Se intercambian los elementos de los índices i y j.
        lista[i], lista[j] = lista[j], lista[i]
    return lista
    
# EJERCICIO 1

# Primero creamos la lista con las letras necesarias
letras = "abcdefghijklmnñopqrstuvwxyz"
listaLetras = []

for l in letras:    
    listaLetras.append(l)
    
# Pedimos datos al usuario

letra = input("Introduce una letra -> ")
num = int(input("Introduce un numero -> "))

l = buscarLetra(listaLetras,letra,num)
print(f"Letra encontrada:{l}")

# EJERCICIO 3

listaDesordenada = desordenar_lista(listaLetras)

print(listaDesordenada)
