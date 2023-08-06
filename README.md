# Manual de Usuario #
## LFP_S2_2023_Practica_202201117 ##
### Archivo main.py ###
Al ejecutar el programa, se muestra un menú principal con cuatro opciones: "Cargar inventario inicial", "Cargar instrucciones de movimiento", "Crear informe de inventario" y "Salir". El usuario puede seleccionar una opción ingresando el número correspondiente.

La primera opción, "Cargar inventario inicial", permite al usuario seleccionar un archivo ".inv" utilizando un explorador de archivos. Si se elige un archivo válido, el programa lee cada línea y crea productos en base a los datos proporcionados. Para cada línea, se elimina la palabra "crear_producto " al inicio antes de procesar los datos. Los productos creados se almacenan en una lista llamada "inventario". Después de cargar el inventario, se muestra un mensaje de éxito y se regresa al menú principal.

La tercera opción, "Crear informe de inventario", muestra en pantalla los productos que se han cargado en el inventario hasta ese momento. Se imprimen los detalles de cada producto, incluyendo su nombre, cantidad, precio unitario y ubicación. Luego de mostrar el informe, el programa regresa al menú principal.

La cuarta opción, "Salir", muestra un mensaje de despedida y termina la ejecución del programa.

Si el usuario ingresa una opción inválida, el programa muestra un mensaje de error y solicita una nueva opción válida hasta que el usuario proporcione una opción correcta.
