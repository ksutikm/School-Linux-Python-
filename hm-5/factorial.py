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

print(f'Нахождение факториала числа {a}:\n{a}!={factorial(a)}')