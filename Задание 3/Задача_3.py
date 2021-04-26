def my_func():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    num_3 = int(input('Введите третье число: '))
    if num_1 > num_3 and num_2 > num_3:
        num_summ = num_1 + num_2
        return num_summ
    elif num_1 > num_2 and num_3 > num_2:
        num_summ = num_1 + num_3
        return num_summ
    elif num_2 > num_1 and num_3 > num_1:
        num_summ = num_2 + num_3
        return num_summ
    elif (num_1 == num_2 and num_3 > num_2) or (num_2 == num_3 and num_1 > num_2) or (num_3 == num_1 and num_2 > num_1):
        print('Вы ввели два одинаковых числа, меньшее, чем третье')
    elif num_1 == num_2 == num_3:
        print('Вы ввели три одинаковых числа')


a = my_func()
print(f'Сумма наибольших чисел равна {a}')