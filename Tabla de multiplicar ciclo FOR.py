def tabla_multplicar_numero(num1):
        for i in range (1,11):
            print(f"{num1} x {i} = {num1 * i}")
        return


print("Bienvenido a su generador de tablas de multiplicar.")
print("")
num1= int(input("Ingrese el número a operar.\n"))
print("")
i=1
tabla_multplicar_numero(num1)







