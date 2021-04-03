import unittest
from balanced_bracket import check


class Test(unittest.TestCase):

    def test_1(self):
        string = '{[]{()}}'
        self.assertTrue(check(string))

    def test_2(self):
        string = '[{}{})(]'
        self.assertFalse(check(string))

    def test_3(self):
        string = '((()'
        self.assertFalse(check(string))



if __name__ == "__main__":
    unittest.main()

