# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player) == True:
                print("Game Over!")
                sys.exit()


            for shot in shots:
                if shot.check_collisions(asteroid) == True:
                    shot.kill()
                    asteroid.split()



        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
