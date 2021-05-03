with open('Zarplata', 'r') as object:
    sal = []
    poor = []
    my_list = object.read().split('\n')
    print(my_list)
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20000 {poor}, Средний оклад {sum(map(int, sal)) / len(sal)}')