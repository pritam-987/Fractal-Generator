import random
import sys

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
# clolours:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

triangle = [[200, 10], [10, 390], [390, 390]]


def chaos_game(pos):
    x, y = [200, 200]
    i = 0
    while i < 1000000:
        cx, cy = random.choice(pos)
        x = (x + cx) / 2
        y = (y + cy) / 2
        i += 1
        pygame.draw.circle(window, WHITE, (x, y), 1)


def main():
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
        window.fill(BLACK)
        chaos_game(triangle)
        pygame.display.update()


if __name__ == "__main__":
    main()
