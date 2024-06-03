# ejemplo basico de funcion


def sum1(num1,num2):
    return num1+num2

resultado = sum1(20,40)
print(resultado)


####################

print("""\
    
    
    """)

############### Ejemplo de variable local vs variable global

resultado = 20  # es global

def sum(num1,num2):
    resultado = num1+num2   # resultado es variable local
    return resultado

print(resultado)


#############

print("""\
    
    
    """)

#############

def multiplicar(num1,num2):
    result1= num1*num2
    result2= num1*num2*2
    return result1, result2


result1, result2 = multiplicar(10,18)  # se le da salida a los datos producidos en la funcion mediante 2 variables.

print(result1,result2)

##################

print("""\
    
    
    """)

################

