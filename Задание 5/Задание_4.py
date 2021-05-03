rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('Numbers') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with open('Numbers_rus', 'w') as file_2:
    file_2.writelines(new_file)