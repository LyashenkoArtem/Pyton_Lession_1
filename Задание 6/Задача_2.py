class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.height = 5


    def asphalt_mass(self):
        asphalt_mass = self.length * self.weight * self.height* self.weight
        print(f'Количество асфальта, для покрытия дорожного покрытия: {asphalt_mass}')

r = Road (5000, 20)
r.asphalt_mass()