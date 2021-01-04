class Circulo():
    PI = 3.14159
    '''
    All members in a Python class are public by default. Any member can be accessed from outside the class environment.
    Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. 
    This effectively prevents it to be accessed, unless it is from within a sub-class. 
    Similarly, a double underscore __ prefixed to a variable makes it private.
    '''

    def __init__(self,radio):
        self.__x = radio

    @property
    def radio(self):
        return self.__x

    @radio.setter
    def radio(self, value):
        self.__x = value

    def perimetro(self):
        return 2*Circulo.PI*self.__x

    def area(self):
        return Circulo.PI*self.__x*self.__x
    def String(self):
        return print('Circulo [radio=' + str(self.__x) + '] ')