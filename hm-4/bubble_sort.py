from random import randint

"""
Сортировка методом пузырька
"""
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

try:
    print("Введите количество элементов в массиве или Enter(массив будет придуман за вас): ")
    s = input("Ввод: ")
    a = []
    if not s:
        for _ in range(randint(5, 15)):
            a.append(randint(-100, 100))
        print()
    else:
        for _ in range(int(s)):
            a.append(int(input('Введите целое число: ')))

    bubble_sort(a)
    print(f'Отсортированный массив:\n{a}')

except ValueError:
    print('Введено не число!')
