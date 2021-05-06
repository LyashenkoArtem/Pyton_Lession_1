# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'поехал'

    def stop(self):
        return ', а затем остановился'

    def turn(self, direction):
        return f'повернул на{direction}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы привысили скорость! Ваша скорость {self.speed}!')
            return self.speed
        else:
            print(f'Ваша скорость {self.speed}')
            return self.speed


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы привысили скорость! Ваша скорость {self.speed}!')
            return self.speed
        else:
            print(f'Ваша скорость {self.speed}')
            return self.speed

class PoliceCar(Car):
    pass

# TownCar, SportCar, WorkCar, PoliceCar
# speed, color, name, is_police (булево).

tc = TownCar(80, 'Red', 'Mini', False)
print(f'Автомобиль {tc.name + " " + tc.color} цвета {tc.go()} со скоростью {tc.show_speed()} и {tc.turn("право")}{tc.stop()}\n')

sc = SportCar(180, 'White', 'Jaguar', False)
print(f'Автомобиль {sc.name + " " + sc.color} цвета {sc.go()} со скоростью {sc.speed} и {sc.turn("лево")}{sc.stop()}\n')

wc = WorkCar(50, 'Black', 'WV', False)
print(f'Автомобиль {wc.name + " " + wc.color} цвета {wc.go()} со скоростью {wc.show_speed()} и {wc.turn("назад")}{wc.stop()}\n')

pc = PoliceCar(70, 'White', 'Priora', True)
print(f'Автомобиль {pc.name + " " + pc.color} цвета {pc.go()} со скоростью {pc.speed} и {pc.turn("кругом")}{pc.stop()}\n')


