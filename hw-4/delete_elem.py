def main():
    old_list = input('Введите элементы списка через пробел:').split(' ')
    new_list = []
    for i in old_list:
        if not i in new_list:
            new_list.append(i)
    print(f'Список без повторяющихся элементов: {new_list}')

if __name__ == '__main__':
    main()