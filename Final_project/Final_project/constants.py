import pygame as pygame

display_width = 1200
display_height = 700

background_color = (34, 139, 34)
background_image = pygame.image.load("png/background.jpg")
menu_background_image = pygame.image.load("png/menu_background.jpg")
scaled_image = pygame.transform.scale(background_image, (display_width, display_height))
scaled_menu_image = pygame.transform.scale(menu_background_image, (display_width, display_height))
grey = (220, 220, 220)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (255, 0, 0)
light_slat = (119, 136, 153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)
pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont("Times New Roman", 35)
textlargerfont = pygame.font.SysFont("Times New Roman", 50)
game_end = pygame.font.SysFont("dejavusans", 100)
blackjack = pygame.font.SysFont("roboto", 70)


SUITS = ["C", "S", "H", "D"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)

font = pygame.font.SysFont("Georgia", 25, bold=True)
surf_hit = font.render("Hit", True, "white")
surf_stand = font.render("Stand", True, "white")
surf_double = font.render("Double", True, "white")

font_bet = pygame.font.SysFont("Georgia", 50, bold=True)
font_startmenu = pygame.font.SysFont("Times New Roman", 35)

sound_effect = pygame.mixer.Sound("sounds/card_sound.mp3")
win_effect = pygame.mixer.Sound("sounds/win_sound.mp3")
lose_effect = pygame.mixer.Sound("sounds/lose_sound.mp3")
menu_effect = pygame.mixer.Sound("sounds/menu_sound.mp3")
push_effect = pygame.mixer.Sound("sounds/push_sound.mp3")