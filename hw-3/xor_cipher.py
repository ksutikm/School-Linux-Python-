from itertools import cycle

def cipher(data, key):
    """
    Алгоритм шифрования XOR
    """
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(data, cycle(key)))

def main():
    """
    Пользователь вводит сообещение и ключ на вход.
    Скрипт засшифровывает сообщение, а потом расшифровывает его
    и проверяет успешно  прошло шифрование или нет.
    """

    data = input("Введите сообщение: ")
    key = input("Введите ключ: ")
    crypted = cipher(data, key)
    decrypted = cipher(crypted, key)

    print(f"\nЗасшифрованный текст:\n{crypted}")
    print(f"\nРасшифрованный текст:\n{decrypted}")

    if data == decrypted:
        print("\nИтог: шифрование прошло успешно")
    else:
        print("\nИтог: шифрование провалено")

if __name__ == '__main__':
    main()