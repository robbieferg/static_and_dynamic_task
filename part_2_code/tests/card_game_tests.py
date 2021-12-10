import unittest
from src.card import Card
from src.card_game import CardGame

card_1 = Card("hearts", 1)
card_2 = Card("diamonds", 5)

class TestCardGame(unittest.TestCase):
    def test_check_for_ace(self):
        expected = True
        actual = CardGame.check_for_ace(self, card_1)
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        expected = card_2
        actual = CardGame.highest_card(self, card_1, card_2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        cards = [card_1, card_2]
        expected = "You have a total of 6"
        actual = CardGame.cards_total(self, cards)
        self.assertEqual(expected, actual)
