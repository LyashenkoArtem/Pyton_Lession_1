a = int(input('Введите любое число от 1 до 10: '))

from itertools import count

for el in count(a):
    if el > 10:
        break
    else:
        print(el)


b = ('abcd')
from itertools import cycle
c = 0
for el in cycle(b):
    if c > 15:
        break
    else:
        print(el)
        c = c + 1