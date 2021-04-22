a = int(input('Введите номер месяца '))

if a > 0 and a <= 12:
    my_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
               'Октябрь', 'Ноябрь', 'Декабрь']
    i = (a - 1)
    print(my_list[i])

else:
    print('Введен неверный номер месяца')
    quit()

list_year = ['Зима', 'Весна', 'Лето', 'Осень']
if a==1 or a==2 or a==12:
    print(list_year[0])
elif a==3 or a==4 or a==5:
    print(list_year[1])
elif a == 6 or a == 7 or a == 8:
    print(list_year[2])
else:
    print(list_year[3])


my_dict = {1:'Winter', 2:'Spring', 3:'Summer',4:'Autumn'}
if a==1 or a==2 or a==12:
    print(my_dict.get(1))
elif a==3 or a==4 or a==5:
    print(my_dict.get(2))
elif a == 6 or a == 7 or a == 8:
    print(my_dict.get(3))
else:
    print(my_dict.get(4))