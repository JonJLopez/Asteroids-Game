from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(rand_angle)
        vec2 = self.velocity.rotate(rand_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid1.velocity = vec1 * 1.2
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2.velocity = vec2

        