from init_module import init_int, init_float

class MyError(Exception):
    """ Описание своей ошибки """
    def __init__(self, text):
        self.txt = text


def check(a):
    """ Проверка числа на процент """
    if 0 < a <= 100:
        return True
    else:
        return False

def calc(money, percent, months):
    """ Вычисление итоговой суммы денежных средств в копилке """
    ans = 0
    for i in range(months+1):
        buff = ans + money
        ans = buff + buff*percent
        print(f"Месяц {i}, сумма на депозите {ans:.2f}")

    print(f'\nИтоговая сумма средств в копилке: {ans:.2f}')

def main():
    """
    Каждый месяц вы откладываете в копилку в банке одну и ту же определенную сумму, банк
    начисляет проценты на вклад в копилке ежемесячно, прибавляя начисленный % ко вкладу
    в копилке. Программа запрашивает размер взноса, банковский процент и срок накоплений,
    рассчитывающий с помощью функции итоговую сумму денежных средств в копилке.
    """
    money, percent, months = '', '', ''

    while True:
        try:
            money = init_float('\nВведите размер взноса: ')
            if money <= 0:
                raise MyError('\nВведена неверная сумма взноса!\n')
            percent = init_float('Введите банковский процент: ')
            if not check(percent):
                raise MyError('\nВведен неверный процент!\n')
            months = init_int('Введите срок накопления (количество месяцев): ')
            if months < 6 and months > 120:
                raise MyError('Введено неверное количество месяцев! (Минимально - 6, максимально - 120)')
        except ValueError:
            print('\nВы ввели не число, попробуйте ещё раз!\n')
            continue
        except MyError as pe:
            print(pe)
            continue
        else:
            print('Введено верно!')
            break

    calc(money, percent/12/100, months)


if __name__ == '__main__':
    main()