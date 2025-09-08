# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from explosion import Explosion
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group() # Add this

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (explosions, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    score = 0
    font = pygame.font.Font(None, 36)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        # ... after drawing the score
        for i in range(player.lives):
            # Create a small triangle for the life icon
            life_icon = [
                (SCREEN_WIDTH - 30 - i * 30, 30),
                (SCREEN_WIDTH - 45 - i * 30, 45),
                (SCREEN_WIDTH - 15 - i * 30, 45)
            ]
            pygame.draw.polygon(screen, "white", life_icon, 2)

        for thing in drawable:
            thing.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if not player.invincible and asteroid.check_collisions(player) == True:
                player.lives -= 1
                if player.lives > 0:
                    player.respawn()
                else:
                    print("Game Over!")
                    sys.exit()


            for shot in shots:
                if shot.check_collisions(asteroid) == True:
                    shot.kill()
                    if asteroid.radius > ASTEROID_MIN_RADIUS * 2:
                        score += 10
                    elif asteroid.radius > ASTEROID_MIN_RADIUS:
                        score += 20
                    else:
                        score += 50
                    asteroid.split()



        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
