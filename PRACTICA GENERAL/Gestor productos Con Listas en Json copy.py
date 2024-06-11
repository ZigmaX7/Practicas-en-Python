#proyecto debe tener listas, ciclos, condicionales, interfaz gráfica, CRUD, buscador.
# prductos tendran ID , NOMBRE , PRECIO , CANTIDAD como sus valores.
# la información de productos se almacenará en archivo productos.json

import json

lista_productos = []

PATH_FILE = "D:/Users/Sigma/Desktop/CODO A CODO 4.0 INICIAL/Ejercicios Python/productos.json"

def menu():
    #falta agregar validación de datos en ciclo.
    
    print("""
    
            CRUD de Productos
            1. Crear Producto
            2. Modifcar Producto
            3. Quitar Producto
            4. Listado de Productos
            5. Buscar un Producto
            6. Salir.
            
                """) 
    opcion = int(input("ingrese la opción a realizar.\n"))
    
    return opcion

def cargar_productos():
    try:
        with open('PATH_FILE','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_productos(lista_productos):
    with open ('PATH_FILE', 'w') as file:
        json.dump(lista_productos,file)

def buscar_productos(id):
    lista_productos = cargar_productos()
    for i in range (len((lista_productos)-1)):
        if lista_productos[i].id == id:
            return lista_productos[i]
    return("producto inexistente")
    

def crear_producto(nombre,precio,cantidad):
    lista_productos = cargar_productos() # trae desde el archivo toda la información que tenga.
    nuevo_producto = { 'id': len(lista_productos) + 1, 'nombre': nombre,'precio':  precio, 'cantidad': cantidad}
    
    lista_productos.append(nuevo_producto)
    guardar_productos(lista_productos)
    return nuevo_producto

def main():
    
    while True:
        
        opcion = menu()
        
        if opcion == 1:   # solicitar datos producto
            while true:
                try:            
                    nombre = str(input("ingrese el nombre del producto.\n"))
                    precio = float(input("ingrese el precio del producto.\n"))
                    cantidad = int(input("ingrese la cantidad del producto.\n"))
                    producto = crear_producto(nombre,precio,cantidad) # agrega a la lista y guarda en el archivo
                    print("usted ha creado el siguiente producto:\n",producto)
                    break 
                except ValueError:
                    print("ingreso inválido, intente nuevamente")
        if opcion == 2:    
            
            
        break
    return


main()