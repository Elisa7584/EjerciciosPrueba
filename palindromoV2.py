frase = "Isaac no ronca asi"
fraseSinEspacios = ""
esPalindromo = True

for letra in frase:
    if letra > 'a' and letra < 'Z':
        fraseSinEspacios += letra.lower()
 
for pos in range(len(fraseSinEspacios)):
    if fraseSinEspacios[pos] != fraseSinEspacios[-pos - 1]:
        esPalindromo = False

if esPalindromo == True:
    print("Si es un palindromo")