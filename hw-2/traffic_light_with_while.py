def traffic_light():
    '''
    Скрипт "Светофор" в бесконечном цикле с возможностью
    прекращения цикла по кодовому слову "выход"
    '''
    data = ['красный', 'желтый', 'жёлтый', 'зеленый', 'зелёный', 'выход']
    while True:
        str = input(
            'Введите сигнал светофора (завершение скрипта - команда "выход"): ').lower().strip()
        if str == data[5]:
            break
        elif not str in data:
            print('Введен неправильный сигнал светофора!')
        elif str == data[0]:
            print('Стой!')
        elif str == data[1] or str == data[2]:
            print('Подожди!')
        elif str == data[3] or str == data[4]:
            print('Иди!')


if __name__ == '__main__':
    traffic_light()
