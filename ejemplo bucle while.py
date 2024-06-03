############### Ejemplo de bucle while y contador con control de flujo continue

contador = 0
while contador < 5:
    contador = contador + 1
    if contador == 3:
        print("se omite la iteración cuando contador es 3.")
        continue   # salta las lineas que siguen dentro de la iteración
    print("Iteración:", contador)
    print("-----------------------")
    print("***********************")
    
    print("el contador ha llegado a ser:",contador)
    
print("fin del bucle")


############### Ejemplo de bucle while y contador con control de flujo break

contador = 0
while contador < 5:
    contador = contador + 1
    if contador == 3:
        print("se omite la iteración cuando contador es 3.")
        break   # sale del bucle
    print("Iteración:", contador)
    print("-----------------------")
    print("***********************")
    
    print("el contador ha llegado a ser:",contador)
    
print("fin del bucle")
