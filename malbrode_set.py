import numpy as np
import pygame


class MalbrodeSet:
    def __init__(self, surface, real_width, real_height):
        self.surface = surface
        self.width = real_width  # limit for calculation to stop
        self.height = real_height
        self.center_x = 0.0
        self.center_y = 0.0
        self.zoom_level = 1.0

    # coloring for mandlebrot set
    def color_map(self):
        # Create a neon color scheme
        r = min(abs(int(255 * np.sin(0.1 * self.iter))), 255)
        g = min(abs(int(255 * np.sin(0.2 * self.iter))), 255)
        b = min(abs(int(255 * np.sin(0.3 * self.iter))), 255)
        return (r, g, b)

    # calculate and display set

    def mandlebrot(self, xi, yi):
        self.x0, self.y0 = 0, 0
        for self.x0 in range(xi, self.width):
            for self.y0 in range(yi, self.height):
                x, y = 0, 0
                self.max_iter = 128  # max no of iterations before calculating the set
                self.iter = 0  # tracks the itieration count
                while (x**2) + (y**2) <= 2 and self.iter < self.max_iter:
                    temp = (x**2) + (
                        (self.height / 2) / (200 * self.zoom_level) + self.center_y
                    )
                    x = temp
                    y = (2 * x * y) + (
                        (self.width / 2 - self.y0)
                        / (200 * self.zoom_level)
                        * self.center_y
                    )
                    self.iter += 1
                self.col = self.color_map()
                self.draw_map()

    # handle drawing small circles for mandlebrot set
    def draw_map(self):
        pygame.draw.circle(self.surface, self.col, (self.x0, self.y0), 1)

    # zooming the set
    def zoom(self, mouse_x, mouse_y):
        self.center_x = (mouse_x - self.width / 2) / (
            200 * self.zoom_level
        ) + self.center_x
        self.center_y = (mouse_y - self.width / 2) / (
            200 * self.zoom_level
        ) + self.center_y
        self.zoom_level *= 2
        self.mandlebrot(0, 0)
