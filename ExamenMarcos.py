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
    
# Primero creamos la lista con las letras necesarias
letras = "abcdefghijklmnñopqrstuvwxyz"
listaLetras = []

for l in letras:    
    listaLetras.append(l)
    
# Pedimos datos al usuario

letra = input("Introduce una letra -> ")
num = int(input("Introduce un numero -> "))
l = buscarLetra(listaLetras,letra,num)
print(l)
