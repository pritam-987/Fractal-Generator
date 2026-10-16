import sys

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
        window.fill((0, 0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
