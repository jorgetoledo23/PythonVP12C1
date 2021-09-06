from Model.Clases import Auto, Mecanico, Reparacion

#Auto1 = Auto()
Auto1 = Auto(
    chas="AJKSDGAHJ234",
    pat="FSZR35",
    col="Rojo",
    marca="KIA",
    modelo="ceRATo",
    tipoTrans="Automatico",
    tipoAuto="Sedan",
    year=2013
)

Auto2 = Auto(
    chas="JKFSUYSFDHRWESDH23",
    pat="GhDg54", #GHDG54
    col="Verde",
    marca="kIa",
    modelo="ceRATo",
    tipoTrans="aUtoMaTiCo",
    tipoAuto="sEdan",
    year=2013
)

Meca1 = Mecanico(nom="Juan", ape="Ramirez", edad=35, tel="+56912345678")
Meca2 = Mecanico("Daniel", "Gonzalez", 45, "+56987654321")

Auto1.getPatente()

listaRepuestos = ["Empaquetadura de Culata", "Sellante"]

reparacionKia = Reparacion(
    auto=Auto1,
    mecanico=Meca2,
    costo=285000,
    repuestos=listaRepuestos
)
reparacionKia.cambiarColor("Verde")

#reparacionKia.autoReparado.patente = "JAJAJAJAJAJA"

print(reparacionKia.getInfoReparacion())
#INFO REPARACION: Auto Patente: FSZR35, Color: ROJO, Mecanico Asignado: DANIEL GONZALEZ, COSTO TOTAL $285000
#INFO REPARACION: Auto Patente: FSZR35, Color: Verde, Mecanico Asignado: DANIEL GONZALEZ, COSTO TOTAL $285000
print(Auto1.getColor())

print(Auto1.__doc__) # Clase que representa a los Autos del sistema
print(str.__doc__)




