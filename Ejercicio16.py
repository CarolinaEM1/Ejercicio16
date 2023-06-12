#Menu interactivo
saldo = 1000

while True:
    print("\t. :Menú:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir ")

    opcion = int(input("Digite una opción del menú"))
    print()

    if opcion == 1:
        extra = float(input("¿Cuánto dinero desea ingresar? "))
        saldo += extra
        print(f"Dinero de la cuenta: {saldo}")
    elif opcion == 2:
        retirar = float(input("Cuánto dinero desea retirar-> "))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero de la cuenta: {saldo}")
    elif opcion == 3:
        print(f"Dinero de la cuenta: {saldo}")
    elif opcion == 4:
        print("Gracias por utilizar su cajero automático")
        break
    else:
        print("Opcion incorrecta, por favor digite una del 1 al 4")

        print()



#Carolina EM
