
a = int(input('Введите целое число n от 1 до 9 '))

if a > 0:
    if a < 10:
        print(f'сумма n+nn+nnn равна {a + (a * 11) + (a * 111)}')
    else: 
        print(f'Вы ввели число больше 10')
else: 
    print(f'Вы ввели число меньше 1')

