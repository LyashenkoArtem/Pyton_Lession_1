file = open('Text', 'w')
line = input('Введите текст:')
while line:
    file.writelines(line + '\n')
    line = input('Введите текст: ')
    if not line:
        break



