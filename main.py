import sys

import pygame

from button import Button
from serpinski_triangle import Serpinski

pygame.init()
WIDTH, HEIGHT = 800, 600
# clolours:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

triangle = [[200, 10], [10, 390], [390, 390]]


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

running = False
serpinski = Serpinski(window, 200, 200, triangle, 5000)


def main():
    global running
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
        if not running:
            window.fill(BLACK)
        else:
            None
        if not running:
            if serpinski_triangle_button.draw():
                serpinski.reset(200, 200)
                running = True
        else:
            serpinski.chaos_game(WHITE, triangle)
            if serpinski.points >= serpinski.max_points:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
