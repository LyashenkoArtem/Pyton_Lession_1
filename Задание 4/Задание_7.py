import math

fact = (1, 2, 3, 4, 5)
def generator():
    for el in fact:
        yield el

g = generator()
print(g)


for el in g:
    a = math.factorial(el)
    print(a)
