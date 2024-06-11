### FUNCION TABLA DE MULTIPLICAR SIN RETORNO NI PARAMETROS

def tabla_multplicar_numero():
    
    
    opcion_mult_mainmenu = str
    main_mult_flag = True
    
    while main_mult_flag == True:
    
        print("""\ Bienvenido a su generador de tablas de multiplicar.
            
            1. Generar Tabla
            2. Salir
                                """)
        
        opcion_mult_mainmenu = input("ingrese una opción para continuar.\n")
        
        if opcion_mult_mainmenu == "1":
                    
            num1= int(input("Ingrese el número a operar.\n"))
            print("")
            i=1
            
            for i in range (1,11):
                acum =+ num1 * i
                print(f"{num1} x {i} = {num1 * i}")
                print("")
                
        elif opcion_mult_mainmenu == "2":
            main_mult_flag = False
            break
        else:
            print("la opcion ingresada no es correcta")
    return         



### FUNCION CONVERSOR KM A MILLA SIN RETORNO NI PARAMETROS

def conver_km_a_milla():
    
    conversor_flag = True
    
    while conversor_flag == True:
        
        conversor_menu_op = input("""\ ingrese operacion de conversión a realizar
                                        
                                        1. Kilómetros a millas
                                        2. Millas a Kilómetros
                                        3. Salir
                                                                        """)
        
        if conversor_menu_op == "1":
            kilometros = float(input(" ingrese distancia en Kilómetros para convertir a Millas:\n"))
            conver_millas = kilometros * 1.60934
            print("La distancia en Millas es:",conver_millas)
        elif conversor_menu_op == "2":
            milla = float(input(" ingrese distancia en Millas para convertir a Kilómetros:\n"))
        elif conversor_menu_op == "3":
            conversor_flag = False
            print("Gracias por utilizar nuestros servicios.")
        else:
            print("opcion inválida.")
    return

## FUNCION CALCULADORA SIMPLE SIN RETORNO NI PARAMETROS

def calculadora_simple():
    
    # Define variables de ambito local en función calculadora_simple 
    
    menu_op_1 = str
    operand_1 = str
    operand_2 = str
    opera_suma = float
    opera_resta = float
    opera_multi = float
    opera_div = float
    
    # FLAGS SETUP

    f_menu_1 = True
    f_input_num_ok = True

    # Main menu and process cycle.  
    

    while f_menu_1 == True:
        
        
        while f_input_num_ok == True:

            try:

                print("")
                operand_1 = (float(input("Por favor ingrese operando primario: \n")))
                print("")
                operand_2 = (float(input("Por favor ingrese operando secundario: \n")))
                print("")
                f_input_num_ok == False
                break   
            
            except ValueError:
                print("ingreso inválido, por favor intentelo nuevamente.")
        
        
        print("""
        Welcome to your personal Calculator.
        
        MENU DE OPCIONES
            
        1. SUMA.
        2. RESTA.
        3. MULTI.
        4. DIV.
        5. SALIR.
            
        """)
        
        
        menu_op_1 = input("Por favor ingrese una opción: \n")
        
        match menu_op_1:
                case "1":
                    opera_suma = (float(operand_1)) + (float(operand_2))
                    print("El resultado de la operación es: \n",opera_suma)
                case "2":
                    opera_resta = (float(operand_1)) - (float(operand_2))
                    print("")
                    print("El resultado de la operación es: \n",opera_resta)
                    opera_resta = (float(operand_2)) - (float(operand_1))
                    print("")
                    print("El resultado de la operación en reversa es: \n",opera_resta)
                case "3":
                    opera_multi = operand_1 * operand_2
                    print("El resultado de la operación es: \n",opera_multi)
                case "4":
                    if operand_2 != 0:            
                        opera_div = operand_1 / operand_2
                        print("El resultado de la operación es: \n",opera_div)
                    else:
                        print("Error el denominador no puede ser 0")
                case "5":
                    f_menu_1 = False
                    print("")
                    print("Gracias por utilizar nuestros servicios")
                    break
                case _:
                    print("Error, ingrese una opción válida.")
    return


#######  Comienzo del programa RAIZ principal

print("""\ bienvenido a su ejecutor de funciones.
        
                        Por favor ingrese una opción de la lista para invocar la función deseada. 
                        
                        
                        1. Calculadora Simple
                        2. Tabla de multiplicar.
                        3. Conversor de KM a milla. 
                        4. Salir.
                        
                        """)

main_menu_flag = True

Opcion_main_menu = input("ingrese una opcion para continuar.\n")

while main_menu_flag == True:
    
    if Opcion_main_menu == "1":
        calculadora_simple()
    elif Opcion_main_menu == "2":
        tabla_multplicar_numero()
    elif Opcion_main_menu == "3":
        conver_km_a_milla()
    elif Opcion_main_menu == "4":
        main_menu_flag = False
        print("Gracias por utilizar nuestros servicios.")
        break
        
    else:
        print("la opción ingresada no es válida")
        