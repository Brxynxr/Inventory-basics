# Preguntamos al usuario si quiere iniciar el registro
registrarP = input("desea registrar un producto?: yes/no ")

# El bucle se ejecutará mientras la respuesta sea "yes"
while registrarP == "yes":
    nombre = input("ingrese nombre del producto: ")
    
    precio = None
    while precio == None:
        try:
            precio = float(input("ingrese precio del producto: "))
        except ValueError:
            print("Error: informacion invalida")
          
    cantidad = None
    while cantidad == None:
        try:
            cantidad = int(input("ingrese cantidad de unidades: "))
        except ValueError:
            print("Error: informacion invalida")

    # Calculamos el costo total multiplicando precio por cantidad
    costo_total = precio * cantidad

    # Mostramos el resumen ordenado
    print("PRODUCTO REGISTRADO".center(64, "-"))
    print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | total: {costo_total}")
    print("-" * 64)
   
    # Preguntamos si se desea continuar para decidir si el bucle se repite o termina
    registrarP = input("desea registrar otro producto?: yes/no ")
   
print("Registro Finalizado")

"""
-----FUNCION DEL PROGRAMA-----
 - Este programa le pide al usuario el nombre, precio y cantidad de un producto.
 - Valida que el precio y la cantidad sean números correctos antes de usarlos.
 - Luego calcula el costo total y muestra todo en pantalla de forma ordenada.
 - Se puede repetir el proceso para registrar varios productos seguidos.
"""
