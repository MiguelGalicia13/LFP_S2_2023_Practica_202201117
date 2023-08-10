from tkinter import Tk
from tkinter.filedialog import askopenfilename
inventario = []
def menu():
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
                Tk().withdraw() #! Abre un explorador de Archivos
                #! Extensiones de archivos permitidas
                extensiones = [("Archivo INV", "*.inv")]
                #! Filtro para encontrar solo archivos con extension .inv
                filename = askopenfilename(filetypes=extensiones)
                if filename:
                    with open(filename, 'r') as archivo:
                        print("Creando productos")
                        for linea in archivo:
                            if linea.startswith("crear_producto "):
                                linea = linea[len("crear_producto "):]  #! elimina la palbara "crear_producto "
                            datos_producto = linea.strip().split(';')
                            producto = {
                                'nombre': datos_producto[0],
                                'cantidad': int(datos_producto[1]),
                                'precio_unitario': float(datos_producto[2]),
                                'ubicacion': datos_producto[3]
                            }
                            inventario.append(producto)
                    print("Inventario creado exitosamente.")
                else:
                    print("No se seleccionó ningún archivo.")
                print("------------------------------------")
                print("Volviendo al menu.")
                print("------------------------------------")
                menu()
            case 2:
                #? Cargar instrucciones de movimiento
                print("Cargar instrucciones de movimiento")
                Tk().withdraw() #! Abre un explorador de Archivos
                #! Extensiones de archivos permitidas
                extensiones = [("Archivo MOV", "*.mov")]
                #! Filtro para encontrar solo archivos con extension .mov
                filename = askopenfilename(filetypes=extensiones)
                if filename:
                    with open(filename, 'r') as archivo:
                        print("Creando productos")
                        for linea in archivo:
                            if linea.startswith("agregar_stock"):
                                linea = linea[len("agregar_stock "):]
                                datos_producto = linea.strip().split(';')
                                producto = {
                                    'nombre': datos_producto[0],
                                    'cantidad': int(datos_producto[1]),
                                    'ubicacion': datos_producto[2]
                                }
                                #? Si el producto no existe en el inventario se agrega, pero si existe se suma la cantidad
                                for i in range(len(inventario)):
                                    if inventario[i]['nombre'] == producto['nombre'] and inventario[i]['ubicacion'] == producto['ubicacion']:
                                        inventario[i]['cantidad'] += producto['cantidad']
                                    else:
                                        inventario.append(producto)
                            if linea.startswith("vender_producto"):
                                linea = linea[len("vender_producto "):]
                                datos_producto = linea.strip().split(';')
                                producto = {
                                    'nombre': datos_producto[0],
                                    'cantidad': int(datos_producto[1]),
                                    'ubicacion': datos_producto[2]
                                }
                                #? Si el producto existe y se encuentra en la misma bodaga se resta la cantidad
                                for i in range(len(inventario)):
                                    if inventario[i]['nombre'] == producto['nombre'] and inventario[i]['ubicacion'] == producto['ubicacion']:
                                        inventario[i]['cantidad'] -= producto['cantidad']
                        
                else:
                    print("No se seleccionó ningún archivo.")
                print("------------------------------------")
                menu()
            case 3:
                #? Crear informe de inventario
                print("Crear informe de inventario")
                try:
                    with open("FP_S2_2023_Practica_202201117/Archivos/inventario.txt", "w+") as archivo:
                        inventario.sort(key=lambda producto: producto['nombre']) #? Motodo sort para ordenar alfabeticamente los articulos
                        for producto in inventario:
                            archivo.write(f"Nombre: {producto['nombre']} - Cantidad: {producto['cantidad']} - Precio: Q{producto['precio_unitario']} - Valor Total: Q{(round(producto['cantidad']*producto['precio_unitario'],2))}- Ubicacion: {producto['ubicacion']}\n")
                except Exception as e:
                    print("Error al crear el archivo",e)
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



print("---------------------------------------------------")
print("Practica 1 - Lenguajes formales y programacion")
print("---------------------------------------------------")
menu()