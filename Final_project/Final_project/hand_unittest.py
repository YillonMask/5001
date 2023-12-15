"""
Unittest for the Hand class.
"""
import unittest
from hand import Hand, CARD_VALUE


class TestHand(unittest.TestCase):
    """
    Test case for the Hand class.
    """

    def test_add_card(self):
        """
        Test the add_card method.
        """

        self.hand = Hand(cards=[], value=0)
        self.hand.add_card("A")
        self.hand.add_card("K")
        self.assertEqual(self.hand.cards, ["A", "K"])

    def test_calc_value(self):
        """
        Test the calc_value method.
        """
        # Test case 1: Hand with '2' and '4' should have a value of 6
        self.hand = Hand(cards=[], value=0)
        self.hand.add_card("2")
        self.hand.add_card("4")
        self.hand.calc_value()
        self.assertEqual(self.hand.value, 6)

        # Test case 2: Hand with '2', '3', and '4' should have a value of 9
        self.hand = Hand(cards=[], value=0)
        self.hand.add_card("2")
        self.hand.add_card("3")
        self.hand.add_card("4")
        self.hand.calc_value()
        self.assertEqual(self.hand.value, 9)

        # Test case 3: Hand with 'J', 'Q', and 'K' should have a value of 30
        self.hand = Hand(cards=[], value=0)
        self.hand.add_card("J")
        self.hand.add_card("Q")
        self.hand.add_card("K")
        self.hand.calc_value()
        self.assertEqual(self.hand.value, 30)

        # Test edgy case: Hand with 'A', 'A', and 'A' should have a value of 13
        self.hand = Hand(cards=[], value=0)
        self.hand.add_card("A")
        self.hand.add_card("A")
        self.hand.add_card("A")
        self.hand.calc_value()
        self.assertEqual(self.hand.value, 13)

    def test_get_value(self):
        # Test case 1: Hand with '6' and '8' should have a value of 14
        self.hand = Hand(cards=[], value=0)
        self.hand.add_card("6")
        self.hand.add_card("8")
        self.hand.calc_value()
        self.assertEqual(self.hand.get_value(), 14)

    def test_str(self):
        # Test case 1: Hand with 'A' and 'K'
        self.hand = Hand(cards=[], value=0)
        self.hand.add_card("A")
        self.hand.add_card("K")
        self.hand.calc_value()
        self.assertEqual(
            str(self.hand), "Current player's hand is A K with a value of 21"
        )


if __name__ == "__main__":
    unittest.main()
