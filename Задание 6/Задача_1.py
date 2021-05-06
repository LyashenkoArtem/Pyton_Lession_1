import time

class TrafficLight:
    _color = 'Красный'
    def runnung(self):
        print(f'Светофор включен')

        self._color = 'Красный'
        print(f'Загорается свет: {self._color}')
        time.sleep(7)

        self._color = 'Желтый'
        print(f'{self._color}')
        time.sleep(2)

        self._color = 'Зеленый'
        print(f'{self._color}')
        time.sleep(5)

        print('Работа светофора звершена')

traffic_light = TrafficLight()
print(traffic_light.runnung())
