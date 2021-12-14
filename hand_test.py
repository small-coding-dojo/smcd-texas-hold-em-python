import unittest
from hand import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]), ('nothing', ['A', 'K', 'Q', 'J', '9']))  # add assertion here

if __name__ == '__main__':
    unittest.main()
