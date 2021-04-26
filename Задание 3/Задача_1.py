def first_func():
    num_1 = int(input('Введите делимое: '))
    num_2 = int(input('Введите делитель: '))
    if num_2 != 0:
        num_3 = num_1 / num_2
        return num_3

    else:
        print('Невозможно разделить на 0')

a = first_func()

print(f'Частное равно:{a}')