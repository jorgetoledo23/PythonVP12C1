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

    if (opcionSeleccionada == "4"):
        Menu.LimpiarConsola()
        print("Opcion Seleccionada: 4 Ver Autos")
        print("")
        for A in listaAutos:
            print(A.getInfo())
        input("Presione una tecla para volver al Menu Principal.")

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