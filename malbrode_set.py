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
        self.max_iter = 128  # max no of iterations before calculating the set
        self.iter = 0  # tracks the itieration count

    # coloring for mandlebrot set
    def color_map(self):
        if self.iter >= self.max_iter:
            return (0, 0, 0)
        # Create a neon color scheme
        r = min(abs(int(255 * np.sin(0.1 * self.iter))), 255)
        g = min(abs(int(255 * np.sin(0.2 * self.iter))), 255)
        b = min(abs(int(255 * np.sin(0.3 * self.iter))), 255)
        return (r, g, b)

    # calculate and display set
    def mandlebrot(self):
        scale = 200 * self.zoom_level
        self.cx0, self.cy0 = self.width / 2, self.height / 2
        for x0 in range(self.width):
            c_x = (x0 - self.cx0) / scale + self.center_x
            for y0 in range(self.height):
                c_y = (y0 - self.cy0) / scale + self.center_x
                x = y = 0.0
                self.iter = 0
                while x * x + y * y <= 4 and self.iter < self.max_iter:
                    temp = x * x - y * y + c_x
                    y = 2 * x * y + c_y
                    x = temp
                    self.iter += 1
                # draw small circles
                pygame.draw.circle(self.surface, self.color_map(), (x0, y0), 1)

    # zooming the set
    def zoom(self, mouse_x, mouse_y):
        scale = 200 * self.zoom_level
        self.center_x += (mouse_x - self.width / 2) / scale
        self.center_y += (mouse_y - self.height / 2) / scale
        self.zoom_level *= 2
