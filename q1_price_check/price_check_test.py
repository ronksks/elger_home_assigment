import unittest
from price_check import price_check


class TestPriceCheck(unittest.TestCase):
    def test_price_check_first_data(self):
        self.assertEqual(price_check(['eggs', 'milk', 'cheese'],
                                     [2.89, 3.29, 5.79],
                                     ['eggs', 'eggs', 'cheese', 'milk'],
                                     [2.89, 2.99, 5.97, 3.29]), 2)

    def test_price_check_second_data(self):
        self.assertEqual(price_check(['rice', 'sugar', 'wheat', 'cheese'],
                                     [16.89, 56.92, 20.89, 345.99],
                                     ['rice', 'cheese'],
                                     [18.99, 400.89]), 2)
