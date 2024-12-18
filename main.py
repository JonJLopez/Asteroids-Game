import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    astroidfield = AsteroidField()

    dt = 0
    clock = pygame.time.Clock()

    while(1):
        #close button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill background
        screen.fill(0)

        #update position of entities
        for entity in updatable:
            entity.update(dt)

        #check for collision
        for entity in asteroids:
            for shot in shots:
                if entity.colliding_with(player):
                    print("Game over!")
                    return
                if entity.colliding_with(shot):
                    entity.split()
                    shot.kill()

        #draw entities at new positions
        for entity in drawable:
            entity.draw(screen)

        #refresh screen at 60 fps
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()