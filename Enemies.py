from Bullet import Bullet
import math


class Enemy:
    def __init__(self, x_, y_):
        self.hp = 100
        self.speed = 1
        self.damage = 10
        self.x = x_
        self.y = y_

    def move(self, hero_x, hero_y):
        if hero_x > self.x:
            self.x += 1
        if hero_x < self.x:
            self.x -= 1
        if hero_y > self.y:
            self.y += 1
        if hero_y < self.y:
            self.y -= 1

    def dealing_damage(self, d):
        self.hp -= d
        if self.hp <= 0:
            return 0
        else:
            return 1

    def attack(self):
        alpha = math.pi / 2
        bullet = Bullet(self.x, self.y, self.damage, alpha)
        return bullet

    def get_coor(self):
        return self.x, self.y
