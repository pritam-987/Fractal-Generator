import random

import pygame


class Serpinski:
    def __init__(self, surf, x, y, depth):
        self.surf = surf
        self.x = x
        self.y = y
        self.depth = depth
        self.points = 0
        self.max_points = 10**6

    def chaos_game(self, color, pos):

        for _ in range(self.depth):
            if self.points >= self.max_points:
                break
            else:
                self.pos = random.choice(pos)
                self.x = (self.x + self.pos[0]) / 2
                self.y = (self.y + self.pos[1]) / 2
                self.points += 1
                pygame.draw.circle(self.surf, color, (self.x, self.y), 1)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.points = 0

        self.surf.fill((0, 0, 0))
