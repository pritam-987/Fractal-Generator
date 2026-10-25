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

# load assets
serpinski_triangle_image = pygame.image.load(
    "assets/Sierpinski_triangle.png"
).convert_alpha()
mandlebrot_set_image = pygame.image.load("assets/Sprite-0004.png").convert_alpha()

# load font
font = pygame.font.SysFont(pygame.font.get_default_font(), 50)
# render text
text = font.render("Press Escape to reset", True, WHITE)
text_rect = text.get_rect()

# load buttons
serpinski_triangle_button = Button(
    window,
    WIDTH // 2,
    HEIGHT,
    serpinski_triangle_image,
    serpinski_triangle_image.get_width(),
    serpinski_triangle_image.get_height(),
)
mandlebrot_button = Button(
    window,
    WIDTH,
    HEIGHT // 2 + 150,
    mandlebrot_set_image,
    mandlebrot_set_image.get_width(),
    mandlebrot_set_image.get_height(),
)

triangle = [[200, 10], [10, 390], [390, 390]]
serpinski = Serpinski(window, 200, 200, 500000)

malbrode_set = MalbrodeSet(window, WIDTH, HEIGHT)

game_state = None  # None: Menu


def main():
    global game_state
    while True:
        clock.tick(60)

        # main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and game_state == "mandlebrot":
                    x, y = event.pos
                    malbrode_set.zoom(x, y)
                    print(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = None  # Return to menu
            # malbrode_set.mandlebrot()
        if game_state is None:
            window.fill(BLACK)
            # draw the text
            window.blit(text)

            if serpinski_triangle_button.draw():
                window.fill(BLACK)
                serpinski.reset(200, 200)
                game_state = "serpinski"

            elif mandlebrot_button.draw():
                window.fill(BLACK)

                malbrode_set.mandlebrot()
                game_state = "mandlebrot"

        elif game_state == "serpinski":
            serpinski.chaos_game(WHITE, triangle)

            if serpinski.points >= serpinski.max_points:
                game_state = "showing_serpinski"

        elif game_state == "mandlebrot":
            pass

        elif game_state == "showing_serpinski":
            pass

        pygame.display.flip()


if __name__ == "__main__":
    main()
