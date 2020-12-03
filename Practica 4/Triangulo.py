# -------- Sobrecarga de Métodos (no existe en Python :()) ------------------- 
class Triangulo():
    def __init__(self,base,altura):

        self.b = base
        self.a = altura
    def area(self):
        return self.b*self.a/2.0

    def area1(self,base,altura):
        return base * altura/2.0