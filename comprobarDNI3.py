def calcularLetra(dni):
    total = 0
    nMultiplicar = 1
    
    for pos in range(longitud(dni) - 1):
        total += (int(dni[pos]) * nMultiplicar)
        nMultiplicar += 1
        
    numLetraCorrespondiente = total % 23
    
    letras_dni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L",]
    
    return letras_dni[numLetraCorrespondiente]
        
def longitud(cadena):
    longitud = 0
    for caracter in cadena:
        longitud += 1
    return longitud

def validar_dni(dni):
    validar = True
    long = longitud(dni)

    if long != 9:
        validar = False

    for i in range(8):
        if dni[i] < '0' or dni[i] > '9':
            validar = False

    if dni[8] != calcularLetra(dni):
        validar = False

    return validar


dni = input("Dime tu DNI: ")

if validar_dni(dni) == True:
    print("mu bien")