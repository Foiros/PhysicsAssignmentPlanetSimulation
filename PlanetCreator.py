import Planet


def create_planet(name, x, y, radius, color, mass, y_vel):
    new_planet = Planet.Planet(name, x, y, radius, color, mass, y_vel)
    return new_planet
