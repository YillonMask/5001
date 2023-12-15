import pygame
from constants import *

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))


class Button:

    def __init__(self, msg, x, y, width, height):
        self.txt = msg
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        # draw button on screen

        pygame.draw.rect(gameDisplay, light_slat, self.rect)

        surf = font.render(self.txt, True, black)
        rect = surf.get_rect()
        rect.center = ((self.rect.x + (self.rect.w / 2)), (self.rect.y + (self.rect.h / 2)))
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
