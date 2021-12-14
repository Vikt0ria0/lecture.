class Operation:

    def plus(self, x, y):
        print(x + y)

    def minus(self, x, y):
        print(x - y)

    def umnoj(self, x, y):
        print(x * y)

    def delenie(self, x, y):
        print(x / y)

    def modul(self, x, y):
        print(abs(7 + 8j))

    def stepen(self, x, y):
        print(pow(x + y, 2))


k = Operation()
x = complex(5, 6)
y = complex(7, 8)

k.plus(x, y)

k.minus(x, y)

k.umnoj(x, y)

k.modul(x, y)

k.delenie(x, y)

k.stepen(x, y)

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Где сумма c1 и c2 равна:')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Где произведение c1 и c2 равно:')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c1 = ComplexNumber(1, -2)

c2 = ComplexNumber(3, 4)

print(c1)
print(c1+c2)
print(c1*c2)
