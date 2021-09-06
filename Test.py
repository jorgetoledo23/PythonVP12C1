from Model.Clases import Auto


AutoA = Auto()
AutoB = Auto()

AutoA.year = 2013
AutoA.color = "Rojo"
AutoA.patente = "FSZR33"


AutoB.year = 2013
AutoB.color = "Rojo"
AutoB.patente = "GHTS23"

AutoA.avanzar(10)
AutoA.bajarVentanilla("Derecha/Delantera")
AutoA.frenar()


