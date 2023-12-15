"""
    CS5001 Fall 2023 SV
    Final Project
    Byunghyun Ko, Deo Gracias Ong, Xinrui Yi.
"""
import copy
import random
import time
import webbrowser
import pygame
from constants import *
from hand import Hand
from deck import Deck
from button import Button
from menu import *


# initializing pygame
clock = pygame.time.Clock()
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.mixer.init()


def display_instant_result(txt, x, y):
    """
    displays the result of the game if the round is ended early
    parameters: txt (string of result)
                x (int of x coordinate)
                y (int of y coordinate)
    returns: None
    """
    txt_display = textlargerfont.render(txt, True, red)  # Create a text surface
    gameDisplay.blit(txt_display, (x, y))  # Display the text
    pygame.display.update()  # Update the display
    time.sleep(2)


def visualize_cards(player, dealer, reveal):
    """
    Draws and displays the player's and dealer's cards on the game display.
    If reveal is True, both dealer's cards are shown. Otherwise, only one card is shown.
    """
    # Display player's hand
    player_cards = player.cards
    for i, card in enumerate(player_cards):
        card_text = textfont.render(str(card), True, black)
        # even number index cards are drawn in a straight line
        if i % 2 == 0:
            card_rect = pygame.Rect(600 + i * 100, 450, 130, 190)
        # odd number index cards are drawn in the position  lower than the even number index cards
        else:
            card_rect = pygame.Rect(600 + i * 100, 460, 130, 190)
        # Draw a rectangle
        pygame.draw.rect(gameDisplay, white, card_rect, 0, 5)
        gameDisplay.blit(card_text, (card_rect.x + 10, card_rect.y + 10))
        # Draw a rectangle with a border
        pygame.draw.rect(gameDisplay, red, card_rect, 5, 5)

    # Display dealer's hand
    dealer_cards = dealer.cards
    for i, card in enumerate(dealer_cards):
        card_text = textfont.render(str(card), True, black)
        # even number index cards are drawn in a straight line
        if i % 2 == 0:
            card_rect = pygame.Rect(600 + i * 100, 150, 130, 190)
        # odd number index cards are drawn in the position  lower than the even number index cards
        else:
            card_rect = pygame.Rect(600 + i * 100, 160, 130, 190)
        # Draw a rectangle
        pygame.draw.rect(gameDisplay, white, card_rect, 0, 5)
        # Hide the second card if reveal is False
        if i == 0 and not reveal:
            card_text = textfont.render("??", True, black)
        gameDisplay.blit(card_text, (card_rect.x + 10, card_rect.y + 10))
        # Draw a rectangle with a border
        pygame.draw.rect(gameDisplay, red, card_rect, 5, 5)

    player_hand_text = textfont.render("Player's Hand: ", True, black)
    dealer_hand_text = textfont.render("Dealer's Hand: ", True, black)

    gameDisplay.blit(player_hand_text, (300, 450))
    gameDisplay.blit(dealer_hand_text, (300, 150))

    pygame.display.update()


def choose_bet():
    """
    displays a screen for the user to select which bet size they would like to choose
    parameters: None
    returns: bet (int)
    """
    menu_effect.play()
    # creating a button for the betting options
    button_5 = Button("$5", 30, 315, 150, 50)
    button_10 = Button("$10", 280, 315, 150, 50)
    button_25 = Button("$25", 530, 315, 150, 50)
    button_50 = Button("$50", 780, 315, 150, 50)
    button_100 = Button("$100", 1003, 315, 150, 50)
    button_reset = Button("Reset", 420, 500, 150, 50)
    button_bet = Button("Bet", 620, 500, 150, 50)

    bet = 0
    run = True
    while run:
        gameDisplay.blit(scaled_image, [0, 0])
        pygame.draw.rect(
            gameDisplay, black, pygame.Rect(0, 250, display_width, display_height / 4)
        )

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
                return run, bet

        # checking if a button was clicked and acting accordingly
        if button_5.check_click():
            bet += 5
        if button_10.check_click():
            bet += 10
        if button_25.check_click():
            bet += 25
        if button_50.check_click():
            bet += 50
        if button_100.check_click():
            bet += 100
        if button_reset.check_click():
            bet = 0
        if button_bet.check_click():
            run = False

        # draws the buttons
        button_5.draw()
        button_10.draw()
        button_25.draw()
        button_50.draw()
        button_100.draw()
        button_reset.draw()
        button_bet.draw()

        # visualize the current bet state
        pygame.draw.circle(gameDisplay, black, (600, 125), 90)
        surf = font_bet.render(f"${bet}", True, white)
        gameDisplay.blit(surf, (550, 95))

        pygame.display.update()
    run = True
    menu_effect.stop()
    return run, bet


def player_action(player, shoe, bet, dealer):
    """
    performs all actions requested by the player
    determines which button is clicked by user then acts accordingly
    parameters: player (object: Class Hand)
    returns: bet (int, value of the bet)
    """

    # creating the player action buttons
    hit_button = Button("Hit", 30, 200, 150, 50)
    stand_button = Button("Stand", 30, 300, 150, 50)
    double_button = Button("Double", 30, 400, 150, 50)

    run = True
    while run:
        gameDisplay.blit(scaled_image, [0, 0])
        pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
                return run, bet

        # checking if the hit button was clicked and acting accordingly
        if hit_button.check_click():
            player.add_card(shoe.draw_card())
            player.calc_value()
            sound_effect.play()
            if player.get_value() > 21:
                run = False

        # checking if the stand button was clicked and acting accordingly
        if stand_button.check_click():
            run = False

        # checking if the double button was clicked and acting accordingly
        if double_button.check_click():
            player.add_card(shoe.draw_card())
            player.calc_value()
            sound_effect.play()
            bet *= 2
            run = False

        # drawing the buttons
        hit_button.draw()
        stand_button.draw()
        double_button.draw()
        visualize_cards(player, dealer, reveal=False)

        pygame.display.update()
    run = True
    return run, bet


def dealer_action(player, dealer, shoe):
    """
    performs all actions of a dealer once the player action is over
    draws cards until the dealer's card values are over 16
    """
    visualize_cards(player, dealer, reveal=True)
    sound_effect.play()
    time.sleep(1)
    # while dealer's hand is less than 16, add card to dealer hand
    while dealer.get_value() <= 16:
        dealer.add_card(shoe.draw_card())
        dealer.calc_value()
        visualize_cards(player, dealer, reveal=True)
        sound_effect.play()
        time.sleep(1)


def main():
    decks = 8
    cut_off = 52 * decks * 0.20

    # initialize a deck class here
    shoe = Deck()

    # initialize stats
    wins = 0
    losses = 0
    pushes = 0
    rounds = 0

    # initialize bankroll
    bank = 0

    pygame.display.set_caption("Pygame Blackjack!")
    gameDisplay.blit(scaled_image, [0, 0])
    pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

    run = start_menu()

    while (shoe.get_remaining_cards() > cut_off) and run:
        # generate user input for bet
        run, bet = choose_bet()
        if not run:
            continue

        # create player hand (object)
        # create dealer hand (object)
        player = Hand(cards=[], value=0)
        dealer = Hand(cards=[], value=0)

        gameDisplay.blit(scaled_image, [0, 0])
        pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 220, 700))

        for i in range(2):
            player.add_card(shoe.draw_card())
            visualize_cards(player, dealer, reveal=False)
            sound_effect.play()
            time.sleep(0.5)
            dealer.add_card(shoe.draw_card())
            visualize_cards(player, dealer, reveal=False)
            sound_effect.play()
            time.sleep(0.5)

        player.calc_value()
        dealer.calc_value()

        # create a loop for player action
        # generate user input to determine action
        # display new player hand
        if player.get_value() == 21 and dealer.get_value() != 21:
            wins += 1
            bank += 1.5 * bet
            rounds += 1
            display_instant_result("BlackJack", 900, 350)
            win_status = "won"
            win_effect.play()
            end_of_round_menu(win_status.upper(), bank, wins, losses, rounds, pushes)
            continue

        if player.get_value() == 21 and dealer.get_value() == 21:
            pushes += 1
            rounds += 1
            display_instant_result("Double Blackjack", 900, 350)
            win_status = "push"
            push_effect.play()
            end_of_round_menu(win_status.upper(), bank, wins, losses, rounds, pushes)
            continue

        if dealer.get_value() == 21 and player.get_value() != 21:
            losses += 1
            bank -= bet
            rounds += 1
            visualize_cards(player, dealer, reveal=True)
            display_instant_result("Dealer Blackjack", 800, 50)
            win_status = "lost"
            lose_effect.play()
            end_of_round_menu(win_status.upper(), bank, wins, losses, rounds, pushes)
            continue

        # player's turn to act
        run, bet = player_action(player, shoe, bet, dealer)
        if not run:
            continue

        if player.get_value() > 21:
            losses += 1
            bank -= bet
            rounds += 1
            display_instant_result("You Busted", 900, 350)
            win_status = "lost"
            lose_effect.play()
            end_of_round_menu(win_status.upper(), bank, wins, losses, rounds, pushes)
            continue
        # create loop for dealer action
        # hit until can no longer hit or bust
        # display new dealer hand
        time.sleep(1)
        dealer_action(player, dealer, shoe)

        if dealer.get_value() > 21:
            wins += 1
            bank += bet
            rounds += 1
            display_instant_result("Dealer Busted", 800, 50)
            win_status = "won"
            win_effect.play()
            end_of_round_menu(win_status.upper(), bank, wins, losses, rounds, pushes)
            continue

        time.sleep(1)
        # determine who won
        # calculate the remaining balance of the player
        if player.get_value() < dealer.get_value():
            losses += 1
            bank -= bet
            rounds += 1
            win_status = "lost"
            lose_effect.play()

        elif player.get_value() > dealer.get_value():
            wins += 1
            bank += bet
            rounds += 1
            win_status = "won"
            win_effect.play()

        else:
            pushes += 1
            rounds += 1
            win_status = "push"
            push_effect.play()

        run = end_of_round_menu(win_status.upper(), bank, wins, losses, rounds, pushes)
    pygame.quit()


if __name__ == "__main__":
    main()
