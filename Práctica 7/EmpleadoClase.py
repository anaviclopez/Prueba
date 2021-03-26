class Empleado():
    "Clase que representa un empleado."
    def __init__(self,nombre,numEmpleado, sueldo):
        "Constructor de empleado"
        self.nombre = nombre
        self.numEmpleado = numEmpleado
        self.sueldo = sueldo
    def aumentarsueldo(self,porcentaje):
        self.sueldo += (self.sueldo * int(porcentaje) / 100)
        return self.sueldo

