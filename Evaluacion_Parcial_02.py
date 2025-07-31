opciones = 0
a = False
while a == False:
    print("---Menu---")
    print("1. Calcular el MCD de dos numeros")
    print("2. Crear una cadena repetida N veces")
    print("3. Contar cuantas veces aparece una letra en una cadena")
    print("4. Convertir un numero decimal a binario")
    print("5. Calcular cuantos digitos tiene un numero")
    print("6. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")