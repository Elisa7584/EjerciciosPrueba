import random

def longitud(lista):
    longitud = 0
    for elemento in lista:
        longitud += 1
    return longitud

def buscarLetra(lista, letra, num):
    letraEncontrada = "no encontrada"
    for pos in range(longitud(lista)):
        if lista[pos] == letra:
            nuevo_pos = (pos + num) % longitud(lista)
            letraEncontrada = lista[nuevo_pos]
    return letraEncontrada

def desordenarLista(lista):
    for i in range(longitud(lista)):
        j = random.randint(0, longitud(lista)-1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista

def letra_en_otra_lista(lista1, lista2, letra):
    index = lista1.index(letra)
    return lista2[index]

def traducir(lista1, lista2, frase):
    frase_traducida = ''
    for caracter in frase:
        if caracter in lista1:
            letra_traducida = letra_en_otra_lista(lista1, lista2, caracter)
            frase_traducida += letra_traducida
    return frase_traducida
    
# EJERCICIO 1

letras = "abcdefghijklmnñopqrstuvwxyz"
listaLetras = []

for l in letras:    
    listaLetras.append(l)
    
letra = input("Introduce una letra -> ")
num = int(input("Introduce un numero -> "))

l = buscarLetra(listaLetras,letra,num)
print(f"Letra encontrada:{l}")

# EJERCICIO 3

listaDesordenada = desordenarLista(listaLetras)

print(f"Lista desordenada:{listaDesordenada}")

# EJERCICIO 4

frase = input("Introduce una frase: ")
# NI IDEA POR AHORA
fraseTraducida = traducir(frase, listaLetras, listaDesordenada)
print("La frase traducida es:", fraseTraducida)
