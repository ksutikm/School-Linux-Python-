def main():
    a = ['h', 'e', 'l', 'l', 'o']
    b = ['h', 'e', 'l', 'l', 'e', 'h', 'o', 'o']

    print(f'Список a: {a}')
    print(f'Список b: {b}')
    if set(a) - set(b) == set():
        print('Множества этих списков совпадают')
    else:
        print('Множества этих списков не совпадают')

if __name__ == '__main__':
    main()