from circleshape import CircleShape
import pygame
from constants import *
import random
from explosion import Explosion

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        Explosion(self.position.x, self.position.y, self.radius)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        googoo = self.velocity.rotate(random_angle)
        gaagaa = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        lol = Asteroid(self.position.x, self.position.y, new_radius)
        lmao = Asteroid(self.position.x, self.position.y, new_radius)
        lol.velocity = googoo * 1.2
        lmao.velocity = gaagaa * 1.2
