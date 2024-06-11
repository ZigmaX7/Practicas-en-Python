# Define variables

menu_op_1 = str;
operand_1 = str;
operand_2 = str;
opera_suma = float;
opera_resta = float;
opera_multi = float;
opera_div = float;

# FLAGS

f_menu_1 = bool;
f_input_num_ok = bool;

# FLAG SETUP

f_menu_1 = True;


# Main menu and process cycle.

while f_menu_1 == True:
    
    print("""
    Welcome to your personal Calculator.
    """)
    
    while True:

        try:

            print("");
            operand_1 = (float(input("Por favor ingrese operando primario: \n")));
            print("");
            operand_2 = (float(input("Por favor ingrese operando secundario: \n")));
            print("");
            
            break   
        
        except ValueError:
            print("ingreso inválido, por favor intentelo nuevamente.");
    
    print("""\
    MENU DE OPCIONES
        
    1. Sumar.
    2. Restar.
    3. multiplicar.
    4. Dividir.
    5. Salir.
        
    """)

### tratar de hacer el menu con un match case, siendo menu_op_1 el CASE
### y las opciones los matchs.
### recordar que los


    menu_op_1 = str(input("Por favor ingrese una opción: \n"));
    print("Su opción ingresada es: \n", str(menu_op_1));
    if menu_op_1 == ("1"):
        opera_suma = (float(operand_1)) + (float(operand_2));
        print("El resultado de la operación es: \n",opera_suma);
    elif menu_op_1 == ("2"):
        opera_resta = (float(operand_1)) - (float(operand_2));
        print("");
        print("El resultado de la operación es: \n",opera_resta);
        opera_resta = (float(operand_2)) - (float(operand_1));
        print("");
        print("El resultado de la operación en reversa es: \n",opera_resta);
    elif menu_op_1 == ("3"):
        opera_multi = operand_1 * operand_2;
        print("El resultado de la operación es: \n",opera_multi);
    elif menu_op_1 == ("4"):
        if operand_2 != 0:            
            opera_div = operand_1 / operand_2;
            print("El resultado de la operación es: \n",opera_div);
        else:
            print("Error el denominador no puede ser 0");
    elif menu_op_1 == ("5"):
        f_menu_1 = False;
        print("");
        print("Gracias por utilizar nuestros servicios");
    else:
        print("La opcion elegida no corresponde a una opción válida. Vuelva a intentarlo");

