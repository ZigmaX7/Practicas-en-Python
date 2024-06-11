# gestion de los productos: agregar, modificar, eliminar, listar, buscar
# guardar en un archivo
lista_productos = []

def agregar_producto():
    producto = input("ingresa un producto")
    lista_productos.append(producto) 

def listar_productos():
    print(lista_productos)   

def eliminar_producto():
    producto_a_eliminar = input("ingresa el producto que deseas eliminar")
    lista_productos.remove(producto_a_eliminar)
   
def modificar_producto():
    producto_a_modificar=  input("ingresa el producto a modificar")
    producto_moficado = input("ingresa el producto con el texto modificado")
    posicion = lista_productos.indexOf(producto_a_modificar)
    lista_productos[posicion] = producto_moficado
    
    
def buscar_producto():
    producto_a_buscar = input(" ingrese el producto a buscar")
    posicion = lista_productos.indexOf(producto_a_buscar)
    if posicion > 0:
        print("el producto existe")
    else: 
        print("el producto no existe")
            

def opciones_menu():
    opcion_valida= False
    while opcion_valida == False:
        opcion = int(input("1. agregar_producto, 2. eliminar_producto, 3.modificar_producto..."))
        if opcion >=1 and opcion <=6:
            opcion_valida = True
        else: 
            print("ingresaste una opcion invalida, volve a intentarlo..")    
    return opcion

def menu():
    continuar = True
    while continuar == True:
        opcion = opciones_menu()
        match opcion:
            case 1: agregar_producto()
            case 2: eliminar_producto()
            case 3: modificar_producto()
            case 4: buscar_producto()
            case 5: listar_productos()
            case 6: continuar = False
            

def gestion_productos():
    menu()

gestion_productos() 

   
    





