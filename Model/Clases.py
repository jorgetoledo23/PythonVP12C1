class Auto:
    """Clase que representa a los Autos del sistema"""
    #Atributos de Clase
    cantidadRuedas = 4

    #Atributos de Instancia
    #Constructor
    def __init__(self, chas, pat, col, marca, modelo, tipoTrans, tipoAuto, year):
        self.year = year
        self.nchasis = str(chas).upper()
        self.marca = str(marca).lower()
        #Atributo Privado ==> Encapsular
        self.__patente = str(pat).upper()
        self.__color = str(col).upper()
        self.tipoAuto = str(tipoAuto).upper()
        self.tipoTransmision = str(tipoTrans).upper()
        self.modelo = str(modelo).upper()

    def getPatente(self):
        """Retorna la patente del Auto"""
        return self.__patente

    def getColor(self):
        """Retorna el Color del Auto"""
        return self.__color

    def setColor(self, value):
        """Cambia el color del Auto al valor especificado"""
        self.__color = value

    

class Mecanico:
    def __init__(self, nom, ape, edad, tel):
        self.nombre = str(nom).upper()
        self.apellido = str(ape).upper()
        self.edad = edad
        self.telefono = str(tel).upper()

        if edad >= 18:
            self.mayorDeEdad = True
        else:
            self.mayorDeEdad = False



class Reparacion:
    def __init__(self, auto, mecanico, costo, repuestos):
        self.autoReparado = auto
        self.mecanicoAsignado = mecanico
        self.costo = costo
        self.respuestosUtilziados = repuestos

    def getInfoReparacion(self):
        infoReparacion = f"INFO REPARACION: Auto Patente: {self.autoReparado.getPatente()}, Color: {self.autoReparado.getColor()}, Mecanico Asignado: {self.mecanicoAsignado.nombre} {self.mecanicoAsignado.apellido}, COSTO TOTAL ${self.costo}" 
        return infoReparacion

    def cambiarColor(self, color):
        self.autoReparado.setColor(color)


class Cliente:
    pass





class Perro:
    #Atributo de Clase
    especie = "Mamifero"

    def __init__(self, nom):
        self.nombre = nom

class Math:
    #Atributo de Clase
    PI = 3.1416
