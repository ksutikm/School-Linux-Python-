"""
Подсчет частоты вхождений символов в тексте
"""
def symbols_text(s):
    dictionary = {}

    for symbol in s:
        dictionary[symbol] = dictionary.get(symbol, 0) + 1

    for key in sorted(dictionary):
        print(f'{key}: {dictionary[key]}')

'''
Подсчета количества слов в тексте
'''
def words_text(text):
    text = text.replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ')
    words = text.split(' ')
    for w in words:
        if w == '':
            words.remove(w)
    return len(words)

"""
Подсчет количества предложений в тексте
"""
def sentence_text(text):
    text.replace('\n', ' ')
    dots = text.count('.')
    exclamation_mark = text.count('!')
    question_mark = text.count('?')
    return dots + exclamation_mark + question_mark


data = input("Введите строку или Enter(за вас придумается строка): ")
if not data:
    data = """Shakespeare "Romeo and Juliet" (PROLOGUE)

Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose misadventured piteous overthrows
Do with their death bury their parents' strife.
The fearful passage of their death-mark'd love,
And the continuance of their parents' rage,
Which, but their children's end, nought could remove,
Is now the two hours' traffic of our stage;
The which if you with patient ears attend,
What here shall miss, our toil shall strive to mend."""

while True:
    print("""\nЧто вы хотите сделать:
  1. Подсчет частоты вхождений символов в тексте
  2. Подсчета количества слов в тексте
  3. Подсчет количества предложений в тексте
  4. Выход""")
    s = input('Ваш выбор (укажите цифру от 1 до 4): ')
    if not s in ['1', '2', '3', '4']:
        print("Неверный выбор, попробуйте еще раз!")
        continue
    if s == '1':
        print('Частота вхождений символов в тексте:')
        symbols_text(data)
    elif s == '2':
        print(f'Количество слов в тексте: {words_text(data)}')
    elif s == '3':
        print(f'Количество предложений в тексте: {sentence_text(data)}')
    else:
        break