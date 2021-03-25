from functools import reduce


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения: {end-start} секунд.')
        return res
    return wrapper


def logging(func):
    """
    Декоратор, логирующий работу кода.
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('log result:', res)
        return res
    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    if not hasattr(counter, 'count'):
        counter.count = {}

    counter.count[func.__name__] = 0

    def wrapper(*args, **kwargs):
        counter.count[func.__name__] += 1
        res = func(*args, **kwargs)
        print(f"{func.__name__} была вызвана: {counter.count[func.__name__]}x")
        return res
    return wrapper


@benchmark
@logging
@counter
def reverse_string(string):
    return string[::-1]


print('Реверс строки:', reverse_string("А роза упала на лапу Азора"))
print('Реверс строки:', reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))
