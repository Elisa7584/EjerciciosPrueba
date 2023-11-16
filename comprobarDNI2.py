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

    if dni[8] < 'a' or dni[8] > 'z' or dni[8] < 'A' or dni[8] > 'Z':
        validar = False

    return validar
