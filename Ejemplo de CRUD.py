# gestion de productos

# se establece lista_productos como variable/lista global
lista_productos = []

def ingresar_producto():
    producto = input("ingrese el producto")
    lista_productos.append(producto)
    
    
# se crea el menu como funcion sin parámetros. para solicitar un ingreso de datos con bucle de verificación y capturar una opcion válida.
def menu():
    opcion = -1
    while opcion == -1:
        
        opcion = int
        opcion = int(input("""\
                                1. Ingresar nuevo producto.
                                2. Borrar producto existente.
                                3. Actualizar producto existente.
                                4. Listar productos existentes.
                                5. Salir               
                                                        """))
        if opcion != 1 and opcion !=2 and opcion != 3 and opcion !=4 and opcion !=5:
            print("opcion inválida, inténtelo nuevamente...")
            opcion = -1
    return opcion
    


# se utiliza la salida de la funcion menu para utilizarlo en otra funcion.

def eliminar_producto():
    producto = input("ingrese el nombre del producto que desea elmiinar\n")
    lista_productos.remove(producto)
    

def listar_producto():
    print(lista_productos)
    
    
def actualizar_producto():
    producto = input("ingrese el producto que desea modificar\n")
    posicion = lista_productos.index(producto)
    lista_productos[posicion] = input("ingrese la modificación de producto\n")


def gestion_productos():
    # se remueve de local para hacer global -->lista_productos = []
    
    salir = False # se configura una flag booleaan para siguiente bucle while.add(
    while salir == False:
        
        opcion = menu() # se cita la opción ingresada capturada en el menú anterior
    
    
        match opcion:
            case 1: ingresar_producto()
            case 2: eliminar_producto()
            case 3: actualizar_producto()
            case 4: listar_producto()
            case 5: salir = True
            
    # ingreso un producto y lo agrego a la lista.add(
    producto = ingresar_producto()
    
gestion_productos()
