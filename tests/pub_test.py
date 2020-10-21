import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("White Russian", 10)
        self.drink_2 = Drink("Dolce Banana", 15)
        
        drinks = [self.drink_1, self.drink_2]
        self.pub = Pub("The Prancing Pony", 100.00, drinks)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_does_till_have_cash(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_can_add_money(self):
        self.pub.add_money(10.00)
        self.assertEqual(110.00, self.pub.till)

    def test_pub_stock_count(self):
        self.assertEqual(2, self.pub.drink_count())

    def test_can_add_drink_to_stock(self):
        new_drink = Drink("White Russian", 10)
        self.pub.add_drink(new_drink)
        self.assertEqual(3, self.pub.drink_count())

    def test_can_find_drink_by_name(self):
        self.pub.find_drink_by_name(self.drink_1)
        self.assertEqual("White Russian", self.drink_1.name)

    # def test_sell_drink_to_customer(self):
    #     customer = Customer("Michael Sinclair", 1000)
