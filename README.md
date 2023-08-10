# Manual de Usuario #
## LFP_S2_2023_Practica_202201117 ##
### Archivo main.py ###
Al ejecutar el programa, se muestra un menú principal con cuatro opciones: "Cargar inventario inicial", "Cargar instrucciones de movimiento", "Crear informe de inventario" y "Salir". El usuario puede seleccionar una opción ingresando el número correspondiente.

#### Cargar inventario ####

La primera opción, "Cargar inventario inicial", permite al usuario seleccionar un archivo ".inv" utilizando un explorador de archivos. Si se elige un archivo válido, el programa lee cada línea y crea productos en base a los datos proporcionados. Para cada línea, se elimina la palabra "crear_producto " al inicio antes de procesar los datos. Los productos creados se almacenan en una lista llamada "inventario". Después de cargar el inventario, se muestra un mensaje de éxito y se regresa al menú principal.

#### Registrar movimientos ####

Para la segunda opcion donde se deben registrar las ventas o el agregar stock por medio de crear un diccionario llamado producto se agrega a la matriz de inventario principal que junto a un par de condicionales if-else se agregan si encierto caso se agrega stock, o se elimina la cantidad de productos si se realiza una venta, para elegir los archivos igual es manejo con un TK.withdraw que busca solo archivos .MOV en un seleccionador de archivos

#### Crear informe de inventario ####

La tercera opción, "Crear informe de inventario", se declara un archivo con el modelo de lectura w+ mas para que escriba y lea un archivo, y si en dado caso no existe este lo crea, posterior mente se crea un archivo txt con el modelo brindado en el enucido de la practica con los datos que se encuentran en la matriz inventario.

#### Salir ####
La cuarta opción, "Salir", muestra un mensaje de despedida y termina la ejecución del programa.

Si el usuario ingresa una opción inválida, el programa muestra un mensaje de error y solicita una nueva opción válida hasta que el usuario proporcione una opción correcta.
