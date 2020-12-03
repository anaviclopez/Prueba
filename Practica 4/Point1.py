# -------- Constructores ------------------- 

class Point1():

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def ImprimirPunto(self):
        return print('Punto[x = '+ str(self.x) +',y = '+ str(self.y) + ']')

