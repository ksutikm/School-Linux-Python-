# Код с ошибками (*_incorrect) и испраленный вариант (*_correct)

# Ошибки типа SyntaxError
def syntax_error_incorrect()
    print("Hello, World!")

def syntax_error_correct():
    print("Hello, World!")

syntax_error_incorrect()
syntax_error_correct()

x, y = 1, 2
def syntax_error_incorect_2():
    if x = y:
        print('x = y')
    else:
        print('x != y')

def syntax_error_corect_2():
    if x == y:
        print('x = y')
    else:
        print('x != y')

syntax_error_incorect_2()
syntax_error_corect_2()

# Ошибка типа TypeError
def type_error_incorrect():
    print('Hi' + 5)

def type_error_correct():
    print('Hi' + str(5))

type_error_incorrect()
type_error_correct()

# Ошибка типа NameError
def name_erorr_incorrect(a):
    print(b)

def name_erorr_correct(a):
    print(a)

name_erorr_incorrect(42)
name_erorr_correct(42)

# Ошибка типа UnboundLocalError
def unbound_local_error_incorrect():
    print(a)
    a = 42

def unbound_local_error_correct():
    a = 42
    print(a)

unbound_local_error_incorrect()
unbound_local_error_correct()

# Ошибка типа IndentationError
def indentation_error_incorrect(a):
    if a % 2 == 0:
    else:
        print('нечетное')

def indentation_error_correct(a):
    if a % 2 == 0:
        print('четное')
    else:
        print('нечетное')

indentation_error_incorrect(42)
indentation_error_correct(42)

# Ошибка типа TabError
def tab_error_incorrect():
    print("Hello,")
	print('World!!!')

def tab_error_correct():
    print("Hello,")
    print('World!!!')

tab_error_incorrect()
tab_error_correct()