def calcular_mcd(n):
    print("asdf")

def cadena_repetida_n(p = "", v = 0):
    p = input("Ingrese la palabra: ")
    v = int(input("Ingrese las veces: "))
    for i in range(v):
        print(p)
    print("------------------------------------------")
    if v >= 0:
        return 1
    else:
        cadena_repetida_n(v - 1)
        print(cadena_repetida_n(p))

def contar_letra(n):
    print("asdf")

def convertir_numero_binario(n):
    print("asdf")

def digitos_numero(n):
    print("asdf")

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
            calcular_mcd()
        case 2:
            cadena_repetida_n()
        case 3:
            contar_letra()
        case 4:
            convertir_numero_binario()
        case 5:
            digitos_numero()
        case 6:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")