#proyecto debe tener listas, ciclos, condicionales, interfaz gráfica, CRUD, buscador.
# prductos tendran ID , NOMBRE , PRECIO , CANTIDAD como sus valores.
# la información de productos se almacenará en archivo productos.json
import os
import json

##  FUNCIONES DE MANEJO DE PERSISTENCIA DE DATOS

def cargar_articulos():
    try:
        with open('PATH_FILE','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
    
def guardar_articulos(lista_articulos):
    with open ('PATH_FILE', 'w') as file:
        json.dump(lista_articulos,file)

# DEFINICION DE LISTA Y PATH DE ARCHIVO JSON

lista_articulos = []

PATH_FILE = "D:/Users/Sigma/Desktop/CODO A CODO 4.0 INICIAL/Ejercicios Python/artículos_kb.json"


## FUNCIONES DE MANEJO DE ARTICULOS CRUD

def crear_articulo(titulo_articulo,descripcion_articulo,cuerpo_articulo):
    lista_articulos = cargar_articulos()
    nuevo_articulo = {
        'id': len(lista_articulos) + 1,
        'titulo': titulo_articulo,
        'descripcion':  descripcion_articulo,
        'cuerpo': cuerpo_articulo
                     }
    
    lista_articulos.append(nuevo_articulo)
    guardar_articulos(lista_articulos)
    return nuevo_articulo

def modificar_articulo(id,titulo_articulo,descripcion_articulo,cuerpo_articulo):
    lista_articulos = cargar_articulos()
    lista_articulos.sort()

    guardar_articulos(lista_articulos)

def main_menu():
    #falta agregar validación de datos en ciclo.
    
    print("""
    
            Base de Conocimientos
          
            1. Crear nuevo artículo
            2. Modifcar artículo
            3. Quitar artículo
            4. Importar artículo desde archivo de texto
            5. Listado de artículos
            6. Buscar un artículo
            7. Salir.
            
                """) 
    opcion = int(input("ingrese la opción a realizar.\n"))
    
    return opcion

def main():
    
    continuar = True
    while continuar == True:
        
        opcion = main_menu()
        
        match opcion:   # solicitar datos producto
            case 1: 
                while True:
                    try:            
                        titulo_articulo = str(input("ingrese el Título del artículo.\n"))
                        descripcion_articulo = str(input("ingrese una descripción del artículo.\n"))
                        cuerpo_articulo = str(input("ingrese el cuerpo del artículo.\n"))
                        articulo = crear_articulo(titulo_articulo,descripcion_articulo,cuerpo_articulo)
                        return print("articulo creado",articulo)
                        break 
                    except ValueError:
                        print("ingreso inválido, intente nuevamente")
            case 2:    
            case 3:
            case 4:
            case 5:
            case 6:
            case 7: continuar = false
    return

main()