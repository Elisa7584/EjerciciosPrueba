#Crea una función a la que le pases una palabra y te indique si la palabra introducida solo tiene letras

def comprobarPalabra(palabra):
    return  palabra.isalpha()
def comprobarNumeros(num):
    return num.isdigit()

    
palabra = input("Dime una palabra: ")
numero = input("Dime un numero:")

if comprobarPalabra(palabra):
    print("Solo hay letras")
else:
    print("No solo hay letras")

if comprobarNumeros(numero):
    print("Solo hay numeros")
else:
    print("No solo hay numeros")


