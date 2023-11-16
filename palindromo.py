#Palíndromo: Palabra o frase que se lee igual al derecho y al revés.
# Nos dan una frase, le damos la vuelta.
# Comprobar si realmente es un palíndromo. [OJO con los espacios]
# Ejemplos:
# Isaac no ronca asi.
# Sé verlas al revés.
# Amo la paloma.
# Anita lava la tina

listaFrase = ["Isaac", "no", "ronca", "asi"]
fraseSinEspacios =""
esPalindromo = True

for palabra in listaFrase:
    fraseSinEspacios += palabra.lower()
 
for pos in range(len(fraseSinEspacios)):
    if fraseSinEspacios[pos] != fraseSinEspacios[-pos - 1]:
        esPalindromo = False

if esPalindromo == True:
    print("Si es un palindromo")