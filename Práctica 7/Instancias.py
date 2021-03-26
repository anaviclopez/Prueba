from EmpleadoClase import Empleado
from GerenteSubclase import Gerente

class Instancias():
    g = Gerente('Luis Aguilar',8524,16000,5000)
    l = [Empleado,Gerente,object,list]
    for i in l:
        if isinstance(g,i):
            print('Instancia de ' + str(i))
        else:
            print('No es instancia de ' + str(i))

Instancias()
