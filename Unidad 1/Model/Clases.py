import os

class Auto:
    """Clase que representa a los Autos del sistema"""
    #Atributos de Clase
    cantidadRuedas = 4

    #Atributos de Instancia
    #Constructor
    def __init__(self, pat, chas, col, marca, modelo, year):
        #Atributo Privado ==> Encapsular
        self.__Year = year
        self.__Nchasis = str(chas).upper()
        self.__Marca = str(marca).lower()
        self.__Patente = str(pat).upper()
        self.__Color = str(col).upper()
        self.__Modelo = str(modelo).upper()

    def getPatente(self):
        """Retorna la patente del Auto"""
        return self.__Patente

    def setPatente(self, pat):
        self.__Patente = pat

    def getColor(self):
        """Retorna el Color del Auto"""
        return self.__Color

    def setColor(self, value):
        """Cambia el color del Auto al valor especificado"""
        self.__Color = value

    def setYear(self, year):
        self.__Year = year

    def setChasis(self, chas):
        self.__Nchasis = chas

    def setMarca(self, marca):
        self.__Marca = marca

    def setModelo(self, modelo):
        self.__Modelo = modelo

    def getInfo(self):
        return f"Patente: {self.__Patente}, Marca: {self.__Marca}, Modelo: {self.__Modelo}, Color: {self.__Color}, Num Chasis: {self.__Nchasis}, Año: {self.__Year}"

class Mecanico:
    def __init__(self, rut, nom, ape, edad, dir):
        self.__Rut = rut
        self.__Nombre = str(nom).upper()
        self.__Apellido = str(ape).upper()
        self.__Edad = edad
        self.__Direccion = str(dir).upper()

    def getInfo(self):
        return f"Rut: {self.__Rut}, Nombre: {self.__Nombre}, Apellido: {self.__Apellido}, Edad: {self.__Edad}, Direccion: {self.__Direccion}"



class Reparacion:
    def __init__(self, auto, mecanico, costo, repuestos):
        self.__Auto = auto
        self.__Mecanico = mecanico
        self.__Costo = costo
        self.__Repuestos = repuestos

    def getInfo(self):
        return f"INFO REPARACION: Auto: {self.__Auto.getInfo()}, Mecanico: {self.__Mecanico.getInfo()}, Costo: {self.__Costo}, Repuesto: {self.__Repuestos}"
         
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
        print("Presiona 6 para Ver Reparaciones del Sistema: ")

        print("Presiona 7 para Modificar Auto del Sistema: ")
        print("Presiona 8 para Eliminar Auto del Sistema: ")


    def LimpiarConsola():
        os.system('cls' if os.name=='nt' else 'clear')

    def ConfirmarGuardado(TipoObjeto):
        input(f"{TipoObjeto} Guardado Exitosamente! Presiona Enter para Continuar...")

    def ConfirmarEdit(TipoObjeto):
        input(f"{TipoObjeto} Modificado Exitosamente! Presiona Enter para Continuar...")

    def ConfirmarDelete(TipoObjeto):
        input(f"{TipoObjeto} Eliminado Exitosamente! Presiona Enter para Continuar...")
