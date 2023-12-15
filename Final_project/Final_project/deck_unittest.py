"""
unittests for deck.py
"""
import unittest
from deck import Deck
import random

random.seed(10)


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        # Deck() creates a shoe(a stack of decks) with 8 Decks

    def test_draw_card(self):
        # Test drawing a card from the deck
        self.assertEqual(self.deck.draw_card(), "J")
        self.assertEqual(self.deck.draw_card(), "2")
        card = self.deck.draw_card()
        self.assertIn(card, self.deck.remaining_cards)

    def test_shuffle(self):
        # Test shuffling the deck
        self.deck.shuffle()
        self.assertEqual(self.deck.get_remaining_cards(), 416)
        self.assertEqual(self.deck.drawn_count, 0)

    def test_get_drawn_count(self):
        # Test getting the number of cards drawn
        self.assertEqual(self.deck.get_drawn_count(), 0)
        self.deck.draw_card()
        self.assertEqual(self.deck.get_drawn_count(), 1)

    def test_get_remaining_cards(self):
        # Test getting the number of remaining cards in the deck
        self.assertEqual(self.deck.get_remaining_cards(), 416)
        self.deck.draw_card()
        self.assertEqual(self.deck.get_remaining_cards(), 415)


if __name__ == "__main__":
    unittest.main()
