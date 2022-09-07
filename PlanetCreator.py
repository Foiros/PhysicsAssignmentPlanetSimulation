import Planet


def create_planet(x, y, radius, color, mass, y_vel):
    new_planet = Planet.Planet(x, y, radius, color, mass, y_vel)
    return new_planet
