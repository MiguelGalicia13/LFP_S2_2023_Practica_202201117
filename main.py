def menu():
    print("---------------------------------------------------")
    print("Practica 1 - Lenguajes formales y programacion")
    print("---------------------------------------------------")
    print("# Sistema de inventario:")
    print("")
    print()
    print("1. Cargar inventario inicial")
    print("2. Cargar instrucciones de movimiento")
    print("3. Crear informe de inventario")
    print("4. Salir")
    print()
    print("ingrese una opcion: ", end="")
    while True:
        try:
            opcion = int(input())
        except ValueError:
            print("Opcion no valida ,intente de nuevo")
            opcion = int(input())
        match opcion:
            case 1:
                #? Cargar inventario
                print("Cargar inventario inicial")
                menu()
            case 2:
                #? Cargar instrucciones de movimiento
                print("Cargar instrucciones de movimiento")
                menu()
            case 3:
                #? Crear informe de inventario
                print("Crear informe de inventario")
                menu()
            case 4:
                #? Salir
                print("Saliendo del Programa...")
                return False          
            case _:
                print("Opcion no valida ,intente de nuevo")
                opcion = int(input())
        break
    return
menu()