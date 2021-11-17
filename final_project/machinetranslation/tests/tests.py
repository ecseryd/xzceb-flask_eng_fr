import unittest
import translator

class testTranslate(unittest.TestCase):
    def test_frenchToEnglish_null_input(self):
        with self.assertRaises(ValueError):
            val = translator.frenchToEnglish(None)

    def test_frenchToEnglish_word_input(self):
        val = translator.frenchToEnglish('Bonjour')
        self.assertEqual(val, 'Hello')

    def test_EnglishToFrench_null_input(self):
        with self.assertRaises(ValueError):
            val = translator.englishToFrench(None)

    def test_EnglishToFrench_word_input(self):
        val = translator.englishToFrench('Hello')
        self.assertEqual(val, 'Bonjour')

if __name__ == "__main__":
    unittest.main()