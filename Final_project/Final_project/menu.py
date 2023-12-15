import pygame
import webbrowser
from constants import *

# initializing display
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))


def start_menu():
    # display the background image for the start menu
    gameDisplay.blit(scaled_menu_image, [0, 0])
    run = True
    # while run is true display title, text, instructions to the screen
    while run:
        font = pygame.font.SysFont('Times New Roman', 40)
        title_text = font.render("BLACKJACK", True, (255, 255, 255))
        deal_text = font.render("Press SPACE to Deal", True, (255, 255, 255))
        instruction_text = font.render("Press i for Instructions & Credits", True, (255, 255, 255))
        exit_text = font.render("Press ESC to Exit", True, (255, 255, 255))
        gameDisplay.blit(title_text, (display_width / 2 - title_text.get_width() / 2,
                                      display_height / 7 - title_text.get_height() / 2))
        gameDisplay.blit(deal_text,
                         (display_width / 2 - deal_text.get_width() / 2,
                          display_height / 3.0 - deal_text.get_height() / 2))
        gameDisplay.blit(exit_text,
                         (display_width / 2 - exit_text.get_width() / 2,
                          display_height / 1.5 - exit_text.get_height() / 2))
        gameDisplay.blit(instruction_text,
                         (display_width / 2 - instruction_text.get_width() / 2,
                          display_height / 2.25 - instruction_text.get_height() / 2))
        # update the display
        pygame.display.update()
        # handling action when respective key is pressed
        for event in pygame.event.get():
            # if x box is pressed, quit game
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # if ESC is pressed, then quit the game completely
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                # if i is pressed change to the instruction screen
                elif event.key == pygame.K_i:
                    instruction()
                # if d is pressed continue on the main function
                elif event.key == pygame.K_SPACE:
                    return True
    return run


def instruction():
    # display the background image for the instruction menu
    gameDisplay.blit(scaled_menu_image, [0, 0])
    run = True
    # while run is true display title and text to the screen
    while run:
        font = pygame.font.SysFont('Times New Roman', 35)
        credit_font = pygame.font.SysFont('Times New Roman', 25)
        title_text = font.render("Instructions & Credit", True, (255, 255, 255))
        return_text = font.render("Press R to return to the start menu", True, (255, 255, 255))
        credit_text_1 = credit_font.render("Northeastern University CS 5001 Final Project", True,
                                           (255, 255, 255))
        credit_text_2 = credit_font.render("Created by: Byunghyun Ko, Deo Gracias Ong, Xinrui Yi", True,
                                           (255, 255, 255))
        instruction_link = font.render("Press HERE for instructions", True, (255, 255, 255))
        gameDisplay.blit(title_text, (display_width / 2 - title_text.get_width() / 2,
                                      display_height / 10 - title_text.get_height() / 2))
        gameDisplay.blit(return_text, (display_width / 2 - return_text.get_width() / 2,
                                       display_height / 2.6 - return_text.get_height() / 2))
        gameDisplay.blit(credit_text_1, (display_width / 2 - credit_text_1.get_width() / 2,
                                         display_height / 1.2 - credit_text_1.get_height() / 2))
        gameDisplay.blit(credit_text_2, (display_width / 2 - credit_text_2.get_width() / 2,
                                         display_height / 1.1 - credit_text_2.get_height() / 2))
        instruction_link = gameDisplay.blit(instruction_link,
                                            (display_width / 2 - instruction_link.get_width() / 2,
                                             display_height / 2 - instruction_link.get_height() / 2))
        # update the display
        pygame.display.update()
        # handling action when respective key is pressed
        for event in pygame.event.get():
            # if x box is pressed, quit game
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # if r is pressed return True to return to start menu
                if event.key == pygame.K_r:
                    # reset the background image
                    gameDisplay.blit(scaled_menu_image, [0, 0])
                    return True
            # if the "press here" is pressed open the link to blackjack rules
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if instruction_link.collidepoint(event.pos):
                    webbrowser.open(r"https://bicyclecards.com/how-to-play/blackjack/")
                    # update display
                    pygame.display.update()
    return run


def end_of_round_menu(win_status, bank, wins, losses, rounds, pushes):
    # display the background image for the end of round menu
    gameDisplay.blit(scaled_menu_image, [0, 0])
    run = True
    # while run is true display the text for instructions/statistics
    while run:
        font = pygame.font.SysFont('Times New Roman', 33)
        title_font = pygame.font.SysFont('Times New Roman', 40, False)
        statistics_font = pygame.font.SysFont('Times New Roman', 33, False)
        exit_font = pygame.font.SysFont('Times New Roman', 37, False)
        title_text = title_font.render("YOU " + win_status + " THIS ROUND.", True, (255, 0, 0))
        deal_text = font.render("Press SPACE to Deal Again", True, (255, 255, 255))
        instruction_text = font.render("Press i for Instructions", True, (255, 255, 255))
        exit_text = exit_font.render("Press ESC to Exit", True, (255, 255, 255))

        bank_text = statistics_font.render("Total Gains or Losses: " + str(bank) + " USD", True,
                                           (255, 255, 255))
        rounds_text = statistics_font.render("Rounds Played: " + str(rounds), True, (255, 255, 255))
        wins_text = statistics_font.render("Wins: " + str(wins), True, (255, 255, 255))
        losses_text = statistics_font.render("Losses: " + str(losses), True, (255, 255, 255))
        pushes_text = statistics_font.render("Pushes: " + str(pushes), True, (255, 255, 255))

        gameDisplay.blit(title_text, (display_width / 2 - title_text.get_width() / 2,
                                      display_height / 7 - title_text.get_height() / 2))
        gameDisplay.blit(deal_text,
                         (display_width / 4.22 - deal_text.get_width() / 2,
                          display_height / 2.5 - deal_text.get_height() / 2))
        gameDisplay.blit(exit_text,
                         (display_width / 2 - exit_text.get_width() / 2,
                          display_height / 1.5 - exit_text.get_height() / 2))
        gameDisplay.blit(instruction_text,
                         (display_width / 4.8 - instruction_text.get_width() / 2,
                          display_height / 3.5 - instruction_text.get_height() / 2))
        gameDisplay.blit(bank_text,
                         (display_width / 1.3 - bank_text.get_width() / 2,
                          display_height / 3.5 - bank_text.get_height() / 2))
        gameDisplay.blit(rounds_text,
                         (display_width / 1.3 - rounds_text.get_width() / 2,
                          display_height / 3.0 - rounds_text.get_height() / 2))
        gameDisplay.blit(wins_text,
                         (display_width / 1.3 - wins_text.get_width() / 2,
                          display_height / 2.65 - wins_text.get_height() / 2))
        gameDisplay.blit(losses_text,
                         (display_width / 1.3 - losses_text.get_width() / 2,
                          display_height / 2.4 - losses_text.get_height() / 2))
        gameDisplay.blit(pushes_text,
                         (display_width / 1.3 - losses_text.get_width() / 2,
                          display_height / 2.16 - losses_text.get_height() / 2))
        pygame.display.update()
        # handling action when respective key is pressed
        for event in pygame.event.get():
            # if x box is pressed, quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                # if escape key is pressed quit the game completely
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                # if i is pressed change to the instruction screen
                elif event.key == pygame.K_i:
                    instruction()
                # if d is pressed continue on the main game function
                elif event.key == pygame.K_SPACE:
                    return True
    return run
