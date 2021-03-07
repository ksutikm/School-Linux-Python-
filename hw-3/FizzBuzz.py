"""
Напишите программу, которая выводит на экран числа от 0 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5,
то программа должна выводить слово «FizzBuzz»
"""
def way_1():
    for i in range(101):
        print('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i)

def way_2():
    list = []
    for i in range(101):
        list.append('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i)
    print(list)

def way_3():
    for i in range(101):
        n, f, b = str(i), 'Fizz', 'Buzz'
        if i%3!=0: f=''
        else: n=''
        if i%5!=0: b=''
        else: n=''
        print(n+f+b)

print("Решение 1:")
way_1()
print("\n\nРешение 2:")
way_2()
print("\n\nРешение 3:")
way_3()