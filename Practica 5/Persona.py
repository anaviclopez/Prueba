from Fecha import Fecha
class Persona():
    def __init__(self,nombre,apellido,fnacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fnacimiento = fnacimiento

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
    def fnacimiento(self,value):
        self.__fnacimiento = Fecha(value.dia,value.mes,value.anio)
