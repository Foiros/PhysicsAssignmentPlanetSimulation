import pygame


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_velo = 0

    def draw(self, win, width, height):
        x = self.x * self.SCALE + width / 2
        y = self.y * self.SCALE + height / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)
