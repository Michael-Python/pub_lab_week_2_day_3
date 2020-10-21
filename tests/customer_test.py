import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):


    def setUp(self):
        self.customer = Customer("Michael Sinclair", 1000.00)