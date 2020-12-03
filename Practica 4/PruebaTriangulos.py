from Triangulo import Triangulo
class PruebaTriangulos():
    def __init__(self):
        T = Triangulo(5,8)
        print('Base: ' + str(T.b))
        print('Altura: ' + str(T.a))
        # Metodo area sobrecargado
        print('area()--> ' + str(T.area()))
        print('area(6,2) ' + str(T.area1(6,2)))
        print('area(5.5,3.2): ' + str(T.area1(5.5,3.2)))

PruebaTriangulos()