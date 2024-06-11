# Defining and initializing variables
opcionMenu = ''
tareaMain = ''
tarea1 = ''
tarea2 = ''
tarea3 = ''
respflag1 = ''
tareaFlag1 = True
opcionListaA = False
opcionListaB = False
contaTarea = 0
tareaMainIRAY = 0
contadorTarea = 0
opcionTarea = 0
index = 0
i = 0

# Arrays for tasks
arregloTarea = []
modTareaAN = ''
taskCheckAll = ''
taskCheck = 0
markTareaAN = ''

# Requesting task data
while tareaFlag1:
    print("Bienvenido a su gestor de tareas.")
    print("Ingrese cantidad de tareas a realizar")
    index = int(input())

    arregloTarea = [None] * index

    for i in range(index):
        print("Tarea[", i+1, "] = ", end='')
        arregloTarea[i] = input()

    print("¿Está de acuerdo con registrar ", index, " tareas a realizar? (S/N)")
    respflag1 = input()

    if respflag1 == "S" and arregloTarea[index-1] != "":
        tareaFlag1 = False
    elif respflag1 == "S" and arregloTarea[index-1] == "":
        print("Error: hay tareas vacías. Vuelva a intentarlo...")
        index = 0
        input("Presione una tecla para volver a intentarlo...")
    elif respflag1 == "N" and arregloTarea[index-1] != "":
        print("Presione una tecla para volver a intentarlo...")
        index = 0
        input()
    else:
        print("Ingreso inválido. Presione una tecla para continuar...")
        index = 0
        input()

# Main menu loop
while opcionMenu != "C":
    print("")
    print("A: Listar / Modificar tareas actuales")
    print("B: Listar / Marcar como realizadas")
    print("C: Salir")
    print("")
    opcionMenu = input("Ingrese una opción (A/B/C): ")

    # Options Menu
    if opcionMenu == "A":
        opcionListaA = True

        while opcionListaA:
            print("Estas son sus tareas. Elija qué tarea desea modificar o borrar.")
            print("")

            for i in range(index):
                print("Tarea[", i+1, "] =", arregloTarea[i])
                print("Desea borrar / modificar? presione ", "(", i+1, ")")
                print("")

            opcionTarea = int(input("Ingrese número de la tarea para modificarla: "))

            if opcionTarea >= 0 and opcionTarea <= i:
                print("Por favor rescriba o ingrese vacío para borrar la tarea.")
                arregloTarea[opcionTarea-1] = input()

                print("Estas son sus tareas actualizadas.")
                print("")

                for i in range(index):
                    print("Tarea[", i+1, "] =", arregloTarea[i])
            else:
                print("Error: ha ingresado un número de tarea inválido.")

            modTareaAN = input("Desea seguir modificando tareas? (S/N): ")

            if modTareaAN == "S":
                input("Presione una tecla para continuar...")
            else:
                opcionListaA = False

    elif opcionMenu == "B":
        opcionListaB = True

        while opcionListaB:
            print("Estas son sus tareas. Elija qué tarea desea marcar como completada.")
            print("")

            for i in range(index):
                print("Tarea[", i+1, "] =", arregloTarea[i])
                print("Desea marcar como completada? presione ", "(", i+1, ")")
                print("")

            taskCheck = int(input("Por favor ingrese la tarea a marcar como completada: "))

            while not (taskCheck >= 0 and taskCheck <= i):
                print("Por favor ingrese un número correcto de tarea.")
                taskCheck = int(input())
                os.system('cls')

            arregloTarea[taskCheck-1] += " X"

            print("Esta es la lista de tareas actualizada")
            print("")

            for i in range(index):
                print("Tarea[", i+1, "] =", arregloTarea[i])

            taskCheckAll = input("¿Desea marcar todas las tareas como finalizadas? (S/N): ")

            while taskCheckAll != "S" and taskCheckAll != "N":
                print("Error: Ingrese una opción válida (S/N)")
                taskCheckAll = input()

            if taskCheckAll == "S":
                for i in range(index):
                    arregloTarea[i] += " X "
                print("Esta es la lista de tareas actualizada")
                print("")
                for i in range(index):
                    print("Tarea[", i+1, "] =", arregloTarea[i])
                print("")
            else:
                if taskCheckAll == "N":
                    markTareaAN = input("Desea seguir marcando tareas? (S/N): ")

                    if markTareaAN == "S":
                        input("Presione una tecla para continuar...")
                    else:
                        opcionListaB = False

    elif opcionMenu == "C":
        print("Gracias por utilizar nuestros servicios.")
    else:
        print("Error: Por favor ingrese una opción válida.")
