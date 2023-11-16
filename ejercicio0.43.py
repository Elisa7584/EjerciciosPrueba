#Solicita una vocal por consola y repite la petición hasta que te intoduzcan una vocal

letraUsuario = input("Introduce una vocal: ")

while letraUsuario == "a" or letraUsuario == "e" or letraUsuario == "i" or letraUsuario == "o" or letraUsuario == "u":
    letraUsuario = input("Lo siento, no es una consonante , vuelve a introducirla: ")
print("Es una consonante")