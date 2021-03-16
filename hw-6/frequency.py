def frequency(file='./War and Peace.txt'):
    with open(file) as f:
        data = f.read()
    frequency_list = list(map(lambda a: {a: data.count(a)}, set(data)))
    for i in frequency_list:
        print(i)


if __name__ == '__main__':
    frequency()