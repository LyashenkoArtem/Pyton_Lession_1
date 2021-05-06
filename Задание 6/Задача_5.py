# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Some staff'

class Pen(Stationery):
    def draw(self):
        return self.title


class Pancil(Stationery):
    def draw(self):
        return self.title


class Handle(Stationery):
    def draw(self):
        return self.title

pen = Pen('Pen')
penc = Pancil('Pancil')
hand = Handle('Handle')
stat = Stationery('Stationery')

print(pen.draw())
print(penc.draw())
print(hand.draw())
print(stat.draw())
