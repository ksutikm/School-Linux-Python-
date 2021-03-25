from init_module import init_int


def foo(a, b):
    """
    Функция foo собирает все числа из заданного диапазона в одну строку.
    """
    return ''.join(str(x) for x in range(a, b + 1))


def main():
    """ Частота использования цифр в диапозоне
    Пользователь вводит начало и конец диапазона.
    Скрипт выводит частоту использованания 10 цифр (от 0 до 9).
    """

    try:
        a = init_int("\nВведите начало диапазона: ")
        b = init_int("Введите конец диапазона: ")
        if a > b:
            print("\nНачало диапазона не может быть больше конца!\n")
        else:
            res = foo(a, b)
            print(f"\nЧастота использования цифр в диапазоне от {a} до {b}:")
            d = {}
            for i in range(10):
                d[str(i)] = 0
            for i in res:
                if i != '-':
                    d[i] += 1
            for key in d:
                print(f"Цифра {key}: {d[key]}")
    except ValueError:
        print("\nВведена строка или не целое число!\n")


if __name__ == '__main__':
    main()
