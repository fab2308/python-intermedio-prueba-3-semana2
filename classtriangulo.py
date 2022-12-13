#Crear una clase personalizada para cálculos básicos sobre un triángulo.

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        resultado = self.base * self.altura / 2

        return resultado
    
    def perimetro(self, a, b, c):
        resultado = a + b + c

        return resultado
    def Triangletype(a, b, c):
        a = int(a)
        b = int(b)
        c = int(c)
        
        if a==b and a==c and b==c:
           print("El triangulo es Equilatero")
        elif a == b or b == c or a == c:
           print("El triangulo es Isosceles")
        else:
           print("El triangulo es Escaleno")

t = Triangulo.Triangletype(3,3,3)

t = Triangulo(3, 5)
print('Área del triángulo: %.2f' % t.area())
print('Perímetro del triángulo: %.2f' % t.perimetro(3, 3, 3))

