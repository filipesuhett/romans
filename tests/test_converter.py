# tests/test_converter.py\
import unittest
import sys
import os
# Adiciona o diretório 'src' ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from romans.converter import int_to_roman

class TestIntToRoman(unittest.TestCase):
    def test_one(self):
        self.assertEqual(int_to_roman(1), "I")
    
    def test_two(self):
        self.assertEqual(int_to_roman(2), "II")
    
    def test_three(self):
        self.assertEqual(int_to_roman(3), "III")
    
    def test_four(self):
        self.assertEqual(int_to_roman(4), "IV")
    
    def test_five(self):
        self.assertEqual(int_to_roman(5), "V")
    
    def test_ten(self):
        self.assertEqual(int_to_roman(10), "X")
    
    def test_twenty_nine(self):
        self.assertEqual(int_to_roman(29), "XXIX")
    
    def test_forty_four(self):
        self.assertEqual(int_to_roman(44), "XLIV")
    
    def test_ninety_nine(self):
        self.assertEqual(int_to_roman(99), "XCIX")
    
    def test_four_hundred(self):
        self.assertEqual(int_to_roman(400), "CD")
    
    def test_five_hundred(self):
        self.assertEqual(int_to_roman(500), "D")
    
    def test_one_thousand(self):
        self.assertEqual(int_to_roman(1000), "M")
    
    def test_three_thousand_nine_hundred_ninety_nine(self):
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")
        
    def test_complex_number(self):
        self.assertEqual(int_to_roman(1987), "MCMLXXXVII")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

if __name__ == "__main__":
    unittest.main()
