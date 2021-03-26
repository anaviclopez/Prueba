from EmpleadoClase import Empleado
class Gerente(Empleado):
    "Clase que representa a empleado gerente."
    def __init__(self,nombre,numEmpleado, sueldo,presupuesto):
        "Constructor de Gerente"
        # llamamos al constructor de Empleado
        Empleado.__init__(self,nombre,numEmpleado, sueldo)
        # agregamos el nuevo atributo
        self.presupuesto = presupuesto
    def asignarpresupuesto(self,presupuesto):
        self.presupuesto = presupuesto
        return self.presupuesto