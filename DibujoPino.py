def patronFila(simbolo,ancho):
    return  simbolo*ancho 

def dibujarCuadrado(simbolo,ancho,alto):
    dibujo = ""
    for fila in range(alto):
        dibujo += patronFila(simbolo,ancho)
        dibujo +=  "\n"
    return dibujo

def dibujarCuadradoDos(simbolo,simbolo2,ancho,alto):
    dibujo = ""
    for fila in range(alto):
        dibujo += patronFila(simbolo,ancho)
        dibujo +=  "\n"
        dibujo += patronFila(simbolo2,ancho)
        dibujo +=  "\n"
    return dibujo

def dibujarLateralDerecho(simbolo,ancho,alto):
    dibujo = ""
    patron = ""
    for fila in range(alto):
        dibujo += patron
        patron += patronFila(simbolo,ancho)
        dibujo +=  "\n"
    return dibujo

def dibujarLateralIzquierdo(simbolo,altura):
    dibujo = ""
    for fila in range(altura):
        patron = patronFila(" ",altura-(fila+1)) + patronFila(simbolo,fila+1)
        dibujo += patron + "\n"
        print(f"El dibujo con {fila+1} filas: \n{dibujo}")
    return dibujo
def piramide(simbolo,altura):
    dibujo = ""
    patron = "X"
    for fila in range(altura):
        dibujo += patronFila(" ",altura-(fila+1)) + patron
        dibujo += "\n"
        print(f"El dibujo con {fila+1} filas: \n{dibujo}")
        patron += simbolo*2
    return dibujo
def dibujarForma(alto,ancho):

    for i in range(alto):
        if i == 0 or i == ancho - 1:
            print('X' * ancho)
        else:
            print('X' + ' ' * (ancho - 2) + 'X')
def dibujarPiramideSeparada(alto):

    for i in range(alto):
        espacios = " " * (alto - i - 1)
        x = "X" + "  X" * i
        print(espacios + x)


     
simbolo = input("Introduce el simbolo que quieres utilizar: ")
simbolo2 = input("Introduce el segundo simbolo que quieres utilizar: ")
ancho = int(input("¿Cuánto quieres que mida el simbolo de ancho?: "))
alto = int(input("¿Cuánto quieres que mida el simbolo de alto?: "))

patronFila(simbolo,ancho)
print(dibujarCuadrado(simbolo,ancho,alto))
print(dibujarCuadradoDos(simbolo,simbolo2,ancho,alto))
print(dibujarLateralDerecho(simbolo,alto,ancho))
print(dibujarLateralIzquierdo(simbolo,alto))
print(piramide(simbolo,alto))
dibujarForma(alto,ancho)
dibujarPiramideSeparada(alto)