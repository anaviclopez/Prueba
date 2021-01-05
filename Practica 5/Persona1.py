from Fecha1 import Fecha1
class Persona1():
    def __init__(self,nombre,apellido,fdia,fmes,fanio):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fnacimiento = Fecha1(fdia,fmes,fanio)
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value
# La composición es una forma de reutilización de software, en donde una clase tiene como miembros referencias a objetos de otras clases
    @property
    def fnacimiento(self):
        
        return self.__fnacimiento

    @fnacimiento.setter
    def fnacimiento(self,fdia,fmes,fanio):
        self.__fnacimiento = Fecha1(fdia,fmes,fanio)