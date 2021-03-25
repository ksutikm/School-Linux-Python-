from math import pi, sqrt


class Figure:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        pass

    def area(self):
        pass

    def volume(self):
        pass

    def __str__(self):
        s = f'Фигура: {self.name}\n'
        s += f'Периметр: {self.perimeter():.2f}\n' if self.perimeter() else ''
        s += f'Площадь: {self.area():.2f}\n' if self.area() else ''
        s += f'Объем: {self.volume():.2f}\n' if self.volume() else ''
        return s


class Square(Figure):
    def __init__(self, length):
        super().__init__("Квадрат")
        self.length = length

    def perimeter(self):
        return self.length * 4

    def area(self):
        return self.length ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Треугольник")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semi_perimeter = self.perimeter() / 2
        return sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c))


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


class Ball(Figure):
    def __init__(self, radius):
        super().__init__("Шар")
        self.radius = radius

    def area(self):
        return 4 * pi * self.radius ** 2

    def volume(self):
        return 4 / 3 * pi * self.radius ** 3


def main():
    square = Square(4)
    print(square)

    triangle = Triangle(3, 4, 5)
    print(triangle)

    circle = Circle(5)
    print(circle)

    ball = Ball(6)
    print(ball)


if __name__ == '__main__':
    main()
