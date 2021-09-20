import os

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

    def uptPatente(self, pat):
        self.__patente = pat

    def getColor(self):
        """Retorna el Color del Auto"""
        return self.__color

    def setColor(self, value):
        """Cambia el color del Auto al valor especificado"""
        self.__color = value

    def getInfo(self):
        return f"Patente: {self.__patente}, Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.__color}, Num Chasis: {self.nchasis}, Tipo Auto: {self.tipoAuto}, Tipo Transmision: {self.tipoTransmision}, Año: {self.year}"

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

    def getInfo(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Telefono: {self.telefono}"

class Reparacion:
    def __init__(self, auto, mecanico, costo, repuestos):
        self.autoReparado = auto
        self.mecanicoAsignado = mecanico
        self.costo = costo
        self.respuestosUtilziados = repuestos

    def getInfo(self):
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

class Menu:

    def MostrarMenu():
        print("-----------------------------SISTEMA DE TALLER MECANICO-----------------------------")
        print(" ")
        #Opciones de Insert
        print("Presiona 1 para Agregar Auto: ")
        print("Presiona 2 para Agregar Mecanico: ")
        print("Presiona 3 para Agregar Reparacion: ")

        #Opciones de Leer
        print("Presiona 4 para Ver Autos del Sistema: ")
        print("Presiona 5 para Ver Mecanicos del Sistema: ")


    def LimpiarConsola():
        os.system('cls' if os.name=='nt' else 'clear')