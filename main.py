import pygame
import sys
import Planet
import PlanetCreator

pygame.init()

WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
GREEN = (65, 239, 0)
BLACK = (0, 0, 0)

FONT = pygame.font.SysFont("comicsans", 16)
TITLE_FONT = pygame.font.SysFont("comicsans", 40)


def main():
    run = True
    simulation_started = False
    clock = pygame.time.Clock()

    title_text = TITLE_FONT.render("Planet Simulation 3000", True, RED)
    start_button_text = TITLE_FONT.render("Start", True, BLACK)
    stop_button_text = TITLE_FONT.render("Stop", True, BLACK)

    start_button_rect = pygame.Rect(800, 750, 200, 100)
    stop_button_rect = pygame.Rect(1200, 0, 200, 100)

    sun = PlanetCreator.create_planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30, 0)
    sun.sun = True

    earth = PlanetCreator.create_planet(-1 * Planet.Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24, 29.783 * 1000)

    mars = PlanetCreator.create_planet(-1.524 * Planet.Planet.AU, 0, 12, RED, 6.39 * 10 ** 23, 24.7077 * 1000)

    mercury = PlanetCreator.create_planet(0.387 * Planet.Planet.AU, 0, 8, DARK_GREY, 0.330 * 10 ** 24, -47.4 * 1000)

    venus = PlanetCreator.create_planet(0.723 * Planet.Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24, -35.02 * 1000)

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    simulation_started = True

                if stop_button_rect.collidepoint(event.pos):
                    simulation_started = False

        # Aloitamme simulaation pyörittämisen.
        if simulation_started:
            pygame.draw.rect(WIN, RED, stop_button_rect)
            WIN.blit(stop_button_text, (1250, 0))

            for planet in planets:
                planet.update_position(planets)
                planet.draw(WIN, WIDTH, HEIGHT, FONT, WHITE)
        # Käytännössä siis planeettojen luontiruutu. Kaiken laittaminen tämän elsen alle tulee olemaan aika tuskaista.
        # Siksi tulen siirtämään tämän osion omaan metodiin tai johonkin muuhun.
        else:
            for planet in planets:
                planet.reset_position()

            pygame.draw.rect(WIN, WHITE, pygame.Rect(300, 100, 800, 800))
            WIN.blit(title_text, (500, 100))
            pygame.draw.rect(WIN, GREEN, start_button_rect)
            WIN.blit(start_button_text, (850, 770))

        pygame.display.update()

    pygame.quit()
    sys.exit()


main()
