from math import sqrt, pi

class Figure:

    def square(self):
        pass

class Circle(Figure):

    def __init__(self, r: int|float) -> None:
        if float(r) <= 0:
            raise Exception(
                'Радиус окружности должен быть положительным числом'
            )
        self.r = float(r)

    def square(self):
        return round(pi*(self.r**2), 2)
    
class Triangle(Figure):

    def __init__(self, a: int|float, b: int|float, c: int|float) -> None:
        if float(a) <= 0 or float(b) <= 0 or float(c) <= 0:
            raise Exception('Длинна стороны не может быть меьше или равна 0')
        data = [float(a), float(b), float(c)]
        for _ in range(3):
            side = data.pop(0)
            if side >= sum(data): 
                raise Exception(
                    'Треугольник существует только тогда, когда сумма двух его'
                    ' сторон больше третьей.'
                )
            data.append(side)
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def rectangular(self):
        data = [self.a, self.b, self.c]
        for _ in range(3):
            gipotenusa = data.pop(0)
            catets = [d**2 for d in data]
            if gipotenusa**2==sum(catets):
                return True
            data.append(gipotenusa)
        return False

if __name__ == '__main__':
    c1 = Circle(5)
    c2 = Circle('0.76')
    t1 = Triangle(3, 5, 7)
    t2 = Triangle(3, 4, '5')
    # t3 = Triangle(0, 5, 3)
    # t3 = Triangle(9, 5, 3)
    print(c1.square())
    print(c2.square())
    print(t1.square())
    print(t1.rectangular())
    print(t2.square())
    print(t2.rectangular())
    # print(t3.square())