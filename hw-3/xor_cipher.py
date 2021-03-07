from itertools import cycle

def cipher(data, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(data, cycle(key)))

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