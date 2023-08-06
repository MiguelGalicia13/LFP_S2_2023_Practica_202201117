from tkinter import Tk
from tkinter.filedialog import askopenfilename
class cargar_inventario:
    def crear_inventario():
        Tk().withdraw() #! Abre un explorador de Archivos
        #! Extensiones de archivos permitidas
        extensiones = [("Archivo INV", "*.inv")]
        #! Filtro para encontrar solo archivos con extension .inv
        filename = askopenfilename(filetypes=extensiones)
        if filename:
            inventario = []
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
    
    #def mostrar_inventario(inventario):
        print("Inventario:")
        for producto in inventario:
            print(f"{producto['nombre']} - {producto['cantidad']} - {producto['precio_unitario']} - {producto['ubicacion']}")


