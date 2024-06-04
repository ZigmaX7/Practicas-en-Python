# gestion de producos : CRUD : agregar, modificar , eliminar, listar , buscar. 
  # guardar los datos en un archivo para persistencia de la información

lista_productos = []  	

def agregar_producto():
  producto = input("ingrese un producto.\n")
  lista_productos.append(producto)
  return
  
def eliminar_producto():
  producto_eliminar = input("ingrese un producto a eliminar.\n")
  for producto_eliminar in range (lista_productos):
    lista_productos.pop(producto_eliminar)
  return
    
def modificar_producto():
  producto_modificar = input("ingrese el producto que desea modificar.\n")
  productos_modificado = input("ignrese el producto con el texto modificado.\n")
  posicion =lista_productos.index(producto_modificar)
  lista_productos[posicion] = productos_modificado
  return

def buscar_producto():
  producto_buscar = input("ingrese el prodcuto a buscar.\n")
  posicion = lista_productos.index(producto_buscar)
  if posicion > 0 :
    print("producto encontrado.")
  else:
    print("el producto no existe.")
  return
  
def listar_producto():
  print(lista_productos)
  return

def opciones_menu(): 
  opcion_valida = False
  while opcion_valida == False:
    opcion = int(input("""                       
                          
                          1. Agregar producto.
                          2. Eliminar producto.
                          3. Modificar producto.
                          4. Buscar producto.
                          5. Listar productos.
                          6. Salir.
                          
                          Ingrese una opcion del menú:
                          
                          
                          """))    
    if opcion >= 1 and opcion <=6:
      opcion_valida = True
  return opcion

def menu():
  continuar = True
  while continuar == True:
      opcion = opciones_menu()
      match opcion:
          case 1: agregar_producto()
          case 2: elminar_producto()
          case 3: modificar_producto()
          case 4: buscar_producto()
          case 5: listar_producto()
          case 6: continuar = False
          case _: print("Opción inválida")
  return

def gestion_productos():
  menu()
  return

gestion_productos()