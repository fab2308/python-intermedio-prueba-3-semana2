#Crear una clase personalizada para cálculos básicos sobre un rectángulo.

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        resultado = self.ancho * self.alto

        return resultado
    
    def perimetro(self):
        resultado = 2 * (self.ancho + self.alto)

        return resultado
    def anchofinal(self):
        resultado = self.ancho
        return resultado
    def altofinal(self):
        resultado = self.alto
        return resultado 

r = Rectangulo(10, 7)
print('Área del rectángulo: %.2f' % r.area())
print('Perímetro del rectángulo: %.2f' % r.perimetro())
print('Ancho del rectangulo es', r.anchofinal())
print('Alto del rectangulo es', r.altofinal())



