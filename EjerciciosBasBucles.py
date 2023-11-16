#Solicita por consola una hora, unos minutos y unos segundos. Vuelve a solicitar los datos en caso de no estar comprendidos entre los valores correctos

horas = int(input("Introduceme las horas: "))
minutos = int(input("Introduceme los minutos:"))
segundos = int(input("Introduceme los segundos:"))

tiempoValido = False


while tiempoValido == False: 
    print("Esos valores no son correctos,vuelve a repetir: ")
    
    horas = int(input("Introduceme las horas: "))
    minutos = int(input("Introduceme los minutos:"))
    segundos = int(input("Introduceme los segundos:"))
    
else:
    if horas <= 23 and minutos <= 59 and segundos <= 59:
        tiempoValido = True
    print(f"El tiempo que has introducido es correcto y es {horas} horas, {minutos} minutos, {segundos} segundos ")
    