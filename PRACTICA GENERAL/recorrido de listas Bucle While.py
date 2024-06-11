palabras = ["manzana","banana","pera","chorroarin","buken","hadooken","repercuten","chukruten","fin","fatallity"]
contador = 0
i = 0

while i < len(palabras):
    if palabras[i] == "fin":
        print("Se encontró la palabras fin. Deteniendo el lanzamiento nuclear")
        break
    if len(palabras[i]) > 5:
        contador += 1
    i +=1

print(f"Número de palabras con más de 5 letras = {contador}")
        