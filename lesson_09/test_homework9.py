import unittest

try:
    from lesson_09.homework9 import multiplication_table, sum_value, average, opposite, longest
except ImportError:
    from homework9 import multiplication_table, sum_value, average, opposite, longest

class TestFunctions(unittest.TestCase):
    """Positive case for multiplication_table"""
    def test_positive_test_01(self):
        self.assertEqual(multiplication_table(5), True)
    """Negative case for multiplication_table"""
    def test_negative_test_02(self):
        self.assertEqual(multiplication_table("5"), False)
    
    """Positive case for sum_value"""
    def test_positive_test03(self):
        self.assertEqual(sum_value(4, 5), 9)
    """Negative case for sum_value"""
    def test_negative_test04(self):
        self.assertEqual(sum_value("4", 5), False)

    """Positive case for average"""
    def test_positive_test05(self):
        self.assertEqual(average([1, 2, 3, 6]), 3)
    """Negative case for average"""
    def test_negative_test06(self):
        self.assertEqual(average("list"), "EXCEPTION")

    """Positive case for opposite"""
    def test_positive_test07(self):
        self.assertEqual(opposite("world"), ["d", "l", "r", "o", "w"])
    """Positive case for opposite"""
    def test_positive_test08(self):
        self.assertEqual(opposite(["H", "e", "l", "l", "o"]), ["o", "l", "l", "e", "H"])
    """Positive case for opposite"""
    def test_positive_test08(self):
        self.assertEqual(opposite([1,2,3,4]), [4,3,2,1])

    """Positive case for longest"""
    def test_positive_test09(self):
        self.assertEqual(longest(["Hello", "Pet", "Darling"]), "Darling")
    """Negative case for longest"""
    def test_negative_test10(self):
        self.assertEqual(longest([1, 2, 3, 4, 5]), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)