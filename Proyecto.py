def calcularPropiedades(contFelicidad,contSaciedad,contCacas,contPesoTamago,estaEnfermo):
    felicidad = "❤️"
    saciedad = "🍙"
    cacas = "💩"
    sano = "😀"
    enfermo = "🤮"
    peso = "⚖️"
    print(f"Felicidad: {felicidad*contFelicidad}")
    print(f"Saciedad: {saciedad*contSaciedad}")
    print(f"Nivel Cacas: {cacas*contCacas}")
    print(f"Peso: {peso*contPesoTamago}")
    if estaEnfermo == True:
        print(f"Está enfermo {enfermo}")
    elif estaEnfermo == False: 
        print(f"Está sano {sano}")
        

contFelicidad = 0
contSaciedad = 0
contCacas = 0
contPesoTamago = 1
tiempo = 0
estaEnfermo = False

calcularPropiedades(contFelicidad,contSaciedad,contCacas,contPesoTamago,estaEnfermo)

nombreTamago = input("Introduce el nombre de tu STEMgotchi: ")
    
while len(nombreTamago) > 5:
        nombreTamago = input("Lo siento, el nombre no puede tener más de cinco letras, vuelve a repetirlo: ")
        
bucle = True

while bucle == True:
    
    elegirSeccion = input("\nElige la opción deseada:\n  1 - Comer\n  2 - Jugar\n  3 - Limpiar caca:\n  4 - Curar:\n")

    # COMPROBAR QUE INTRODUCE UNA OPCION CORRECTA

    if elegirSeccion not in ["1","2","3","4"]:
        print("Opcion incorrecta")
    else:
        # OPCION COMER 
        if elegirSeccion == "1" and contCacas == 0:
            
            elegirOpcionComida = input("Elige que tipo de comida quieres:\n  1 - Comida salada\n  2 - Comida dulce\n")
            
            if elegirOpcionComida == "1":
                if contCacas > 0:
                    print("No puedes comer, ¡hay cacas!")
                elif contSaciedad < 4:
                    contSaciedad += 1  
            elif elegirOpcionComida == "2":
                if contSaciedad < 4:
                    contSaciedad += 1  
                if contFelicidad < 4: 
                    contFelicidad += 1 
                contPesoTamago += 2
                if contPesoTamago > 99:
                    contPesoTamago = 99    
            tiempo += 1
           
        # OPCION JUGAR
        if elegirSeccion == "2" and contCacas < 4:
            
            if contFelicidad < 4:
                contFelicidad += 1
            if contSaciedad > 0:
                contSaciedad -= 1
            if contPesoTamago > 1:
                contPesoTamago -= 1
                
            tiempo += 1
        elif elegirSeccion == "2" and contCacas >= 4:
            print("No puedes jugar, hay demasiadas cacas")
            
        # OPCION LIMPIAR CACAS
        if elegirSeccion == "3":
            contCacas = 0
            
        #CURAR
        if estaEnfermo == True and contCacas == 0:
            estaEnfermo = False
        else:
            if estaEnfermo == False:
                print("No puedes curarle, porque no está malo")
            if contCacas > 0:
                print("No puedes curarle, ya que hay cacas")
        
        # TERMINAR 3 TIEMPOS
        if tiempo == 3:
            tiempo = 0
            
            if contCacas < 6:
                contCacas += 1
            if contFelicidad > 4:
                contFelicidad -= 1
            if contCacas == 3:
                estaEnfermo = True
        
        calcularPropiedades(contFelicidad,contSaciedad,contCacas,contPesoTamago,estaEnfermo)