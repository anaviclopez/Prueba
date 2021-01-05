from Fecha1 import Fecha1
from Persona1 import Persona1

# Sin embargo, se pueden modificar las clases para que no tenga que instanciarse la clase
# Fecha fuera de la clase Persona, quedando así un mejor diseño de clases.

class PruebaPersona1():
    def __init__(self):
        Per1 = Persona1(None,None,None,None,None)
        Per1.nombre = 'Juan'
        Per1.apellido = 'Perez'
        Per1.fnacimiento.fdia = 15
        Per1.fnacimiento.fmes = 8
        Per1.fnacimiento.fanio = 1950
        print('Nombre: ' + Per1.nombre)
        print('Apellido: ' + Per1.apellido)
        print('Fecha de Nacimiento: ' + str(Per1.fnacimiento.fdia) + '/' + str(Per1.fnacimiento.fmes) + '/' + str(Per1.fnacimiento.fanio))
PruebaPersona1()