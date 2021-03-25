from itertools import cycle


def cipher(data, key):
    """
    Алгоритм шифрования XOR
    """
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(data, cycle(key)))


def main():
    """
    Пользователю предлагается на выбор 3 действия:
        1. XOR шифрование
        2. XOR расшифрование
        3. Выход
    Первое выполняет шифрование сообщения, поданного на вход.
    Второе выполняет расшифрование сообщения, поданного на вход.
    Третье - выход из скрипта
    """
    while True:
        input_data = ['1', '2', '3']
        print("\nВыберите один из пунтков:\n  1. XOR шифрование\n  2. XOR расшифрование\n  3. Выход")
        message = input("Ваш выбор: ").strip()
        if not message in input_data:
            print("\nДанные введены не корректно!\nНужно ввести 1, 2 или 3.\n")
            continue
        if message == input_data[2]:
            break
        else:
            data = input("Введите сообщение: ")
            key = input("Введите ключ: ")
            text = cipher(data, key)
            if message == input_data[0]:
                print(f"\nЗасшифрованный текст:\n{text}")
            else:
                print(f"\nРасшифрованный текст:\n{text}")


if __name__ == '__main__':
    main()
