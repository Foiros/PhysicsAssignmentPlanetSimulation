import pygame
import math
import Planet

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)


def main():
    run = True
    clock = pygame.time.Clock()

    # Planeetan luonnille vois mieluummin tehdä oman metodin
    sun = Planet.Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet.Planet(-1 * Planet.Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)

    mars = Planet.Planet(-1.524 * Planet.Planet.AU, 0, 12, RED, 6.39 * 10**23)

    mercury = Planet.Planet(0.387 * Planet.Planet.AU, 0, 8, DARK_GREY, 0.330 * 10**24)

    venus = Planet.Planet(0.723 * Planet.Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN, WIDTH, HEIGHT)

        pygame.display.update()

    pygame.quit()


main()
