def traffic_light():
    data = ['красный', 'желтый', 'жёлтый', 'зеленый']
    str = input('Введите сигнал светофора: ').lower().strip()
    assert str in data, 'Введен неправильный сигнал светофора'
    if str == data[0]:
        print('Стой!')
    elif str == data[1] or str == data[2]:
        print('Подожди!')
    elif str == data[3]:
        print('Иди!')

traffic_light();