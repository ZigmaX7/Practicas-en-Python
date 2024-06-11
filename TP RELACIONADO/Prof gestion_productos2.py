#variables, condicionales, ciclos, validaciones, interfaz, listas

lista_productos = []

def agregar_producto():
    producto = input("ingrese el nombre producto: ")
    lista_productos.append(producto)
    
def listar_producto():
    print(lista_productos)  
      
def eliminar_producto():
    producto = input("ingresa el nombre del producto que deseas eliminar: ")
    lista_productos.remove(producto)
    
def modificar_producto():
    producto = input(" ingrese al nombre del producto que deseas modificar: ")
        
def ingresar_opcion():
   validacion = False
   while validacion == False:
       opcion = int(input("1. agregar producto, 2.eliminar producto, 3.listar producto,  4. modificar producto, 5. salir : "))
       if opcion >= 1 and opcion <= 5:
           validacion = True 
   return opcion   
        
def menu():
    continuar = True
    while continuar == True:
        opcion = ingresar_opcion()    
        match opcion:
            case 1: agregar_producto()
            case 2: eliminar_producto()
            case 3: listar_producto()
            case 4: modificar_producto()
            case 5: continuar = False    

def gestion_productos():
    menu()
    
#llamar a la funcion que hace la gestion de productos
gestion_productos()