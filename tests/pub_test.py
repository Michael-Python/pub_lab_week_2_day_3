import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        # this sets up the list with two list items
        self.drink_1 = Drink("Brew Dog", 5)
        self.drink_2 = Drink("Dolce Banana", 15)
        # this says that the two items go in the list
        drinks = [self.drink_1, self.drink_2]
        # this gives values to the parameters to Class pub
        self.pub = Pub("The Prancing Pony", 100.00, drinks)

    def test_pub_has_name(self):
        # this checks if the pub has a name
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_does_till_have_cash(self):
        # this checks if the pub has cash
        self.assertEqual(100.00, self.pub.till)
    
    def test_can_add_money(self):
        # this checks if the pub can have money added
        self.pub.add_money(10.00)
        self.assertEqual(110.00, self.pub.till)

    def test_pub_stock_count(self):
        # this checks if the pub has 2 in its list
        self.assertEqual(2, self.pub.drink_count())

    def test_can_add_drink_to_stock(self):
        # this sets up a new drink with its price
        new_drink = Drink("White Russian", 10)
        # this calls the add_drink method from pub.py and adds the drink assigned to new_drink
        self.pub.add_drink(new_drink)
        # this checks if the list now has three items, the 2 in the list and the 1 added
        self.assertEqual(3, self.pub.drink_count())

    def test_can_find_drink_by_name(self):
        # this calls the find_drink_by_name method from pub.py and checking the drinks in the list
        self.pub.find_drink_by_name(self.drink_1)
        # this checks the name of the drink against name in the list
        self.assertEqual("Brew Dog", self.drink_1.name)

    def test_sell_drink_to_customer(self):
        
        customer = Customer("Michael Sinclair", 1000)
        self.pub.sell_drink_to_customer("Brew Dog", customer)
        # don't need 'self'.customer because customer is an instance in this method
        self.assertEqual(995, customer.wallet)
        self.assertEqual(105, self.pub.till)
        