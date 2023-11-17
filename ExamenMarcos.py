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

def traducir(frase,lista1,lista2):
    fraseTraducida = ""
    for letra in frase:
        fraseTraducida += buscarLetra(lista1,letra,(longitud(lista2) - longitud(lista1)))
    return fraseTraducida

# HE HECHO UN ULTIMO COMMIT AHORA MISMO, COPIA TODO DE 0, QUE HE CAMBIADO LOS METODOS

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

# EJERCICIO 4 - No funciona por ahora xD

frase = input("Introduce una frase: ")
fraseTraducida = traducir(frase, listaLetras, listaDesordenada)
print("La frase traducida es:", fraseTraducida)
