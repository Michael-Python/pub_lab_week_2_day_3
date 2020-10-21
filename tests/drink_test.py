import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Brew Dog", 5)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)

        
