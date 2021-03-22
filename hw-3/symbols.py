def main():
    """
    Пользователь вводит строку, в коносль выводится
    частота использования символов в тексте.
    """
    data = get_data()
    if data.isdigit():
        print("Строка должна состоять из символов, а не из цифр")
    else:
        d = {}
        for s in data:
            if s in d.keys():
                d[s] += 1
            else:
                d[s] = 1
        for key, value in sorted(d.items(), key=lambda x: x[0]):
            print("{} = {}".format(key if key != '\n' else '\\n', value))

def get_data():
    data = input("Введите строку: ")

    if not data:
        data = """
Shakespeare "Romeo and Juliet" (PROLOGUE)

# Two households, both alike in dignity,
# In fair Verona, where we lay our scene,
# From ancient grudge break to new mutiny,
# Where civil blood makes civil hands unclean.
# From forth the fatal loins of these two foes
# A pair of star-cross'd lovers take their life;
# Whose misadventured piteous overthrows
# Do with their death bury their parents' strife.
# The fearful passage of their death-mark'd love,
# And the continuance of their parents' rage,
# Which, but their children's end, nought could remove,
# Is now the two hours' traffic of our stage;
# The which if you with patient ears attend,
# What here shall miss, our toil shall strive to mend."""

    return data

if __name__ == '__main__':
    main()