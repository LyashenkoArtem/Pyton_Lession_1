def first_func():
    data_1 = input('Введите Имя пользователя: ')
    data_2 = input('Введите Фамилию пользователя: ')
    data_3 = input('Введите год рождения пользователя: ')
    data_4 = input('Введите город проживания: ')
    data_5 = input('Введите email: ')
    data_6 = input('Введите номер телефона: ')

    all_data = data_1 + ' ' + data_2 + ', ' + data_3 + ' года рождения ' + ', проживающий в городе ' + data_4 + ', ' + data_5 + ', ' + data_6
    return all_data

a = first_func()

print(f'Вы зарегистрировались как: {a}')