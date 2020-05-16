comprar = "s"

while comprar == "s":
    edad= int(input("introduce tu edad: "))
    if edad < 4:
        print("entra gratis!")
        tickets = entradas[0]
    elif  4 <= edad <= 18:
        print("el costo de la entrada es: 5 euros")
        tickets = entradas[1]
    else:
        print("El precio de la entrada es 10 euros")
        tickets = entradas[2]
    comprar = str(input("¿Desea comprar otra entrada? s/n"))
    if comprar == "n":
        print("¡Hasta luego!")
        break
