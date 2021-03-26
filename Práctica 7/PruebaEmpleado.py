from EmpleadoClase import Empleado
from GerenteSubclase import Gerente
class PruebaEmpleado():
    def __init__(self):
        g = Gerente('Luis Aguilar',8524,16000,5000)
        print('Nombre: ' + str(g.nombre))
        print('Número: ' + str(g.numEmpleado))
        print('Sueldo: ' + str(g.sueldo))
        print('Presupuesto: ' + str(g.presupuesto))
        g.aumentarsueldo(10)
        print('Nuevo sueldo: ' + str(g.sueldo))
        g.asignarpresupuesto(650000)
        print('Nuevo presupuesto: ' + str(g.presupuesto))

PruebaEmpleado()
