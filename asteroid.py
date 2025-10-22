import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        theta = random.uniform(20, 50)

        path1 = self.velocity.rotate(theta)
        path2 = self.velocity.rotate(-theta)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid1.velocity = path1 * 1.2
        new_asteroid2.velocity = path2 * 1.2