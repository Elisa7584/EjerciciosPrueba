#Solicita una letra por consola.
#Si esa letra está en una lista de vocales, di que es vocal.

listaVocales = ["a","e","i","o","u"]

letraUsuario = input("Introduce una letra: ")

for letra in listaVocales:
    if letraUsuario == letra:
        print(f"la letra {letraUsuario} es una vocal")
    elif letraUsuario != letra:
        print(f"la letra {letraUsuario} es una consonante")
    

