a = int(input('Введите количество элементов вашего списка '))

my_list = []
i = 0
el = 0

while i < a:
    my_list.append(input('Введите следующее значение списка '))
    i = i + 1

list1 = my_list[::2]
list2 = my_list[1::2]

i = 0
while i < (a / 2):
    print(list1[i], list2[i])
    i = i + 1


