import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_vowels_ignored(self):
        self.assertEqual(generate_soundex("AeioU"), "A000")

    def test_double_letters(self):
        self.assertEqual(generate_soundex("Bobb"), "B100")

    def test_name_with_h_and_w(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")

    def test_name_with_vowels_separating(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")

    def test_mixed_case(self):
        self.assertEqual(generate_soundex("RoBeRt"), "R163")

    def test_short_name(self):
        self.assertEqual(generate_soundex("Li"), "L000")

    def test_name_with_no_mappable_consonants(self):
        self.assertEqual(generate_soundex("AEIOU"), "A000")

    def test_name_with_repeated_consonants_separated_by_vowels(self):
        self.assertEqual(generate_soundex("BaeiouBB"), "B100")

if __name__ == '__main__':
    unittest.main()
