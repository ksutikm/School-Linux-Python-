def calc():
    """
    Калькулятор для расчета базовых операций:
        "+" - сложение
        '-' - вычитание
        '*' - умножение
        '/' - деление
        '**' - возведение в степень
    """
    with open('./example.txt') as f:
        example = f.read()
    if example:
        if check_brackets(example):
            stack = example.split()
            new_stack = infix_to_postfix(stack)
            print(f'Результат вычисления: {calc_posfix(new_stack):.2f}')
        else:
            print('Ошибка в примере: неправильное количество скобок!')
    else:
        print('Введен не пример, попробйте ещё раз!')

def check_brackets(s):
    """ Проверка скобок """
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) <= 0 or stack.pop() != '(':
                return False

    if len(stack) == 0:
        return True
    return False

def infix_to_postfix(stack):
    """
    Переход от инфиксной записи в постфиксную
    (От прямой польской записи в обратную)
    """
    prioritet = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    postfix, op_stack = [], []
    for elem in stack:
        if check_digit(elem):
            postfix.append(elem)
        elif elem == '(':
            op_stack.append(elem)
        elif elem == ')':
            top = op_stack.pop()
            while top != '(':
                postfix.append(top)
                top = op_stack.pop()
        else:
            while op_stack and prioritet[op_stack[len(op_stack) - 1]] >= prioritet[elem]:
                postfix.append(op_stack.pop())
            op_stack.append(elem)
    while op_stack:
        postfix.append(op_stack.pop())
    return postfix

def calc_posfix(stack):
    """ Вычисление постфиксной записи """
    digits_stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    for elem in stack:
        if check_digit(elem):
            digits_stack.append(int(elem))
        else:
            a, b = digits_stack.pop(), digits_stack.pop()
            result = operators[elem](b, a)
            digits_stack.append(result)
    return digits_stack.pop()

def check_digit(n):
    """ Проверка объекта на число """
    if n.isdigit():
        return True
    elif n[0] == '-' and n[1:].isdigit():
        return True
    return False

if __name__ == '__main__':
    calc()