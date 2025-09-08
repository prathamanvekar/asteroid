import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.max_radius = radius + 30
        self.lifespan = 0.5  # seconds
        self.current_radius = 5

    def update(self, dt):
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

        # Grow the explosion
        self.current_radius += 1

    def draw(self, screen):
        # Draw a simple expanding circle
        pygame.draw.circle(screen, "orange", self.position, int(self.current_radius), 2)
