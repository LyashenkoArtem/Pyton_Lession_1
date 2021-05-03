with open('Space', 'r') as file:
    num = file.read().split()
    sum_num = 0
    for el in num:
        sum_num = sum_num + int(el)
print(num)
print(sum_num)