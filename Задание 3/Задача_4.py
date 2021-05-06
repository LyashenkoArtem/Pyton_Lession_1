# Первое решение, с использованием возведения в степень
def my_func():
    num_1 = int(input('Введите положительное действительное число '))
    num_2 = int(input('Введите целое отрицательное число '))
    if num_1 > 0 and num_2 < 0:
        num_summ = num_1 ** num_2
        return num_summ
    elif num_2 == 0:
        num_summ = 1
        return num_summ
    else:
        print('Вы ввели неверные числа')


a = my_func()
print(a)


# Второе решение
def my_func1():
    num_11 = int(input('Введите положительное действительное число '))
    num_12 = int(input('Введите целое отрицательное число '))
    i = 0
    b = 1
    if num_11 > 0 and num_12 < 0:
        d = (-1 * num_12)
        while i < d:
            b = b * num_11
            i = i+1
        b = 1 / b
        return b

    elif num_12 == 0:
        b = 1
        return b
    else:
        print('Вы ввели неверные числа')


с = my_func1()
print(с)