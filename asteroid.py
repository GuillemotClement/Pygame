import random

import pygame.draw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # genere la direction
            rand = random.uniform(20, 50)
            direction_1 = self.velocity.rotate(-rand)
            direction_2 = self.velocity.rotate(rand)

            # reduction du radius de l'ateroid
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            x = self.position[0]
            y = self.position[1]

            astr1 = Asteroid(x, y, new_radius)
            astr2 = Asteroid(x, y, new_radius)

            astr1.velocity = direction_1 * 1.2
            astr2.velocity = direction_2 * 1.2

            return astr1, astr2
