from init_module import init_float

def main():
    '''
    Решение квадратного уравнения
    '''
    try:
        print('Введите коэффициенты квадратного уровнения a•x²+b•x+c=0')
        a = init_float('Введите значение a: ')
        b = init_float('Введите значение b: ')
        c = init_float('Введите значение c: ')

        if a == 0:
            if b == 0:
                if c == 0:
                    print('x - любое число')
                else:
                    print('Нет решения!')
            elif c == 0:
                print('x = 0')
            else:
                print('x = {0:.2f}'.format(-c / b))
        elif b == 0:
            if c == 0:
                print('x = 0')
            else:
                x1 = (-c / a) ** 0.5
                x2 = - (-c / a) ** 0.5
                print('x₁ = {0:.2f}'.format(x1))
                print('x₂ = {0:.2f}'.format(x2))
        elif c == 0:
            print('x₁ = 0')
            print('x₂ = {0:.2f}'.format(-b / a))
        else:
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

    except ValueError:
        print("Введена строка, а не число")

if __name__ == '__main__':
    main()