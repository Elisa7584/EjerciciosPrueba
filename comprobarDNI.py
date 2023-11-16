def longitud(cadena):
    longitud = 0
    for caracter in cadena:
        longitud += 1
    return longitud

def comprobarNumeros(dni):
    sonNumeros = True
    for pos in range(longitud(dni)-1):
        if dni[pos] < '0' or dni[pos] > '9':
            sonNumeros = False
    return sonNumeros
    
def comprobarLetra(dni):
    esLetra = True
    # if dni[7] < 'a' or dni[7] > 'Z':
    if dni[longitud(dni)-1] < 'a' or dni[longitud(dni)-1] > 'Z': # longitud(cadena)-1  ->  esto se refiere a la ultima posicion
        esLetra = False 
    return esLetra

# - - - -  MAIN  - - - - 

repetir = True 
while repetir == True:
    dni = input('Introduce un DNI -> ')
    repetir = False 
    if longitud(dni) != 9:
        print('El DNI debe de tener 9 caracteres')
        if comprobarNumeros(dni) == False:
            print('El DNI no tiene los numeros que le corresponden')
            if comprobarLetra(dni) == False:
                print('El DNI no tiene una letra final')
        repetir = True
    
print(f"Has introducido el siguiente DNI correcto -> {dni}") 