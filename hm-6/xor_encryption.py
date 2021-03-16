from random import randint, choice

def cipher(file='./text.txt'):
    with open(file, 'rb') as f:
        data = f.read()
    key = input('Введите ключ или Enter(автоматическая генерация ключа)')

    len_data = len(data)
    if not key:
        key = ''.join(
            choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            for _ in range(randint(1, 500 if len_data > 500 else len_data))
        )
        print(f'Автоматически сгенерированный ключ:\n{key}')

    ans = bytearray()
    if type(data) == str:
        data = bytearray(data, 'utf-8')
    key = bytearray(key, 'utf-8')

    len_key = len(key)
    for i in range(len(data)):
        ans.append(data[i] ^ key[i % len_key])

    with open(file, 'wb') as f:
        f.write(ans)

if __name__ == "__main__":
    cipher('./War and Peace.txt')