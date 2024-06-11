# Elegir la temática de la aplicación.
# CRUD: CREAR , MODIFICAR, ELIMINAR, LISTAR, BUSCAR
# FUNCION DEL MENU PARA INTERACCIÓN DE USUARIOS
# QUE ESTRUCTURA DE DATOS UTILIZARÉ Y QUE TIPO DE ALMACENAMIENTO DE DATOS EN ARCHIVO.

import json

lista_usuarios = []
lista_articulos = []

def cargar_usuarios():
    try:
        with open("usuarios.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def guardar_usuarios(lista_usuarios):
    with open("usuarios.json",'w') as file:
        json.dump(lista_usuarios,file)   

def cargar_articulos():
    try:
        with open("articulos.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def guardar_articulos(lista_articulos):
    with open("articulos.json",'w') as file:
        json.dump(lista_articulos,file)   

def alta_de_usuario(username, nombre, email ):
    # json con los datos de los productos
    nuevo_usuario = {
        'id': len(lista_usuarios) + 1,
        'username': username ,
        'nombre':nombre,
        'email': email        
    }    
    lista_usuarios.append(nuevo_usuario)
    guardar_usuarios(lista_usuarios)
    return nuevo_usuario

def crear_usuario():

    username = input("Ingrese el nombre de usuario: ")
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el email: ")
    usuario = alta_de_usuario(username,nombre,email)
    return usuario
  
def leer_usuarios():
    return cargar_usuarios()


def modificar_usuario():

    return
def eliminar_usuario():

    return
def listar_usuarios():

    return
def buscar_usuario():

    return

def crear_articulo():

    return
def modificar_articulo():
    return

def eliminar_articulo():
    return

def listar_articulos():
    return



def buscar_articulo():

    return

def ingresar_opcion():
    validacion = False
    while validacion == False:
       opcion = int(input("""
                                1. crear usuario
                                2. modificar usuario
                                3. eliminar usuario
                                4. listar usuarios
                                5. buscar usuario
                                6. crear articulo
                                7. modificar articulo
                                8. eliminar articulo
                                9. listar articulos
                                10. Salir 
                          """))
       if opcion >= 1 and opcion <= 5:
           validacion = True 
    return opcion


def menu_principal():
    continuar = True
    while continuar == True:
        opcion = ingresar_opcion()    
        match opcion:
            case 1: crear_usuario()
            case 2: modificar_usuario()
            case 3: eliminar_usuario()
            case 4: listar_usuarios()
            case 5: buscar_usuario()
            case 6: crear_articulo()
            case 7: modificar_articulo()
            case 8: eliminar_articulo()
            case 9: listar_articulos()
            case 10: continuar = False

menu_principal()
    






