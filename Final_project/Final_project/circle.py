import pygame
from constants import *

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))


class Circle:
    def __init__(self, msg, x, y, radius):
        self.txt = msg
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.rect.topleft = (x, y)
        self.clicked = False
        self.radius = radius

    def draw_circle(self):
        # draw button on screen

        pygame.draw.circle(gameDisplay, red, self.rect.center, self.radius, width=0)

        if self.txt == "$5":
            surf = scaled_five_image
        elif self.txt == "$10":
            surf = scaled_ten_image
        elif self.txt == "$25":
            surf = scaled_twentyfive_image
        elif self.txt == "$50":
            surf = scaled_fifty_image
        else:
            surf = scaled_hundred_image

        rect = surf.get_rect()
        rect.center = (
            (self.rect.x + (self.rect.w / 2)),
            (self.rect.y + (self.rect.h / 2)),
        )
        gameDisplay.blit(surf, rect)

    def check_click(self):
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                return True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return False
