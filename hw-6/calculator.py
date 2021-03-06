from math import inf


def calculator():
    """
    Калькулятор для расчета базовых операций:
        "+" - сложение
        '-' - вычитание
        '*' - умножение
        '/' - деление
        '**' - возведение в степень
    """
    print('''
    Калькулятор для расчета базовых операций:
    "+" - сложение
    '-' - вычитание
    '*' - умножение
    '/' - деление
    '**' - возведение в степень
    Пустая строка - выход
    ''')

    data = input('Введите первое действие (например, 4+12):')
    ans = 0
    while True:
        operation, index = get_operation(data)
        if operation:
            a = ans if ans else get_float(data[:index])
            b = get_float(data[index + len(operation):])

            def add(a, b): return a + b
            def difference(a, b): return a - b
            def multiply(a, b): return a * b
            def divide(a, b): return a / b if b else inf

            def power(a, b):
                try:
                    ans = a ** b
                except OverflowError as ex:
                    print('Переполнение!!!', ex)
                    return 0
                return ans

            op = {
                '+': add,
                '-': difference,
                '*': multiply,
                '/': divide,
                '**': power
            }

            ans = op[operation](a, b)
        else:
            print('Неверная операция!')
        data = input(f'Результат: {ans}. Продолжаем считать? (Выход - Enter)')

        if not data:
            print('Расчет закончен!')
            break


def get_float(number):
    """ Получение числа типа float """
    try:
        number = float(number)
    except Exception as ex:
        print('Введено не число или не введен стартовый элемент!')
        return 0
    return number


def get_operation(data):
    """ Получение оператора для вычисления """
    operation = ['**', '+', '-', '*', '/']
    for op in operation:
        index = data.find(op)
        if index > -1:
            return op, index
    return False, False


if __name__ == '__main__':
    calculator()
