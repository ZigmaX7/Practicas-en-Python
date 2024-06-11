#ejemplo de listas son variables cno multiples valores

primer_lista = [] # lista vacia
lista_numeros = [1]
lista_numeros1 = [1,2,3,4,5,6,7,8]
lista_mascotas = ["luna","manolo", "lucy"]

#mostrar información almancenada en listas.

print(lista_numeros1)  # muestra toda la totalidad de valores contenidos.

print(lista_mascotas[0]) # muestra un elemento selecto de la lista.

#agregar elementos en listas

lista_mascotas.append("berni") #agrega nuevo valor al final de la lista.

lista_mascotas.insert(0,"felipe") # inserta nuevo valor en posición selecionada sobreescribiendo valor anterior en caso de existir.


# quitar elementos en listas

lista_mascotas.remove("lucy")  # remueve elemento guardado según su valor "lucy", busca la posición donde se aloja y lo elimina.

print(lista_mascotas)

lista_mascotas.pop(1) # elminina el elemento en la posición de la lista "1"

print(lista_mascotas)

# localizar en variable y posición y modificarlo mediante ciclo for

lista_alumnos = ["juan","pedro","laura","jorge","santiago","sebedeo","lucas"]

pos = 0

for alumno in lista_alumnos:
    if alumno == "lucas":
        lista_alumnos[pos] = "LUCAS"
    pos =+ 1

print(lista_alumnos)

