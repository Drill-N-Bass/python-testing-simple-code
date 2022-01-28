import unittest
from fractions import Fraction


from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers: 
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)



class TestSumNot6(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers - here the list != 6:
        """
        data = [1, 2, 10]
        result = sum(data)
        self.assertEqual(result, 6)

class TestSumStringList(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers - here the list != 6 and one of list's object is a string:
        """
        data = [1, 2, "Cat"]
        result = sum(data)
        self.assertEqual(result, 6)

class TestSumFraction(unittest.TestCase):
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)





if __name__ == '__main__':
    unittest.main()
