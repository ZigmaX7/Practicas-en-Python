# lista, ciclos, condicionales, interfaz grafica, funciones, match, 
# alta, modificacion, baja, listado, buscar
# id, nombre, precio, cantidad : 
# la informacion la vamos a almacenar en productos.json es un archivo
import json

lista_productos = []
PATH_FILE = 'productos.json'

def cargar_productos():
    try:
        with open(PATH_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
            
def guardar_productos(lista_productos):
    with open(PATH_FILE, 'w') as file:
        json.dump(lista_productos,file)


def menu():
    #falta agregar un ciclo que valide que la opcion ingresa es : 1,2,3,4,5,6, 
    # sino es asi -> pedir que ingrese nuevamente
    print("\nCRUD de Productos")
    print("1. Crear Producto")
    print("2. Modificar Producto")
    print("3. Quitar Producto")
    print("4. Listado de Productos")
    print("5. Buscar un Producto")
    print("6. Salir")
    opcion = int(input("Que opcion desea hacer?: ")) 
    return opcion

def crear_producto(nombre, precio,cantidad):
    lista_productos = cargar_productos()
    nuevo_producto = {
        'id': len(lista_productos) + 1,
        'nombre': nombre,
        'precio': precio ,  
        'cantidad': cantidad  
             
    }
    lista_productos.append(nuevo_producto)
    guardar_productos(lista_productos)
    return nuevo_producto  
    
def main():
    print("esta es la funcion principal")
    while True:
       opcion = menu()       
       if opcion == 1:
           nombre = input("Ingresa el nombre del producto: ")
           precio = float(input("Ingresa el precio del producto: "))
           cantidad = int(input(" Ingresa la cantidad del producto: "))
           producto = crear_producto(nombre, precio,cantidad)
           
# estoy llamando a una funcion, pero como esta en rojo la funcion no existe

main()