# import pygame
#
#
# class Camera:
#     def __init__(self, width, height):
#         self.camera = pygame.Rect(0, 0, width, height)
#         self.height = height
#         self.width = width
#
#     def apply(self, entity):
#         return entity.rect.move(self.camera.topleft)
#
#     def update(self, target):
#         x = -target.rect.x + int(width / 2)
#         y = -target.rect.y + int(height / 2)
#         self.camera = pygame.Rect(x, y, self.width, self height)
