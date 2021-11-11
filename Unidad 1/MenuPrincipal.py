from Model.Clases import *

listaAutos = []
listaMecanicos = []
listaReparaciones = []


def insertarDatosTesting():
    A = Auto('GHFG23','GTSFDRSF343434','ROJO', 'KIA','RIO 5', 2013)
    A2 = Auto('WESD17','HSTDGDRSF34332','BLANCO', 'NISSAN','TERRANO', 2010)
    A3 = Auto('HTDG22','IKYUHHFTDG2323','GRIS', 'MAZDA','CX 5', 2020)
    listaAutos.append(A)
    listaAutos.append(A2)
    listaAutos.append(A3)

    #(self, nom, ape, edad, tel)
    M = Mecanico('1.123.123-1','ALEXIS', 'SANCHEZ', 35, 'CURICO')
    M2 = Mecanico('2.123.123-1','ARTURO', 'VIDAL', 30, 'MOLINA')
    M3 = Mecanico('3.123.123-1','GARY', 'MEDEL', 40, 'TENO')
    listaMecanicos.append(M)
    listaMecanicos.append(M2)
    listaMecanicos.append(M3)
insertarDatosTesting()

while True:
    Menu.LimpiarConsola()
    Menu.MostrarMenu()
    opcionSeleccionada = input("Selecciona una Opcion: ")

    if(opcionSeleccionada == "7"):
        #Editar Auto
        Menu.LimpiarConsola()
        i = 1
        for A in listaAutos:
            print(f"{i} - {A.getInfo()}")
            i += 1

        opcion = int(input("Selecciona el Auto que deseas Modificar: "))

        listaAutos[opcion - 1].setPatente(input("Ingrese Patente: "))
        listaAutos[opcion - 1].setChasis(input("Ingrese Numero Chasis: "))
        listaAutos[opcion - 1].setColor(input("Ingrese Color: "))
        listaAutos[opcion - 1].setMarca(input("Ingrese Marca: "))
        listaAutos[opcion - 1].setModelo(input("Ingrese Modelo: "))
        listaAutos[opcion - 1].setYear(input("Ingrese Año: "))

        Menu.ConfirmarEdit("Auto")

    if (opcionSeleccionada == "8"):
        Menu.LimpiarConsola()
        i = 1
        for A in listaAutos:
            print(f"{i} - {A.getInfo()}")
            i += 1

        opcion = int(input("Selecciona el Auto que deseas Eliminar: "))

        listaAutos.remove(listaAutos[opcion - 1])

        Menu.ConfirmarDelete("Auto")

    if (opcionSeleccionada == "1"):
        Menu.LimpiarConsola()
        #Logica para Agregar un Auto a la Base de Datos
        print("Opcion Seleccionada: Agregar Auto.")
        print("------------Ingrese Informacion del Auto-----------------")
        print(" ")
        pat = input("Patente: ")
        chas = input("Numero Chasis: ")
        col = input("Color: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        year = input("Año: ")
        A = Auto(pat,chas,col,marca,modelo,year)
        #A = Auto(chas=chas,pat=pat,col=col,marca=marca,modelo=modelo,tipoTrans=tTrans,tipoAuto=tAuto,year=year)
        listaAutos.append(A)
        
        Menu.ConfirmarGuardado("Auto")


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
        Menu.ConfirmarGuardado("Reparacion")

    if (opcionSeleccionada == "2"):
        Menu.LimpiarConsola()
        #Logica para Agregar un Mecanico a la Base de Datos
        print("Opcion Seleccionada: Agregar Mecanico.")
        print("------------Ingrese Informacion del Mecanico-----------------")
        print(" ")
        rut = input("Ingrese Rut: ")
        nom = input("Nombre: ")
        ape = input("Apellido: ")
        edad = int(input("Edad: "))
        dir = input("Direccion: ")
        M = Mecanico(rut,nom,ape,edad,dir)
        listaMecanicos.append(M)
        Menu.ConfirmarGuardado("Mecanico")

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