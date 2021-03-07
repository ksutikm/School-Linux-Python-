# Решение квадратного уравнения (комплексные числа учитываются)

def quadratic_equation():
    print('Введите коэффициенты квадратного уровнения a•x²+b•x+c=0')
    a = float(input('Введите значение a: '))
    b = float(input('Введите значение b: '))
    c = float(input('Введите значение c: '))
    discriminant = b ** 2 - 4 * a * c
    print('Дискриминант = {0:.2f}'.format(discriminant))
    if discriminant == 0:
        x = -b / (2 * a)
        print('x = {0:.2f}'.format(x))
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print('x₁ = {0:.2f}'.format(x1))
        print('x₂ = {0:.2f}'.format(x2))


quadratic_equation()