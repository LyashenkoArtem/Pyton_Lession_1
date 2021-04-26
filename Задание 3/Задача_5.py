def my_sum ():
    sum_res = 0
    exit = False
    while exit == False:
       num = input('Введите числа или нажмите Q для выхода: ')

       res = 0
       for el in range(len(num)):
           if num[el] == 'q' or num[el] == 'Q':
               exit = True
               break
           else:
               res = res + int(num[el])

       sum_res = sum_res + res
       print(f'Промежуточная сумма {sum_res}')
    print(f'Итоговая сумма {sum_res}')
my_sum()