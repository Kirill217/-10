class Clothes:
    def __init__(self, size):
        self.size = size
        # self.height = height

class Coet(Clothes):
    def coat(self):
        V = self.size / 6.5 + 0.5
        return round(V, 2)

class Growth(Clothes):
    def growth(self):
        H = self.size * 2 + 0.3
        return round(H, 2)

@property
class Total_consumption(Coet, Growth):
    def total_consumption(self):
        sum_cloth = cloth_size_coet.coat() + cloth_size_growth.growth()
        return round(sum_cloth, 1)


cloth_size_coet = Coet(48)
cloth_size_growth = Growth(180)
sum_cloth = Total_consumption

print(cloth_size_coet.coat())
print(cloth_size_growth.growth())
print(sum_cloth)


# print(cloth_size.coat())
# print(cloth_size.growth())
# print(cloth_size.total_consumption)