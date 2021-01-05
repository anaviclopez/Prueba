from Fecha import Fecha
from Persona import Persona

class PruebaPersona():
    def __init__(self):
        Per1 = Persona(None,None,None)
        Nac = Fecha(None,None,None)
        Per1.nombre = 'Juan'
        Per1.apellido = 'Perez'
        Nac.dia = 15
        Nac.mes = 11
        Nac.anio = 1970
        Per1.fnacimiento = Nac
        print('Nombre: ' + Per1.nombre)
        print('Apellido: ' + Per1.apellido)
        print('Fecha de Nacimiento:' + str(Per1.fnacimiento.dia) +'/' + str(Per1.fnacimiento.mes) +'/' + str(Per1.fnacimiento.anio) )
        
        #Cambio de datos
        Nac.anio = 2000
        Per1.fnacimiento = Nac
        print('Fecha de Nacimiento:' + str(Per1.fnacimiento.dia) +'/' + str(Per1.fnacimiento.mes) +'/' + str(Per1.fnacimiento.anio) )

PruebaPersona()