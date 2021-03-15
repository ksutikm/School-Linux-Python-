class MyError(Exception):
    def __init__(self, text):
        self.txt = text


money, prothent, months = '', '', ''

def check(a):
    if 0 < a <= 100:
        return True
    else:
        return False

while True:
    try:
        money = float(input('\nВведите размер взноса: '))
        if money <= 0:
            raise MyError('\nВведена неверная сумма взноса!\n')
        prothent = float(input('Введите банковский процент: '))
        if not check(prothent):
            raise MyError('\nВведен неверный процент!\n')
        months = int(input('Введите срок накопления (количество месяцев): '))
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

ans = 0
while months > 0:
    buff = ans + money
    ans = buff + buff * prothent / 100
    months -= 1

print(f'\nИтоговая сумма средств в копилке: {ans:.2f}')
