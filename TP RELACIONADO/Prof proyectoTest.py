# no cambia
import json

# Archivo donde se guardarán los productos
# se debe modificar el nombre del archivo en funcion a lo que se va a guardar
FILE_PATH = 'productos.json'

# Función para cargar productos desde el archivo JSON
#no cambia, excepto el nombre de la funcion
def cargar_productos():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Función para guardar productos en el archivo JSON
# no cambia excepto el nombre la funcion
def guardar_productos(productos):
    with open(FILE_PATH, 'w') as file:
        json.dump(productos, file, indent=4)

# Crear un nuevo producto
def crear_producto(nombre, precio, cantidad):
    #trae los productos del archivo a la lista
    productos = cargar_productos()
    # crea un diccionario o json, como un elemento para agregar a la lista
    nuevo_producto = {
        'id': len(productos) + 1,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    # agrega a la lista el nuevo producto
    productos.append(nuevo_producto)
    # guarda la lista en el archivo
    guardar_productos(productos)
    return nuevo_producto

# Leer productos
def leer_productos():
    return cargar_productos()

# Actualizar un producto
def actualizar_producto(id, nombre=None, precio=None, cantidad=None):
    productos = cargar_productos()
    for producto in productos:
        if producto['id'] == id:
            if nombre is not None:
                producto['nombre'] = nombre
            if precio is not None:
                producto['precio'] = precio
            if cantidad is not None:
                producto['cantidad'] = cantidad
            guardar_productos(productos)
            return producto
    return None

# Eliminar un producto
def eliminar_producto(id):
    productos = cargar_productos()
    productos = [producto for producto in productos if producto['id'] != id]
    guardar_productos(productos)
    return productos

def buscar_producto(identificador):
     productos = cargar_productos()
     for i in len(productos)-1:
         if productos[i].id == identificador:
             return productos[i]          
     return("producto inexistente")    
     
    
# Funciones para la Interfaz de Línea de Comandos (CLI)
def menu():
    print("\nCRUD de Productos")
    print("1. Crear Producto")
    print("2. Leer Productos")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Buscar Producto")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        opcion = menu()
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            # agrega a la lista y guarda en el archivo
            producto = crear_producto(nombre, precio, cantidad) 
            print(f"Producto creado: {producto}")
        elif opcion == '2':
            productos = leer_productos()
            for producto in productos:
                print(producto)
        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            producto = actualizar_producto(id, nombre or None, float(precio) if precio else None, int(cantidad) if cantidad else None)
            if producto:
                print(f"Producto actualizado: {producto}")
            else:
                print("Producto no encontrado")
        elif opcion == '4':
            id = int(input("ID del producto a eliminar: "))
            productos = eliminar_producto(id)
            print(f"Producto eliminado. Productos restantes: {productos}")
        elif opcion == '5':
            id = int(input("ingresa el id que deseas encontrar"))
            producto = buscar_producto(id)
            print(producto)            
        elif opcion == '6':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# es el llamado a una funcion
main()
