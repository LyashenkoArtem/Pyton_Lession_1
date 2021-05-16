class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Клеточки слились, теперь у вас их еще больше: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Упс, клетка исчезли, их количество уменьшилось до {sub}' if sub > 0 else 'Теперь клеток нет!'

    def __truediv__(self, other):
        return f'Клетки поделились, теперь их {self.quantity // other.quantity}'

    def __mul__(self, other):
        return f'Клетки перемножились и теперь у вас МЕГАФЕРМА клеток, в количестве {self.quantity * other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return f'Посмотрите на них: {result}'


cell = Cell(int(input('Введите количество клеток, что у вас было: ')))
cell_2 = Cell(int(input('Введите количетво клеток, что вы добавили: ')))
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))