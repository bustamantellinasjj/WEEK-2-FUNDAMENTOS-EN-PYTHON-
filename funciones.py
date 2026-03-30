# CREO LA LISTA DE INVENTARIO VACIA PARA ALMACENAR LOS PRODUCTOS.
inventario = []

# CREO FUNCIONES  PARA AGREGAR PRODCUTOS, MOSTRAR EL INVENTARIO Y CALCULAR ESTADÍSTICAS, PERO NO LAS UTILIZO EN EL PROGRAMA PRINCIPAL PARA MANTENERLO MÁS SIMPLE Y DIRECTO.
def agregar_producto():

    Volver_Preguntar = True
    while Volver_Preguntar: # BUCLE PARA PERMITIR AL USUARIO VOLVER A INGRESAR LOS DATOS SI COMETE UN ERROR.
        try:
            nombre_producto = input("\nINGRESE EL NOMBRE DEL PRODUCTO:") # (DATO1) SOLICITA AL USUARIO EL NOMBRE DEL PRODUCTO.
            if len(nombre_producto) > 20: # VALIDACIÓN PARA QUE EL NOMBRE NO EXCEDA LOS 20 CARACTERES.
                print("\nNOMBRE INVALIDO. MAXIMO 20 CARACTERES.") # MENSAJE DE ERROR PARA EL USUARIO.
                continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN NOMBRE VÁLIDO.
            else:
                Volver_Preguntar = False # SI EL NOMBRE ES VÁLIDO, SALE DEL BUCLE Y CONTINUA CON LA SOLICITUD DE LOS DEMÁS DATOS DEL PRODUCTO.
        except (ValueError, EOFError, KeyboardInterrupt): # SI EL USUARIO INTERRUMPE EL PROGRAMA CON CTRL+C, MUESTRA UN MENSAJE DE ERROR Y VUELVE A PREUNTAR EL NOMBRE DEL PRODUCTO.       
            print("\nINGRESA UN NOMBRE VALIDO.") # MENSAJE DE ERROR PARA EL USUARIO.
            continue
    
    Volver_Preguntar = True
    while Volver_Preguntar:
        try:
            precio_producto = float(input("\nINGRESE EL PRECIO DEL PRODUCTO:")) # (DATO2) SOLICITA AL USUARIO EL PRECIO DEL PRODUCTO.
            if precio_producto < 0: # VALIDACIÓN PARA QUE EL PRECIO NO SEA NEGATIVO.
                print("\nPRECIO INVALIDO. NO PUEDE SER NEGATIVO.") # MENSAJE DE ERROR PARA EL USUARIO.
                continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UN PRECIO VÁLIDO.
            else:
                Volver_Preguntar = False # SI EL NOMBRE ES VÁLIDO, SALE DEL BUCLE Y CONTINUA CON LA SOLICITUD DE LOS DEMÁS DATOS DEL PRODUCTO.
        except (ValueError, EOFError, KeyboardInterrupt): # SI EL USUARIO INTERRUMPE EL PROGRAMA CON CTRL+C, MUESTRA UN MENSAJE DE ERROR Y VUELVE A PREUNTAR EL PRECIO DEL PRODUCTO.       
            print("\nINGRESA UN PRECIO VALIDO.") # MENSAJE DE ERROR PARA EL USUARIO.
            continue

    Volver_Preguntar = True
    while Volver_Preguntar:
        try:
            cantidad_producto = int(input("\nINGRESE LA CANTIDAD DEL PRODUCTO:")) # (DATO3) SOLICITA AL USUARIO LA CANTIDAD DEL PRODUCTO.
            if cantidad_producto < 0: # VALIDACIÓN PARA QUE LA CANTIDAD NO SEA NEGATIVA.
                print("\nCANTIDAD INVALIDA. NO PUEDE SER NEGATIVA.") # MENSAJE DE ERROR PARA EL USUARIO.
                continue # VUELVE A MOSTRAR EL MENÚ PARA QUE EL USUARIO PUEDA INGRESAR UNA CANTIDAD VÁLIDA.
            else:
                Volver_Preguntar = False # SI LA CANTIDAD ES VÁLIDA, SALE DEL BUCLE Y CONTINUA CON LA SOLICITUD DE LOS DEMÁS DATOS DEL PRODUCTO.
        except (ValueError, EOFError, KeyboardInterrupt): # SI EL USUARIO INTERRUMPE EL PROGRAMA CON CTRL+C, MUESTRA UN MENSAJE DE ERROR Y VUELVE A PREUNTAR LA CANTIDAD DEL PRODUCTO.
            print("\nINGRESA UNA CANTIDAD VALIDA.") # MENSAJE DE ERROR PARA EL USUARIO.
            continue

    producto = { # CREA UN DICCIONARIO PARA ALMACENAR LOS DETALLES DEL PRODUCTO.
        "nombre": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto
    }
    inventario.append(producto) # AGREGA EL PRODUCTO AL INVENTARIO.
    print(f"\nEL PRODUCTO: {nombre_producto}, FUE AGREGADO EXITOSAMENTE.")


def mostrar_inventario():
    if len(inventario) == 0: # SI EL INVENTARIO ESTÁ VACÍO, MUESTRA UN MENSAJE AL USUARIO.
        print("\nEL INVENTARIO ESTÁ VACÍO.") # MENSAJE PARA EL USUARIO.
    else:
        print("\n||||| INVENTARIO ACTUAL |||||") # ENCABEZADO PARA MOSTRAR EL INVENTARIO AL USUARIO.
        for i, producto in enumerate(inventario, start=1): # enumerate ME DA DOS COSAS A LA VEZ: EL ÍNDICE (i) Y EL ELEMENTO (producto) DE LA LISTA DE INVENTARIO, COMENZANDO EL ÍNDICE EN 1 (start=1).
            print(f"\nPRODUCTO {i}:") # MUESTRA EL NÚMERO DEL PRODUCTO EN EL INVENTARIO.
            print(f"NOMBRE: {producto['nombre']}") # ACCEDE A LA LLAVE 'nombre' DEL DICCIONARIO.
            print(f"PRECIO: ${producto['precio']:.2f}") # :.2f FORMATEA EL PRECIO A 2 DECIMALES y ACCEDE A LA LLAVE 'precio' DEL DICCIONARIO.
            print(f"CANTIDAD: {producto['cantidad']}") # ACCEDE A LA LLAVE 'cantidad' DEL DICCIONARIO.

def calcular_estadisticas():
    total = 0
    cantidad_total = 0
    for producto in inventario: # RECORRE CADA PRODUCTO EN EL INVENTARIO PARA CALCULAR EL VALOR TOTAL DEL INVENTARIO Y LA CANTIDAD TOTAL DE PRODUCTOS.
        total += producto['precio'] * producto['cantidad'] # CALCULA EL VALOR DE CADA PRODUCTO MULTIPLICANDO SU PRECIO POR SU CANTIDAD Y LO SUMA AL TOTAL.
        cantidad_total += producto['cantidad'] # SUMA LA CANTIDAD DE CADA PRODUCTO AL TOTAL DE CANTIDAD.
    print(f"\nVALOR TOTAL DEL INVENTARIO: ${total:.2f}") # MUESTRA EL VALOR TOTAL DEL INVENTARIO FORMATEADO A 2 DECIMALES.
    print(f"CANTIDAD TOTAL DE PRODUCTOS: {cantidad_total}") # MUESTRA LA CANTIDAD TOTAL DE PRODUCTOS EN EL INVENTARIO.