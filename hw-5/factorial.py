"""
Вычисление факториала
"""
class NegativeNumberError(Exception):
    def __init__(self, text):
        self.txt = text

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_itter(func, n):
    num = 1
    while n >= 1:
        num = func(num, n)
        n -= 1
    return num

def factorial_recursive(func, n):
    return reduce(func, range(1, n+1))

a = ''
while True:
    try:
        a = int(input('Введите натуральное число: '))
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

func = lambda a, b: a * b


from functools import reduce

print(f'\nНахождение факториала числа {a} через lambda(не рекурсия)\n{a}!={factorial_itter(func, a)}')
print(f'\nНахождение факториала числа {a} через lambda(рекурсия)\n{a}!={factorial_recursive(func, a)}')