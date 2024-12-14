import unittest
from romans.converter import int_to_roman

class TestIntToRoman(unittest.TestCase):
    def test_one(self):
        self.assertEqual(int_to_roman(1), "I")
    
    def test_five(self):
        self.assertEqual(int_to_roman(5), "V")
    
    def test_ten(self):
        self.assertEqual(int_to_roman(10), "X")
    
    def test_complex(self):
        self.assertEqual(int_to_roman(1987), "MCMLXXXVII")

if __name__ == "__main__":
    unittest.main()
