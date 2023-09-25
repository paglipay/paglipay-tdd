import unittest
# from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        #jenkins webhook test
        self.assertEqual('hello world', 'hello world')