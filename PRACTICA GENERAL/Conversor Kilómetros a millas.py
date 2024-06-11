def conver_km_a_milla(kilometros):
    millas = kilometros * 1.60934
    return millas

kilometros = float(input(" ingrese distancia en Kilómetros para convertir a Millas:\n"))
conversion = conver_km_a_milla(kilometros)
print("La distancia en Millas es:",conversion)