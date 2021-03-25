class FunClass:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        print('Вжух! Сложение превратилось в умножение!')
        return self.a * other

    def __pow__(self, other):
        print('Вжух! Возвдение в степень превратилось в Кота и теперь мяукает!')
        return 'Мяу!'

    def __eq__(self, other):
        return 'Здесь должно было быТь сравнение, но его нет'

    def __str__(self):
        return f'Допустим Кря, ой а fun = {self.a}'


def main():
    fun = FunClass(1)
    print(fun)
    print(f'fun + 3 = {fun + 3}')
    print(f'fun == 2: {fun == 2}')
    print(f'fun ** 2: {fun ** 0}')


if __name__ == '__main__':
    main()
