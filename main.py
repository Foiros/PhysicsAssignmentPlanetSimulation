import pygame
import sys
import Planet
import PlanetCreator

pygame.init()

WIDTH, HEIGHT = 1900, 1000
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

    # Colors list
    colors = [WHITE, YELLOW, BLUE, RED, DARK_GREY, GREEN, BLACK]

    # Available Planet names
    planet_names = ["Earth", "Mars", "Venus", "Mercury", "Jupiter", "Uranus", "Saturn", "Neptune", "Orion",
                    "Tatooine", "Endor", "Kashyyk", "Flappy", "Otaku"]

    # Button texts
    title_text = TITLE_FONT.render("Planet Simulation 3000", True, RED)
    start_button_text = TITLE_FONT.render("Start", True, BLACK)
    stop_button_text = TITLE_FONT.render("Stop", True, BLACK)
    quit_button_text = TITLE_FONT.render("Quit", True, BLACK)
    remove_button_text = TITLE_FONT.render("Remove Planet", True, BLACK)
    create_button_text = TITLE_FONT.render("Create Planet", True, BLACK)

    # Button locations on screen - Start, Stop, Quit
    start_button_rect = pygame.Rect(800, 750, 200, 100)
    stop_button_rect = pygame.Rect(1200, 0, 200, 100)
    quit_button_rect = pygame.Rect(300, 750, 200, 100)

    # Planet removal button locations
    remove_button_rect = pygame.Rect(750, 500, 300, 100)
    displayed_planet_rect = pygame.Rect(750, 300, 200, 100)
    remove_right_switch_rect = pygame.Rect(1050, 500, 50, 50)
    remove_left_switch_rect = pygame.Rect(650, 500, 50, 50)

    # Planet Creation button locations
    create_button_rect = pygame.Rect(200, 500, 300, 100)
    planet_name_rect = pygame.Rect(350, 50, 100, 50)
    planet_x__rect = pygame.Rect(350, 150, 100, 50)
    planet_radius_rect = pygame.Rect(350, 250, 100, 50)
    planet_color_rect = pygame.Rect(350, 350, 100, 50)
    planet_mass_rect = pygame.Rect(350, 450, 100, 50)
    planet_y_vel_rect = pygame.Rect(500, 450, 100, 50)



    # Planets
    sun = PlanetCreator.create_planet("Sun", 0, 0, 30, YELLOW, 1.98892 * 10 ** 30, 0)
    sun.sun = True

    earth = PlanetCreator.create_planet("Earth", -1 * Planet.Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24, 29.783 * 1000)

    mars = PlanetCreator.create_planet("Mars", -1.524 * Planet.Planet.AU, 0, 12, RED, 6.39 * 10 ** 23, 24.7077 * 1000)

    mercury = PlanetCreator.create_planet("Mercury", 0.387 * Planet.Planet.AU, 0, 8, DARK_GREY, 0.330 * 10 ** 24, -47.4 * 1000)

    venus = PlanetCreator.create_planet("Venus", 0.723 * Planet.Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24, -35.02 * 1000)

    planets = [sun, earth, mars, mercury, venus]

    # Index of the planet to displayed or removed planet
    planet_index = 0
    color_index = 0
    planet_name_index = 0

    # Planet creation values
    # planet_name = "Jupiter"
    # planet_x = 5.2 * Planet.Planet.AU
    # planet_y = 0
    # planet_radius = 20
    # planet_color = GREEN
    # planet_mass = 1.8982 * 10 ** 27
    # planet_y_vel = 37 * 1000

    planet_name = "Jupiter"
    planet_x = -1.323 * Planet.Planet.AU
    planet_y = 0
    planet_radius = 19
    planet_color = GREEN
    planet_mass = 1.8982 * 10 ** 27
    planet_y_vel = 30 * 1000

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

                if quit_button_rect.collidepoint(event.pos):
                    run = False

                if remove_button_rect.collidepoint(event.pos):
                    if planet_index != 0:
                        planets.pop(planet_index)
                        planet_index = 0

                if remove_right_switch_rect.collidepoint(event.pos):
                    if planet_index == (len(planets) - 1):
                        planet_index = 0
                    else:
                        planet_index += 1

                if remove_left_switch_rect.collidepoint(event.pos):
                    if planet_index == 0:
                        planet_index = (len(planets) - 1)
                    else:
                        planet_index -= 1

                if create_button_rect.collidepoint(event.pos):
                    new_planet = PlanetCreator.create_planet(planet_name,
                                                             planet_x,
                                                             planet_y,
                                                             planet_radius,
                                                             planet_color,
                                                             planet_mass,
                                                             planet_y_vel)
                    planets.append(new_planet)

                if planet_name_rect.collidepoint(event.pos):
                    if planet_name_index == (len(planet_names) - 1):
                        planet_name_index = 0
                        planet_name = planet_names[planet_name_index]
                    else:
                        planet_name_index += 1
                        planet_name = planet_names[planet_name_index]


                if planet_x__rect.collidepoint(event.pos):
                    if planet_x >= 1 * Planet.Planet.AU:
                        planet_x = -1.524 * Planet.Planet.AU
                    else:
                        planet_x += 0.1 * Planet.Planet.AU

                if planet_radius_rect.collidepoint(event.pos):
                    if planet_radius == 20:
                        planet_radius = 1
                    else:
                        planet_radius += 1

                if planet_color_rect.collidepoint(event.pos):
                    if color_index == (len(colors) - 1):
                        color_index = 0
                        planet_color = colors[color_index]
                    else:
                        color_index += 1
                        planet_color = colors[color_index]

                if planet_mass_rect.collidepoint(event.pos):
                    if planet_mass >= 1.8982 * 10 ** 27:
                        planet_mass = 0
                    else:
                        planet_mass += 0.0001 * 10 ** 27

                if planet_y_vel_rect.collidepoint(event.pos):
                    if planet_y_vel >= 30 * 1000:
                        planet_y_vel = -50 * 1000
                    else:
                        planet_y_vel += 1 * 1000





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

            pygame.draw.rect(WIN, BLUE, pygame.Rect(300, 100, 800, 800))
            WIN.blit(title_text, (500, 100))

            pygame.draw.rect(WIN, GREEN, start_button_rect)
            WIN.blit(start_button_text, (850, 770))

            pygame.draw.rect(WIN, RED, remove_button_rect)
            WIN.blit(remove_button_text, (750, 500))

            pygame.draw.rect(WIN, RED, quit_button_rect)
            WIN.blit(quit_button_text, (300, 770))

            pygame.draw.rect(WIN, planets[planet_index].color, displayed_planet_rect)
            WIN.blit(TITLE_FONT.render(planets[planet_index].name, True, BLACK), (750, 300))

            pygame.draw.rect(WIN, BLACK, remove_right_switch_rect)
            pygame.draw.rect(WIN, BLACK, remove_left_switch_rect)

            pygame.draw.rect(WIN, GREEN, create_button_rect)
            WIN.blit(create_button_text, (200, 500))

            pygame.draw.rect(WIN, DARK_GREY, planet_name_rect)
            WIN.blit(FONT.render(planet_names[planet_name_index], True, BLACK), (350, 50))

            pygame.draw.rect(WIN, DARK_GREY, planet_x__rect)
            WIN.blit(FONT.render('{a} km'.format(a=planet_x), True, BLACK), (350, 150))

            pygame.draw.rect(WIN, DARK_GREY, planet_radius_rect)
            WIN.blit(FONT.render('Radius: {a}'.format(a=planet_radius), True, BLACK), (350, 250))

            pygame.draw.rect(WIN, colors[color_index], planet_color_rect)

            pygame.draw.rect(WIN, DARK_GREY, planet_mass_rect)
            WIN.blit(FONT.render('{a} kg'.format(a=planet_mass), True, BLACK), (350, 450))

            pygame.draw.rect(WIN, DARK_GREY, planet_y_vel_rect)
            WIN.blit(FONT.render('{a} km/h'.format(a=planet_y_vel), True, BLACK), (500, 450))

        pygame.display.update()

    pygame.quit()
    sys.exit()


main()
