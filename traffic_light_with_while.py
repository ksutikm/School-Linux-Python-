def traffic_light():
    data = ['красный', 'желтый', 'жёлтый', 'зеленый', 'зелёный', 'выход']
    while True:
        str = input('Введите сигнал светофора (завершение скрипта - команда "выход"): ').lower().strip()
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

traffic_light()