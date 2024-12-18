import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    dt = 0
    clock = pygame.time.Clock()

    while(1):
        #close button functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()