class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def coat(self):
        V = self.size / 6.5 + 0.5
        return round(V, 2)

    def growth(self):
        H = self.height * 2 + 0.3
        return round(H, 2)

    @property
    def total_consumption(self):
        sum_cloth = cloth_size.coat() + cloth_size.growth()
        return round(sum_cloth, 1)

cloth_size = Clothes(48, 10)
print(cloth_size.coat())
print(cloth_size.growth())
print(cloth_size.total_consumption)