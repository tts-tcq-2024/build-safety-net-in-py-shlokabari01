import unittest
from Soundex import generate_soundex  # Ensure this matches the filename

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_encode_name(self):
        self.assertEqual(generate_soundex("Aeiou"), "A000")

    def test_long_string(self):
        self.assertEqual(generate_soundex("Jackandsmith"), "J532")

    def test_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("1234"), "1000")

    def test_mixed_chars(self):
        self.assertEqual(generate_soundex("Jackfruit@home"), "J163")

if __name__ == '__main__':
    unittest.main()
