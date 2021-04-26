my_list = [7, 5, 3, 3, 2]

a = int(input('Add number '))
c = my_list.count(a)
for element in my_list:
    if c > 0:
        i = my_list.index(a)
        my_list.insert(i+c, a)
        break
    else:
        if a > element:
            j = my_list.index(element)
            my_list.insert(j, a)
            break
        elif a < my_list[len(my_list) - 1]:
            my_list.append(a)
print(my_list)
