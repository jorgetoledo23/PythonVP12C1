from Model.Clases import *

listaAutos = []
listaMecanicos = []
listaReparaciones = []


while True:
    Menu.LimpiarConsola()
    Menu.MostrarMenu()
    opcionSeleccionada = input("Selecciona una Opcion: ")

    if (opcionSeleccionada == "1"):
        Menu.LimpiarConsola()
        #Logica para Agregar un Auto a la Base de Datos
        print("Opcion Seleccionada: Agregar Auto.")
        print("------------Ingrese Informacion del Auto-----------------")
        pat = input("Patente: ")
        chas = input("Numero Chasis: ")
        col = input("Color: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        tTrans = input("Tipo Transmision: ")
        tAuto = input("Tipo Auto: ")
        year = input("Año: ")
        A = Auto(chas,pat,col,marca,modelo,tTrans,tAuto,year)
        #A = Auto(chas=chas,pat=pat,col=col,marca=marca,modelo=modelo,tipoTrans=tTrans,tipoAuto=tAuto,year=year)
        listaAutos.append(A)
        print("Auto Guardado!")
        input("Presione una tecla para volver al Menu Principal.")


    if (opcionSeleccionada == "3"):
        Menu.LimpiarConsola()
        #Logica para Agregar un Auto a la Base de Datos
        print("---------------Opcion Seleccionada: Agregar Reparacion.----------------")
        print("------------------Listado de Mecanicos--------------------")

        i = 1
        for M in listaMecanicos:
            print(f"{i} - {M.getInfo()}")
            i += 1

        opcion = int(input("Selecciona el Numero del Mecanico: "))
        mecanicoSeleccionado = listaMecanicos[opcion - 1]

        i = 1
        for A in listaAutos:
            print(f"{i} - {A.getInfo()}")
            i += 1

        opcion = int(input("Selecciona el Numero del Auto: "))
        autoSeleccionado = listaAutos[opcion - 1]

        costo = input("Ingresa el Valor de la Reparacion: ")

        repuesto = input("Ingresa el repuesto de la Reparacion: ")

        R = Reparacion(autoSeleccionado, mecanicoSeleccionado, costo, repuesto)
        listaReparaciones.append(R)
        #print(mecanicoSeleccionado.getInfo())
        input("Reparacion Ingresada Correctamente. Presiona Enter para continuar...")








    

    if (opcionSeleccionada == "2"):
        Menu.LimpiarConsola()
        #Logica para Agregar un Mecanico a la Base de Datos
        print("Opcion Seleccionada: Agregar Mecanico.")
        print("------------Ingrese Informacion del Mecanico-----------------")
        nom = input("Nombre: ")
        ape = input("Apellido: ")
        edad = int(input("Edad: "))
        tel = input("Telefono: ")
        M = Mecanico(nom,ape,edad,tel)
        listaMecanicos.append(M)
        print("Mecanico Guardado!")
        input("Presione una tecla para volver al Menu Principal.")

    if (opcionSeleccionada == "5"):
        Menu.LimpiarConsola()
        print("Opcion Seleccionada: 5 Ver Mecanicos")
        print("")
        for M in listaMecanicos:
            print(M.getInfo())
        input("Presione una tecla para volver al Menu Principal.")
    
    if (opcionSeleccionada == "6"):
        Menu.LimpiarConsola()
        print("Opcion Seleccionada: 6 Ver Reparaciones")
        print("")
        for R in listaReparaciones:
            print(R.getInfo())
        input("Presione una tecla para volver al Menu Principal.")

    if (opcionSeleccionada == "4"):
        Menu.LimpiarConsola()
        print("Opcion Seleccionada: 4 Ver Autos")
        print("")
        for A in listaAutos:
            print(A.getInfo())
        input("Presione una tecla para volver al Menu Principal.")