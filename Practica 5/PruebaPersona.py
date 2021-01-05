from Fecha import Fecha
from Persona import Persona

class PruebaPersona():
    def __init__(self):
        Per1 = Persona(None,None)
        Nac = Fecha(None,None,None)
        Per1.nombre = 'Juan'
        Per1.apellido = 'Perez'
        Nac.dia = 15
        Nac.mes = 11
        Nac.anio = 1950
        print('Nombre: ' + Per1.nombre)
        print('Apellido: ' + Per1.apellido)
        print('Fecha de Nacimiento:' + str(Nac.dia) +'/' + str(Nac.mes) +'/' + str(Nac.anio) )


PruebaPersona()