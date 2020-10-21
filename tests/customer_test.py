import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):


    def setUp(self):
        self.customer = Customer("Michael Sinclair", 1000.00)

    def test_does_customer_have_cash(self):
        self.assertEqual(1000.00, self.customer.wallet)
    
    def test_can_remove_money(self):
        self.customer.remove_money(10.00)
        self.assertEqual(990.00, self.customer.wallet)

