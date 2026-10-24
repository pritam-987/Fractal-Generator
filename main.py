import sys

import pygame

from button import Button
from malbrode_set import MalbrodeSet
from serpinski_triangle import Serpinski

pygame.init()
WIDTH, HEIGHT = 800, 600
# clolours:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


serpinski_triangle_image = pygame.image.load(
    "assets/Sierpinski_triangle.png"
).convert_alpha()
serpinski_triangle_button = Button(
    window,
    WIDTH // 2,
    HEIGHT // 2,
    serpinski_triangle_image,
    serpinski_triangle_image.get_width(),
    serpinski_triangle_image.get_height(),
)

triangle = [[200, 10], [10, 390], [390, 390]]
serpinski = Serpinski(window, 200, 200, 500000)

malbrode_set = MalbrodeSet(window, WIDTH, HEIGHT)

running = False


def main():
    global running
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    malbrode_set.zoom(x, y)
        if not running:
            window.fill(BLACK)
            malbrode_set.mandlebrot()
        else:
            None

        pygame.display.update()


if __name__ == "__main__":
    main()
