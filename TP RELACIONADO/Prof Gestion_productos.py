# gestion de productos: alta , baja , modificacion, elminar, listar
lista_productos = []

def ingresar_producto():
    producto= input("ingrese el producto: ")
    lista_productos.append(producto)

def eliminar_producto():
    producto = input("ingresa el nombre del producto que deseas eliminar")
    lista_productos.remove(producto)
    
def listar_producto():
    print(lista_productos)
    
def actualizar_producto():
    producto = input("ingrese el producto que desea modificar")
    posicion = lista_productos.index(producto)
    lista_productos[posicion] = "PAN"    

def menu():
    opcion = -1 # opcion invalida
    
    while opcion == -1:
        opcion = int(input("""
                           1. ingrese producto
                           2. borrar el producto
                           3. actualizar producto
                           4. listar
                           5. salir
                            """))
        if opcion != 1 and opcion !=2 and opcion !=3 and opcion !=4 and opcion!=5:
            print("ingreso opcion invalida, intentelo nuevamente ....")
            opcion = -1
    return opcion

def gestion_productos():
    salir = False
    
    while salir == False:
        opcion = menu()
        match opcion:
            case 1: ingresar_producto()
            case 2: eliminar_producto()
            case 3: actualizar_producto()
            case 4: listar_producto()
            case 5: salir=True
    
gestion_productos()    
    