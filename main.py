import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    clock = pygame.time.Clock()

    while(1):
        #close button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill background
        screen.fill(0)

        #draw entities
        for entity in updatable:
            entity.update(dt)

        for entity in drawable:
            entity.draw(screen)

        #refresh screen at 60 fps
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()