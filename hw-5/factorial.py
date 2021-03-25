from functools import reduce
from init_module import init_int


class NegativeNumberError(Exception):
    """ Описание своей ошибки """

    def __init__(self, text):
        self.txt = text


def factorial(n):
    """
    Вычисление факториала рекурсивно
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial_itter(func, n):
    """
    Вычисление факториала иттеративно
    """
    num = 1
    while n >= 1:
        num = func(num, n)
        n -= 1
    return num


def factorial_recursive(func, n):
    return reduce(func, range(1, n+1))


def main():
    a = ''
    while True:
        try:
            a = init_int('Введите натуральное число: ')
            if a < 0:
                raise NegativeNumberError('Вы ввели отрицательное число!')
        except ValueError:
            print('Вы ввели не число, попробуйте ещё раз!')
            continue
        except NegativeNumberError as nne:
            print(nne)
        else:
            print('Введено верно!')
            break

    print(f'\nНахождение факториала числа {a}:\n{a}!={factorial(a)}')

    def func(a, b): return a * b

    print(
        f'\nНахождение факториала числа {a} через lambda(не рекурсия)\n{a}!={factorial_itter(func, a)}')
    print(
        f'\nНахождение факториала числа {a} через lambda(рекурсия)\n{a}!={factorial_recursive(func, a)}')


if __name__ == '__main__':
    main()
