class Fecha1():

    def __init__(self,dia,mes,anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        if value > 0 and value < 32:
            self.__dia = value
        else:
            print('Dia no valido')

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        if value > 0 and value < 13:
            self.__mes = value
        else:
            print('Mes no valido')

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, value):
        if value > 0:
            self.__anio = value
        else:
            print('Año no valido')