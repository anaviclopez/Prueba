
class Persona():
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido

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

