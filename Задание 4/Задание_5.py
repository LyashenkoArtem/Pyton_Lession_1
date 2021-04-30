my_set = [el for el in range (100, 1001, 2)]
print(f'Списко всех четных от 100 до 1000: {my_set}')


from functools import reduce

pro_all = reduce(lambda x, y: x * y, my_set)
print(f'Произведение всех четных от 100 до 1000: {pro_all}')