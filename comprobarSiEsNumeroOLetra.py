listaCaracteres = [0,1,2,'a','b','x','C',5,'3']

for caracter in listaCaracteres:
    caracterString = str(caracter)
    if caracterString >= 'a' and caracterString <= 'Z':
        print(f"{caracter} es una letra en general")
    if caracterString >= 'a' and caracterString <= 'z':
        print(f"{caracter} es una letra minuscula")
    if caracterString >= 'A' and caracterString <= 'Z':
        print(f"{caracter} es una letra mayuscula")
    if caracterString >= '0' and caracterString <= '9':
        print(f"{caracter} es un string numerico")