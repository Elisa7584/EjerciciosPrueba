def longitud(cadena):
    longitud = 0
    for caracter in cadena:
        longitud += 1
    return longitud

# PARA CADENAS (OSEA, STIRNGS QUE ACTUAN COMO LISTAS, POR ESO LAS PODEMOS RECORRER CON BUCLES)

def esLetraCadena(cadena):
    esLetr = True 
    for caracter in cadena:
        caracterStr = str(caracter)
    if caracterStr < 'a' and caracterStr > 'Z':
        esLetr = False
    return esLetr
    
def esMinusculaCadena(cadena):
    esMin = True 
    for caracter in cadena:
        caracterStr = str(caracter)
    if caracterStr < 'a' and caracterStr > 'z':
        esMin = False
    return esMin

def esMayusculaCadena(cadena):
    esMayus = True 
    for caracter in cadena:
        caracterStr = str(caracter)
    if caracterStr < 'A' and caracterStr > 'Z':
        esMayus = False
    return esMayus

def esNumeroCadena(cadena):
    esNum = True 
    for caracter in cadena:
        caracterStr = str(caracter)
    if caracterStr < '0' and caracterStr > '9':
        esNum = False
    return esNum

# PARA CARACTERES ESPECIFICOS

def esLetra(caracter):
    esLetr = False 
    for caracter in str(caracter):
        caracterStr = str(caracter)
    if caracterStr >= 'a' and caracterStr <= 'Z':
        esLetr = True
    return esLetr
    
def esMinuscula(caracter):
    esMin = False 
    caracterStr = str(caracter)
    if caracterStr >= 'a' and caracterStr <= 'z':
        esMin = True
    return esMin

def esMayuscula(caracter):
    esMayus = False 
    caracterStr = str(caracter)
    if caracterStr >= 'A' and caracterStr <= 'Z':
        esMayus = True
    return esMayus

def esNumero(caracter):
    esNum = False 
    caracterStr = str(caracter)
    if caracterStr >= '0' and caracterStr <= '9':
        esNum = True
    return esNum

# EJERCICIO PARA CONTAR NUMERO DE MAYUSCULAS, MINUSCULAS Y NUMEROS DENTRO DE UNA PALABRA / CADENA / STRING

cadena = input("Dime una palabra: ")

contMayus = 0
contMinus = 0
contNum = 0

for caracter in cadena:
    if esMayuscula(caracter) == True:
        contMayus += 1
    if esMinuscula(caracter) == True:
        contMinus += 1
    if esNumero(caracter) == True:
        contNum += 1   
           
print(f"Hay {contMayus} mayusculas\nHay {contMinus} minusculas\nHay {contNum} numeros")
    