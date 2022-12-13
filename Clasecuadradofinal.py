#Crear una clase personalizada para cálculos básicos sobre un rectángulo.

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        resultado = self.lado * self.lado

        return resultado
    
    def perimetro(self):
        resultado = self.lado * 4

        return resultado
    def ladosfinal(self):
        resultado = self.lado
        return resultado
    

c = Cuadrado(10)
print('Área del cuadrado: %.2f' % c.area())
print('Perímetro del cuadrado: %.2f' % c.perimetro())
print('Cada lado del cuadrado es:', c.ladosfinal())






