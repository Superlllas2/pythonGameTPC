import math


class Bullet():
    def __init__(self, x_, y_, d_, alpha):
        self.x = x_
        self.y = y_
        self.damage = d_
        self.speed = 10
        self.alpha = alpha

    def move(self):
        self.x += self.speed * math.cos(self.alpha)
        self.y += self.speed * math.sin(self.alpha)

    def get_coor(self):
        return self.x, self.y
