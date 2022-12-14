
import pygame.draw

class Circle:

    def __init__(self, color, x, y, radius) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)