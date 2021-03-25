def check_braclets(s):
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    dictionary = {')': '(', '}': '{', ']': '['}
    stack = []
    for c in s:
        if c in open_brackets:
            stack.append(c)
        elif c in close_brackets:
            if len(stack) <= 0 or stack.pop() != dictionary[c]:
                return 'Неправильное количество скобок!'

    if len(stack) == 0:
        return 'Все скобки раставлены верно!'
    else:
        return'Неправильное количество скобок!'


def main():
    s = input('Введите строку: ')
    print(check_braclets(s))


if __name__ == '__main__':
    main()
