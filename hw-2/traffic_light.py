def traffic_light():
    '''
    Скрипт "Светофор", который запрашивает сигнал светофора,
    после чего разрешает или не разрешает движение
    '''
    data = ['красный', 'желтый', 'жёлтый', 'зеленый', 'зелёный']
    str = input('Введите сигнал светофора: ').lower().strip()
    assert str in data, 'Введен неправильный сигнал светофора!'
    if str == data[0]:
        print('Стой!')
    elif str == data[1] or str == data[2]:
        print('Подожди!')
    elif str == data[3] or str == data[4]:
        print('Иди!')

if __name__ == '__main__':
    traffic_light()